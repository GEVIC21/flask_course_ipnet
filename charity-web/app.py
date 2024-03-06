from flask import Flask, jsonify
from flask_cors import CORS 
from charity import charity_bp
from flask import send_from_directory

# configuration
DEBUG = True

# instantiate the app
# app = Flask(__name__)
app = Flask(__name__, static_folder='static')
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/test', methods=['GET'])
def test():
    return jsonify("Hello, World! From flask API")

# @app.route('/projets', methods=['GET'])
# def get_projets():
#     from charity.data import projets
#     return jsonify(projets)

app.register_blueprint(charity_bp, url_prefix="/charity")

# @app.route('/static/<path:path>')
# def send_static(path):
#     return send_from_directory('static', path)

