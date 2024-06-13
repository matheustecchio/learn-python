import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found.")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found.")

# {
# 	"name":"U-Table",
# 	"price": 45.99
# }
    @blp.arguments(ItemUpdateSchema)
    def put(self, request_data, item_id):
        try:
            item = items[item_id]
            item |= request_data

            return item
        except KeyError:
            abort(404, message="Item not found.")


@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items": list(items.values())}


# Creates an item from a JSON request. Example of JSON request:
# {
# "name": "Table",
# "price": 29.99
# "store_id": "bcd96514328f44b088ab9523aa6a6849"
# }
    @blp.arguments(ItemSchema)
    def post(self, request_data):        
        for item in items.values():
            if (
                request_data["name"] == item["name"]
                and request_data["store_id"] == item["store_id"]
            ):
                abort(400, message=f"Item already exists.")

        item_id = uuid.uuid4().hex
        item = {**request_data, "id": item_id}
        items[item_id] = item

        return item
