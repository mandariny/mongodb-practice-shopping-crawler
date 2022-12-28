import os
import sys
import urllib.request
from dotenv import load_dotenv

load_dotenv()
client_id = os.environ.get('ClientID')
client_secret = os.environ.get('ClientSecret')

encText = urllib.parse.quote(string="clothes")
url = "https://openapi.naver.com/v1/search/shop.json?query=" + encText

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode == 200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code: " + rescode)
