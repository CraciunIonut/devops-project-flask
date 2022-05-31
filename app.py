from flask import Flask, jsonify, render_template
from flask_restful import Api

from getMethod import blueprintGet
from postMethod import blueprintPost
from createdatabase import createdb

app = Flask(__name__)
api = Api(app)

api_rest_host = "0.0.0.0"
api_rest_port = 5001

createdb()

app.register_blueprint(blueprintGet, url_prefix='/GET')
app.register_blueprint(blueprintPost, url_prefix='/POST')


app.run(host=api_rest_host, port=api_rest_port, debug=True)