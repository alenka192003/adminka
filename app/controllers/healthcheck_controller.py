from flask import Blueprint, jsonify

healthcheck_bp = Blueprint('healthcheck', __name__)

@healthcheck_bp.route('/', methods=['GET'])
def healthcheck():
    return jsonify({'status': 'ok'})
