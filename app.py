from flask import Flask, request, Response, render_template, jsonify
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XML, fromstring, tostring
import re
from CARS_calculator import CARS_calculator
from cacheSFTables import cacheSFTables
import pickle
import os
from snowflake_connector import snowflake_connector
import logging
import datetime
import json
from S3_helper import S3_helper
import time


os.makedirs(os.path.dirname('logs/'), exist_ok=True)
applog_filename = "logs/app_log.log"
reclog_filename = "logs/request_rec.txt"
logging.basicConfig(filename=applog_filename, level=logging.DEBUG)
BUCKET_NAME = 'cars-recommendation-logs-prod'

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "Welcome to CAR Recommendation Service Prod!"


@app.route("/transfer_log")
def transfer_log():
	SourceFileDict = {applog_filename: "app_log/"+applog_filename,
					  reclog_filename: "request_rec/"+reclog_filename}
	try:
		for source_filename in SourceFileDict:
			now = time.time()
			S3_helper(source_filename, BUCKET_NAME, "{}_{}".format(SourceFileDict[source_filename],now))
		return "Log files have been successfully transferred into s3 bucket - {} at {}.".format(BUCKET_NAME, now)
	except:
		return "ERROR: Log files have NOT been successfully transferred into s3 bucket." 


# SAVE THE SNOWFALKE TABLES INTO A PICKLE FILE
@app.route('/schedule_database_lookup', methods=['POST', "GET"])
def schedule_database_lookup():
	cache = cacheSFTables()
	return cache.cacheTables()

#http://127.0.0.1:5000/get_guideline
@app.route('/get_guideline', methods = ['POST'])
def xml_example():
	req_data = request.get_data('req_data')
	tree = ET.fromstring(req_data)
	elementsDict = {}
	for ele in tree.findall("."):
		elementsDict["DivisionCode"] = (str(ele.find('{PACCAR.SMKTG.CAR.Model.Core}DivisionCode').text))
		elementsDict["PriceProtectionDt"] =(str(ele.find('{PACCAR.SMKTG.CAR.Model.Core}PriceProtectionDt').text[0:10].replace("-","/")))
		elementsDict["RequestedEndDate"] =(str(ele.find('{PACCAR.SMKTG.CAR.Model.Core}RequestedEndDate').text[0:10].replace("-","/")))
		elementsDict["CCSalesOptionCd"] =(str(ele.find('{PACCAR.SMKTG.CAR.Model.Core}CCSalesOptionCd').text))
		elementsDict["MarketModel"] =(str(ele.find('{PACCAR.SMKTG.CAR.Model.Core}MarketModel').text))
		elementsDict["DealerList"] =(str(ele.find('{PACCAR.SMKTG.CAR.Model.Core}DealerList').text))
		elementsDict["MinQuantity"] =(str(ele.find('{PACCAR.SMKTG.CAR.Model.Core}MinQuantity').text))
		elementsDict["CustomerName"] =(str(ele.find('{PACCAR.SMKTG.CAR.Model.Core}CustomerName').text))
		elementsDict["RequestedCARPercent"] =(str(ele.find('{PACCAR.SMKTG.CAR.Model.Core}RequestedCARPercent').text))
		elementsDict["DealerNet"] =(str(ele.find('{PACCAR.SMKTG.CAR.Model.Core}DealerNet').text))
		elementsDict["DealerCd"] =(str(ele.find('{PACCAR.SMKTG.CAR.Model.Core}DealerCd').text))
		for info in tree.findall('.//{PACCAR.SMKTG.CAR.Model.Core}Order'):
			elementsDict["UnitTypeCd"] =(str(info.find('{PACCAR.SMKTG.CAR.Model.Core}UnitTypeCd').text))			
		for each in tree.findall('.//{PACCAR.SMKTG.CAR.Model.Core}Engine'):
			elementsDict["Engine"] =(str(each.find('.//{PACCAR.SMKTG.CAR.Model.Core}Manufacture').text) + " " + str(each.find('.//{PACCAR.SMKTG.CAR.Model.Core}Model').text))
			elementsDict["EngineBrand"] =(str(each.find('.//{PACCAR.SMKTG.CAR.Model.Core}Manufacture').text))
	elementsDict["PriceProtectionDt"] = re.sub(r'(\d+)/(\d+)/(\d+)', r'\2/\3/\1',elementsDict["PriceProtectionDt"])
	elementsDict["RequestedEndDate"] = re.sub(r'(\d+)/(\d+)/(\d+)', r'\2/\3/\1',elementsDict["RequestedEndDate"])
	print(elementsDict)
	# LOAD THE TABLES FROM PICKLE FILE SAVED PREVIOUSLY
	cache = cacheSFTables()
	tableDict = cache.getTablesFromCache()
	calculator = CARS_calculator(tableDict = tableDict)
	responseDict = calculator.CARS_calculator(inputDict = elementsDict)
	response = jsonify(responseDict)
	return response

