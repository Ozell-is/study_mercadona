import json

from flask import Blueprint, render_template, request

from bdd.database import db
from models.Admin import Admin

admin_ws = Blueprint("adminWs", __name__, template_folder="templates")


@admin_ws.post("/createAdmin")
def create_admin():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        data: Admin = Admin.from_json(request.get_json())
        db.session.add(data)
        db.session.commit()
        return (
            jsonify({"message": "Administrateur créé avec succès"}),
            200,
        )  # Réponse avec un message JSON de succès
        return jsonify({"message": "Requête invalide"}), 400
