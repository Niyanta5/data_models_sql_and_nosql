from pymongo import MongoClient

def test_nosql_denormalization():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["ecommerce"]
    
    # Check if orders are embedded in user docs
    user = db.users.find_one({ "_id": "user_1" })
    assert len(user["orders"]) > 0, "No orders found in user document!"