from flask import request, jsonify, Blueprint

blueprintGet = Blueprint('getMethod', __name__)

@blueprintGet.route('/', methods=['GET'])
def query_record():
    return "Hello World!"