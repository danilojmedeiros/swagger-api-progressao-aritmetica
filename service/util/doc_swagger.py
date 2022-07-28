from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
    'a1': fields.List(fields.Integer(), required=True), 
    'q': fields.List(fields.Integer(), required=True),
    'n': fields.List(fields.Integer(), required=True)})