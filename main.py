from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
]

@app.route("/verify/<pin_code>")
def verify(pin_code):
    if pin_code == "763421":
        data = {
            "pin_code": pin_code,
            "username": "FLAG1"
        }
    else:
        data = {
            "pin_code": pin_code,
            "username": "Invalid pin code"
        }
    return jsonify(data), 200



@app.route("/authenticate", methods=["POST"])
def authenticate():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    for user in users:
        if user["username"] == username and user["password"] == password:
            response = {"success": True, "url": "./Flag2/1cffff3cec2d6f4bb694de90cb2d07a1de005d795c4b7d618adde864.html"}
            return jsonify(response)

    response = {"success": False}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)