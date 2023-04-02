from flask import Blueprint, request

#from pdfextractor.controllers.api_controller import ApiController

bp = Blueprint("router", __name__, template_folder="templates")


@bp.route("/", methods=["GET", "POST"])
def hello_world():
    return "<p>Hello, World!</p>"
    
@bp.route("/documents", methods=["GET", "POST"])
def index():
    """Index of the API.
    GET method returns an HTML upload form.
    POST method can be used to upload a PDF file.
        See README.md for response format.
    Returns:
        flask.Response: standard flask HTTP response.
    """
    return ApiController.index(request)

