#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password", method="pbkdf2:sha256"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password", method="pbkdf2:sha256"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
        check_password_hash(users[username]["password"], password):
        return username

@app.route('/basic-protected')
@auth.login_required
def index():
    return f"Basic Auth: Access Granted"

from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_jwt_extended import JWTManager, get_jwt_identity

app.config["JWT_SECRET_KEY"] = "une_cle_secrete"
jwt = JWTManager(app)

@app.route("/login", methods=["POST"])
def create_token():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and \
        check_password_hash(users[username]["password"], password):
        access_token = create_access_token\
        (identity={"username": username, "role": users[username]["role"]})
        return jsonify(access_token=access_token)
    else:
        return jsonify({"error": "Bad username or password"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify(message="JWT Auth: Access Granted", user=current_user)

@app.route("/admin-only")
@jwt_required()
def get_user():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

if __name__ == "__main__":
    app.run(debug=True)
