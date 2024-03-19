from flask import Blueprint, request, jsonify

routes_blueprint = Blueprint("user_routes", __name__)

@routes_blueprint.route("/transport/cheaper/to", methods=["GET"])
def find_cheaper_transport():
    pass

@routes_blueprint.route("/transport/confort/to", methods=["GET"])
def find_confort_transport():
    pass
