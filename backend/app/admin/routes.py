
from flask import Blueprint
from ..ksql import query_ksql

admin = Blueprint('admin', __name__)

