import requests
import urllib.parse
from dotenv import load_dotenv
import os

url = 'https://api.clashofclans.com/v1/'

load_dotenv()
header = {"Authorization" : "Bearer {}".format(os.environ.get('API_TOKEN'))}

Tag = input("Enter tag number: ")
playerTag = urllib.parse.quote_plus(Tag) #parse for url encode

finalurl = url + f"players/{playerTag}"
response = requests.get(finalurl, headers=header)
print(response.text) #prints json as a python dictionary