from flask import Blueprint, jsonify, make_response, redirect, request, url_for
from flask_jwt_extended import unset_jwt_cookies

logout_ws = Blueprint("logoutWs", __name__, template_folder="templates")

# supprime les cookie de connexion
@logout_ws.post("/api/logout")
def logout():
    redirect_response = make_response(redirect(url_for("loginWs.login_page")))
    unset_jwt_cookies(redirect_response)
    return redirect_response
