from flask import Blueprint, request, jsonify, redirect,url_for, make_response
from flask_jwt_extended import unset_jwt_cookies


logout_ws = Blueprint("logoutWs", __name__, template_folder="templates")

@logout_ws.post('/api/logout')
def logout():
    print("Début de la fonction logout")

    redirect_response = make_response(redirect(url_for('loginWs.login_page')))
    unset_jwt_cookies(redirect_response)
    print("Cookies supprimés")
    return redirect_response