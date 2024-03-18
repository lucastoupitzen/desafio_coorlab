from flask import Blueprint, request, jsonify

routes_blueprint = Blueprint("user_routes", __name__)

@routes_blueprint.route("/transport/to", methods=["GET"])
def find_transports_to_destination():
    pass
