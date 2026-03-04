### put and Delete-HTTP verbs
### Working with API's---json
from adodbapi.ado_consts import adChar

from flask import Flask, request, jsonify

app = Flask(__name__)

# initial data in my to do list
items= [
    {'id':1,"name":"item 1","description": "This is item 1"},
    {'id': 3, "name": "item 1", "description": "This is item 2"}

]
@app.route('/')
def home():
    return "welcome to the sample to do list app"

# get: retrieve all items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

# get:retrieve a specific item by id

@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item['id'] == item_id),None)
    if item is None:
        return jsonify({'error': 'item not found'})
    return jsonify(item)

# post:create a new task

@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'error': 'no name provided'})
    new_item={
        "id":items[-1]["id"] +1 if items else 1,
        "name":request.json['name'],
        "description":request.json['description'],

    }
    items.append(new_item)
    return jsonify(new_item)
# put: update and existing item

@app.route('/items/<int:id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item['id'] == item_id),None)
    if item is None:
        return jsonify({'error': 'item not found'})
    item['name'] = request.json.get('name',item['name'])
    item['description'] = request.json.get('description',item['description'])
    return jsonify(item)

@app.route('/items/<int:id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    item=next((item for item in items if item['id'] == item_id),None)
    return jsonify({"result":"item deleted"})

if __name__ == "__main__":
    app.run(debug=True)