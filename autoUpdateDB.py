import json
import requests

def schedule_database_lookup():
    URL_Proxy = {
        # "http://cars.paccar-aacoe.com": {
	    #    "http":  "http://cars.paccar-aacoe.com",
	    #   "https": "https://cars.paccar-aacoe.com",
	    # },
        # "http://cars.dev.paccar.cloud": {
	    #    "http":  "http://cars.dev.paccar.cloud",
	    #    "https": "http://cars.dev.paccar.cloud",
	    # },
        "http://cars-api.paccar.cloud": {
	       "http":  "http://cars-api.paccar.cloud",
	       "https": "http://cars-api.paccar.cloud",   
	    },
    }


    for URL in URL_Proxy:
        URL_schedule = URL + "/schedule_database_lookup"
        proxies = URL_Proxy[URL]
        response = requests.get(URL_schedule,
                                proxies=proxies,
                                timeout=60)
        if response.ok:
            print("{} \nresponse ok: {}".format(URL_schedule, response.content))
        else:
            print("{} \nresponse not okay. status code: {}".format(URL_schedule, response.status_code))


if __name__ == "__main__":
	schedule_database_lookup()
