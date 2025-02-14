from flask import Flask, request


app = Flask(__name__)


stores = [
    {
        "name": "Dan Murphy's", 
        "items": [
            {
                "name": "Bunderburg Rum",
                "price": 44.99
            }
        ]
    }
]

# Gets data from all Stores
@app.get("/store")
def get_stores():
    return {"stores": stores}


# Creates a New Store
@app.post("/store")
def create_store():
    request_data = request.get_json()   
    # request: 
    #   global variable provided by flask (request import needed)
    #   request_data is a dictionary with the data received from the request
    #   or from the request body in insomia
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


#  Create new Item in existing Store
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item
    return {"message": "Store not found"}, 404


# Get a particular Store and its Items
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404



# Get a particular Item in a Store
@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404