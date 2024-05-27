from flask import Blueprint, jsonify, request
from ..models import Category

categories_bp = Blueprint('categories', __name__)

# Временное хранилище данных
categories = [
    Category(1, 'Clothing'),
    Category(2, 'Accessories')
]

@categories_bp.route('/', methods=['GET'])
def get_categories():
    return jsonify([category.__dict__ for category in categories])

@categories_bp.route('/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = next((category for category in categories if category.id == category_id), None)
    if category:
        return jsonify(category.__dict__)
    else:
        return jsonify({'error': 'Category not found'}), 404

@categories_bp.route('/', methods=['POST'])
def create_category():
    data = request.json
    new_category = Category(id=data['id'], name=data['name'])
    categories.append(new_category)
    return jsonify(new_category.__dict__), 201
