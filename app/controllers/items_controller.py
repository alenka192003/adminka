from flask import Blueprint, jsonify, request
from ..models import Item

items_bp = Blueprint('items', __name__)

items = [
    Item(1, 'Dress', 'A stylish red dress'),
    Item(2, 'Jeans', 'Blue denim jeans')
]

@items_bp.route('/', methods=['GET'])
def get_items():
    return jsonify([item.__dict__ for item in items])

@items_bp.route('/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item.id == item_id), None)
    if item:
        return jsonify(item.__dict__)
    else:
        return jsonify({'error': 'Item not found'}), 404

@items_bp.route('/', methods=['POST'])
def create_item():
    data = request.json
    new_item = Item(id=data['id'], name=data['name'], description=data['description'])
    items.append(new_item)
    return jsonify(new_item.__dict__), 201
