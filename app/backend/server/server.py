from flask import Flask
from flask_cors import CORS
from .routes.routes import routes_blueprint

app = Flask(__name__)

app.register_blueprint(routes_blueprint)

CORS(app, origins='http://localhost:8080', allow_headers=['Content-Type'], methods=['GET', 'POST'])
