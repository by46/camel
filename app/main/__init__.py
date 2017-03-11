from flask import Blueprint
from flask_restful import Api

url_prefix = '/camel'
main = Blueprint('main', __name__, url_prefix=url_prefix)

api = Api(main)

from . import views