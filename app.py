# Use Insomnia or Postman to send manually Http Request to your local application


from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/stores")
def get_all_stores():
    return {"stores": stores}


# Creates a store from a JSON request, this store has no item firstly. Example of JSON request:
# {
# "name": "My Store 2"
# }
@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store={"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


# Creates an item from a JSON request. Example of JSON request:
# {
# "name": "Table",
# "price": 29.99
# }
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found!"}, 404

@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return {"store": store}
    return {"message": "Store not found!"}, 404

@app.get("/store/<string:name>/items")
def get_items(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found!"}, 404
