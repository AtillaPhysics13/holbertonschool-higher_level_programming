from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
auth = HTTPBasicAuth()

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "secret-key"

jwt = JWTManager(app)



users = {
    "user1": {"password": generate_password_hash("password"), "role": "user"},
    "admin1": {"password": generate_password_hash("password"), "role": "admin"}
}
  
@jwt.unauthorized_loader
def unauthorized(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired(jwt_header, jwt_payload):
    return jsonify({"error": "Token expired"}), 401


 
@app.route("/basic-protected")
@auth.login_required
def basic():

    return "Basic Auth: Access Granted"


@auth.verify_password
def verify(username,password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username


@app.route("/login",methods=["POST"])
def login():
    data=request.json
    username = data["username"]
    password = data["password"]
    
    if username in users and check_password_hash(users[username]["password"], password):
        token=create_access_token(identity=username)
        return jsonify(access_token=token)
    return  jsonify({"error": "wrong credentials"}), 401




@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"



@app.route("/admin-only")
@jwt_required()
def admin_only():

    username = get_jwt_identity()

    if users[username]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__=="__main__":
    app.run(debug=True)
