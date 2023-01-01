from fastapi import FastAPI
import datetime
import crawler
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pprint

app = FastAPI()
load_dotenv()

db_addrs = os.environ.get('DB_ADDRS')
db_port = int(os.environ.get('DB_PORT'))
db_name = os.environ.get('DB_NAME')
collection_name = os.environ.get('COLLECTION_NAME')
client = MongoClient()
client = MongoClient(db_addrs, db_port)
db = client[db_name]
collection = db[collection_name]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/create/")
def create_data(query):
    search_data = crawler.search(query)
    dt_now = datetime.datetime.now()

    items = search_data['items']
    for item in items:
        insert_data = {
                "date": dt_now,
                "title": item['title'],
                "link": item['link'],
                "image": item['image'],
                "lprice": item['lprice'],
                "hprice": item['hprice'],
                "mallName": item['mallName'],
                "productId": item['productId'],
                "productType": item['productType'],
                "brand": item['brand'],
                "maker": item['maker'],
                "category1": item['category1'],
                "category2": item['category2'],
                "category3": item['category3'],
                "category4": item['category4']
        }
        collection.insert_one(insert_data)        

    return "success"

@app.get("/read/")
def read_data(key, value):
    return collection.find_one({key:value}, {'_id': 0})
