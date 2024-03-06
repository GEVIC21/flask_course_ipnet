from flask import render_template, Blueprint, jsonify
from charity.data import  projets


charity_bp = Blueprint("charity", __name__, template_folder="templates", static_folder="static")



# def index():
#     return render_template("index.html", projets =projets)
@charity_bp.route("/")
def index():
    return render_template("index.html", projets =projets)

@charity_bp.route("/api/list")
def api_list():
    return jsonify(projets)


# @app.route('/projets', methods=['GET'])
@charity_bp.route("/projets")
def get_projets():
    return jsonify(projets)