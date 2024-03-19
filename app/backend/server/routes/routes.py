from flask import Blueprint, request, jsonify

#import adapters
from ..adapters.request_adapter import request_adapter

#import composers
from ...composers.find_cheaper_composer import find_cheaper_composer
from ...composers.find_confort_composer import find_confort_composer

routes_blueprint = Blueprint("user_routes", __name__)

@routes_blueprint.route("/transport/cheaper", methods=["GET"])
def find_cheaper_transport():
    
    http_response = request_adapter(request, find_cheaper_composer())
    return jsonify(http_response.body), http_response.status_code

@routes_blueprint.route("/transport/confort", methods=["GET"])
def find_confort_transport():
    
    http_response = request_adapter(request, find_confort_composer())
    return jsonify(http_response.body), http_response.status_code
