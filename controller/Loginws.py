import json

from flask import (Blueprint, jsonify, make_response, redirect,
                   render_template, request, url_for)
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                get_jwt_identity, jwt_required,
                                set_access_cookies, set_refresh_cookies,
                                verify_jwt_in_request)

from models.Admin import Admin
from utils.PasswordUtils import check_password

login_ws = Blueprint("loginWs", __name__, template_folder="templates")


@login_ws.get("/api/redirection")
def redirection():
    verify_jwt_in_request(optional=True)
    current_user = get_jwt_identity()
    if current_user:
        return redirect(url_for("productWs.get_admin_page"))
    else:
        return redirect(url_for("loginWs.login_page"))


@login_ws.get("/api/login")
def login_page():
    return render_template("login.html")


@login_ws.post("/api/login")
def authenticator():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return redirect(url_for("loginWs.login_page"))

    admin = Admin.query.filter_by(_username=username).first()

    if not admin:
        return redirect(url_for("loginWs.login_page"))
    hashed_password = admin.password

    if admin:
        if check_password(hashed_password, password):
            access_token = create_access_token(identity=username)
            # refresh le token le temps que l'user est actif
            refresh_token = create_refresh_token(identity=username)

            redirect_response = make_response(
                redirect(url_for("productWs.get_admin_page"))
            )
            set_access_cookies(redirect_response, access_token)
            set_refresh_cookies(redirect_response, refresh_token)

            return redirect_response
        else:
            return redirect(url_for("loginWs.login_page"))
    else:
        return redirect(url_for("loginWs.login_page"))
