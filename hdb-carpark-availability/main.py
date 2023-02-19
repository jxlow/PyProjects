import requests
import json

carparkid = input("Enter carpark ID: ")
if len(carparkid) < 1 :
    carparkid = "B10M"

url = 'https://api.data.gov.sg/v1/transport/carpark-availability'
response = requests.get(url)
response_dict = json.loads(response.text)

for i in response_dict["items"] :
    for j in i["carpark_data"] :
        if j["carpark_number"] == carparkid:
            updatedTime = j["update_datetime"]
            print("Last updated on: " + updatedTime)
            for k in j["carpark_info"]:
                totallots = int(k["total_lots"])
                lotsAvailable = int(k["lots_available"])
                print("Total lots: ", totallots)
                print("Lots Available: ", lotsAvailable)

lotsUnavailable = totallots - lotsAvailable
print("Lots Unavailable: ", lotsUnavailable)