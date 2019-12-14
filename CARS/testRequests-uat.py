import requests
import json

# http://10.248.59.90:5000/get_guideline


global proxies 

proxies = {
		 "http": "http://cars.paccar-aacoe.com",
		 "https": "https://cars.paccar-aacoe.com",
		}


def test_get_guideline():
	URL_1 = "http://cars.paccar-aacoe.com/get_guideline"
	for id in ["1"]:
            ifile = open("data/EventXMLText{}.xml".format(id), "r")
            xml_input = ifile.read()
            #print(xml_input)
            headers = {'Content-type': 'application/xml'}
            response  = requests.post(url=URL_1,data=xml_input,headers=headers)
            print('ID: {}'.format(id))
            if response.ok:
                print(response.json())
            else:
                print("response not okay. status code: {}".format(response.status_code))



def test_jsonget_guideline():
	URL_2 = "http://cars.paccar-aacoe.com/jsonget_guideline"
	ifile =  open('data/JSON_CAR_SubmitError.json', 'r')
	json_input = ifile.read()	
	request_json = json.loads(json_input)
	#print(request_json)
	headers = {'Content-type': 'application/json',}
	response = requests.request("POST", url=URL_2, 
										json=request_json,
										headers=headers,
										proxies=proxies,
								)							
	if response.ok:
		print("response ok")
	else:
		print("response not okay. status code: {}".format(response.status_code))


def transfer_log():
	URL_3 = "http://cars.paccar-aacoe.com/transfer_log"
	response = requests.get(URL_3, proxies=proxies)
	if response.ok:
		print("response ok: {}".format(response.content))
	else:
		print("response not okay. status code: {}".format(response.status_code))
if __name__ == "__main__":
    #test_get_guideline()
    for i in range(100):
        test_jsonget_guideline()
    transfer_log()

