import requests

url = 'https://api.pushover.net/1/messages.json'
token_key = 'insert_tokey_key_here'
user_key = 'insert_user_key_here'

message = 'inesert_message_here'
body = { 'token':token_key, 'user':user_key, 'title':'insert_title_here', 'message':message }

x = requests.post(url, json = body)
print(x.status_code)