# sample_bus_arrival.py

import requests
from dotenv import load_dotenv
import os
import json
from datetime import datetime, timedelta
import time

time_sleep = 5
print("Starting monitoring. Press CTRL + C to terminate")
load_dotenv()

try:
    while True:
        # BS_CODE = int(input("Enter bus stop code: "))
        BS_CODE = 84031
        BUS_SERVICE_NO = 67

        
        url = 'http://datamall2.mytransport.sg/'
        url_path_bus_arrival = 'ltaodataservice/BusArrivalv2?'

        url_path_params = {"BusStopCode": BS_CODE}

        header = {"AccountKey" : "{}".format(os.environ.get('API_KEY')), 'accept' : 'application/json'}
        
        response = requests.get(url + url_path_bus_arrival + "BusStopCode=" + str(url_path_params['BusStopCode']), headers=header)
        response_dict = json.loads(response.text)

        for bus_service in response_dict["Services"] :
            if bus_service["ServiceNo"] == str(BUS_SERVICE_NO) :
                # print(bus_service)
                for k, v in bus_service["NextBus"].items() :
                    if k == "EstimatedArrival" :
                        next_bus_timing = v
                        # print(next_bus_timing)

        clean = str(next_bus_timing).split("+")
        next_bus_timing_clean = clean[0]
        next_bus_timing_clean_time = datetime.strptime(next_bus_timing_clean, "%Y-%m-%dT%H:%M:%S")

        now = datetime.now()
        now_str = now.strftime("%Y-%m-%dT%H:%M:%S")
        now_str_time = datetime.strptime(now_str, "%Y-%m-%dT%H:%M:%S")
        # print(now_str)

        diff = next_bus_timing_clean_time - now_str_time
        # print(diff)

        diff_time = str(diff).split(":")
        minutes = diff_time[1]

        if int(minutes) < 1 :
            print("Bus", BUS_SERVICE_NO, "is arriving soon.")
        else :
            print("Bus", BUS_SERVICE_NO, "is arriving in", minutes, "min(s).")
        time.sleep(time_sleep)
    
except KeyboardInterrupt :
    print("\nMonitoring terminated by user")