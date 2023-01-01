import os
import sys
import urllib.request
import json
from dotenv import load_dotenv

load_dotenv()
client_id = os.environ.get('ClientID')
client_secret = os.environ.get('ClientSecret')

def search(name):
    encText = urllib.parse.quote(string=name)
    url = "https://openapi.naver.com/v1/search/shop.json?query=" + encText

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode == 200):
        response_body = response.read()
        #return response_body.decode('utf-8')
        return json.loads(response_body)
    else:
        return rescode
