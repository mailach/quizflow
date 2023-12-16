
from flask import Blueprint
from ..ksql import query_ksql

admin = Blueprint('admin', __name__)


@admin.route("/admin/questions")
def questions():
    return query_ksql("Select * from QUESTIONS_TABLE;")
