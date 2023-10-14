import json

from flask import Blueprint, render_template, request

from bdd.database import db
from models.Admin import Admin

admin_ws = Blueprint("adminWs", __name__, template_folder="templates")


@admin_ws.post("/admin/login")
def login_admin():
    return "hello admin"
