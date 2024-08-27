from flask import Blueprint

helloworld_bp = Blueprint("helloworld", __name__)

@helloworld_bp.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>", 200