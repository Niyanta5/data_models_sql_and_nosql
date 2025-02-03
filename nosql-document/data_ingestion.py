from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]

with open("mongo-scripts/sample_data.json") as f:
    data = json.load(f)

db.users.insert_many(data)