### new json format 
@app.route('/jsonget_guideline', methods = ['POST'])
def json_example():
	req_data = request.get_json()
	elementsDict = {}
	elementsDict["DivisionCode"] = (str(req_data["DivisionCode"]))
	elementsDict["PriceProtectionDt"] = (str(req_data["PriceProtectionDt"])[0:10].replace("-","/"))
	elementsDict["RequestedEndDate"] = (str(req_data["RequestedEndDate"])[0:10].replace("-","/"))
	elementsDict["PriceProtectionDt"] = re.sub(r'(\d+)/(\d+)/(\d+)', r'\2/\3/\1',elementsDict["PriceProtectionDt"])
	elementsDict["RequestedEndDate"] = re.sub(r'(\d+)/(\d+)/(\d+)', r'\2/\3/\1',elementsDict["RequestedEndDate"])
	elementsDict["CCSalesOptionCd"] = (str(req_data["CCSalesOptionCd"]))
	elementsDict["MarketModel"] = (str(req_data["MarketModel"]))
	elementsDict["DealerList"] = (req_data["DealerList"])
	elementsDict["MinQuantity"] = (req_data["MinQuantity"])
	elementsDict["CustomerName"] = (str(req_data["CustomerName"]))
	elementsDict["Engine"] = ((str(req_data["Engine"]["Manufacture"])) + " " + (str(req_data["Engine"]["Model"])))
	elementsDict["EngineBrand"] = (str(req_data["Engine"]["Manufacture"]))
	elementsDict["RequestedCARPercent"] = (float(req_data["RequestedCARPercent"]))
	elementsDict["DealerNet"] = (float(req_data["DealerNet"]))
	elementsDict["DealerCd"] = (str(req_data["DealerCd"]))
	elementsDict["UnitTypeCd"] = (int(req_data["Order"]["UnitTypeCd"])) if req_data["Order"]["UnitTypeCd"] else 5
	# LOAD THE TABLES FROM PICKLE FILE SAVED PREVIOUSLY
	cache = cacheSFTables()
	tableDict = cache.getTablesFromCache()
	calculator = CARS_calculator(tableDict = tableDict)
	responseDict = calculator.CARS_calculator(inputDict = elementsDict)
	response = jsonify(responseDict)

	def default(o):
	    if isinstance(o, (datetime.date, datetime.datetime)):
	        return o.isoformat()
	rec_obj = {"timestamp": datetime.datetime.now(),
				"input":elementsDict, 
				"response":responseDict,
			}
	with open(reclog_filename,"a+") as rec_log:
		rec_log.write("{}\n".format(json.dumps(rec_obj, sort_keys=False, default=default)))
	rec_log.close()
	return response


if __name__ == '__main__':
	#app.run(host='0.0.0.0', port=5000)
	app.run(port=5000, debug=True)
