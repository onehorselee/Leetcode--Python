from CARS_calculator import CARS_calculator
from cacheSFTables import cacheSFTables
import json
import re
import os
import pandas as pd


TestPath =  'tests/'   
class testCalculator:
    def __init__(self):
        if not os.path.exists(TestPath):
            os.makedirs(TestPath)
        self.cache = cacheSFTables()
        self.tableDict = self.cache.getTablesFromCache()
        self.calculator = CARS_calculator(tableDict = self.tableDict)


    def getJSON(self, jsonfilename):
        with open(jsonfilename) as json_file:
            req_data = json.load(json_file)
        elementsDict = {}
        elementsDict["DivisionCode"] = (str(req_data["DivisionCode"]))
        elementsDict["PriceProtectionDt"] = (str(req_data["PriceProtectionDt"])[0:10].replace("-","/"))
        elementsDict["PriceProtectionDt"] = re.sub(r'(\d+)/(\d+)/(\d+)', r'\2/\3/\1',elementsDict["PriceProtectionDt"])
        elementsDict["CCSalesOptionCd"] = (str(req_data["CCSalesOptionCd"]))
        elementsDict["MarketModel"] = (str(req_data["MarketModel"]))
        elementsDict["DealerList"] = (req_data["DealerList"])
        elementsDict["MinQuantity"] = (req_data["MinQuantity"])
        elementsDict["CustomerName"] = (str(req_data["CustomerName"]))
        elementsDict["Engine"] = ((str(req_data["Engine"]["Manufacture"])) + " " + (str(req_data["Engine"]["Model"])))
        elementsDict["EngineBrand"] = (str(req_data["Engine"]["Manufacture"]))
        #elementsDict["EngineModel"] = (req_data["Engine"]["Model"])	
        elementsDict["RequestedCARPercent"] = (float(req_data["RequestedCARPercent"]))
        elementsDict["DealerNet"] = (float(req_data["DealerNet"]))
        elementsDict["DealerCd"] = (str(req_data["DealerCd"]))
        elementsDict["UnitTypeCd"] = (int(req_data["Order"]["UnitTypeCd"])) if req_data["Order"]["UnitTypeCd"] else 5
        return elementsDict


    def testCalcualtor(self, elementsDict):
        responseDict = self.calculator.CARS_calculator(inputDict = elementsDict)
        return responseDict


    def translateJsonToDataframe(self, responseDict):
        df = pd.DataFrame.from_dict(responseDict, orient='index')
        return df


if __name__ == "__main__":
    division = "KW" if 1 else "PB"
    samples = [f for f in os.listdir('jCARs-{}'.format(division))]
    DataPath = 'jCARs-{}/'.format(division)  
    responseDict = {}
    FinalResultsDF = pd.DataFrame()
    for filename in samples:
        test = testCalculator()
        print(DataPath + filename)
        elementsDict = test.getJSON(DataPath + filename)
        response = test.testCalcualtor(elementsDict)
        response["CCSalesOptionCd"] = elementsDict["CCSalesOptionCd"]
        responseDict[filename] = response
        print("filename:{}".format(filename))
        print(responseDict)
        responseDF = test.translateJsonToDataframe(responseDict)
        FinalResultsDF.append(responseDF)        
    responseDF.to_csv("{}testResults_{}.csv".format(TestPath, division))

    

	