import requests
import json

carparkid = input("Enter carpark ID: ")

url = 'https://api.data.gov.sg/v1/transport/carpark-availability'
response = requests.get(url)
response_dict = json.loads(response.text)

for i in response_dict["items"] :
    for j in i["carpark_data"] :
        if j["carpark_number"] == carparkid:
            print("Last updated on: " + j["update_datetime"])
            for k in j["carpark_info"]:
                print("Total lots: " +k["total_lots"])
                print("Lots available: " +k["lots_available"])
