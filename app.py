# Use Insomnia or Postman to send manually Http Request to your local application
from flask import Flask, request
from db import items, stores
import uuid
from flask_smorest import abort

app = Flask(__name__)


@app.get("/stores")
def get_all_stores():
    return {"stores": list(stores.values())}

@app.get("/items")
def get_all_items():
    return {"items": list(items.values())}

# Creates a store from a JSON request, this store has no item firstly. Example of JSON request:
# {
# "name": "My Store 1"
# }
@app.post("/store/create")
def create_store():
    request_data = request.get_json()
    
    if "name" not in request_data:
        abort(400, message="Bad request! Ensure 'name' is included in the JSON payload.")

    for store in stores.values():
        if request_data["name"] == store["name"]:
            abort(400, message="Store already exists.")
    
    store_id = uuid.uuid4().hex # Creating an unique id for the store
    new_store={**request_data, "id": store_id}
    stores[store_id] = new_store
    return new_store, 201


# Creates an item from a JSON request. Example of JSON request:
# {
# "name": "Table",
# "price": 29.99
# "store_id": "bcd96514328f44b088ab9523aa6a6849"
# }
@app.post("/item/create")
def create_item():
    request_data = request.get_json()
    
    if ("price" not in request_data
        or "store_id" not in request_data
        or "name" not in request_data):
        abort(400, message="Bad request! Ensure 'name', 'price', 'store_id' are included in the JSON payload.")
    
    if request_data["store_id"] not in stores:
        abort(404, message="Store not found!")
        
    for item in items.values():
        if (request_data["name"] == item["name"]) and (request_data["store_id"] == item["store_id"]):
            abort(400, message="Item already exists.")

        
    
    item_id = uuid.uuid4().hex # Creating an unique id for the store
    new_item={**request_data, "id": item_id}
    items[item_id] = new_item
    return new_item, 201

@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return {"store": stores[store_id]}
    except KeyError:
        abort(404, message="Store not found!")

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return {"item": items[item_id]}
    except KeyError:
        abort(404, message="Item not found!")

@app.delete("/item/delete/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted."}
    except KeyError:
        abort(404, message="Item not found!")
        
@app.put("/item/update/<string:item_id>")
def update_item(item_id):
    request_data = request.get_json()
    if "price" not in request_data or "name" not in request_data:
        abort(400, message="Bad request! Ensure 'name', 'price' are included in the JSON payload.")
    
    try:
        item = items[item_id]
        item |= request_data
        return item
    except KeyError:
        abort(404, message="Item not found!")
    
