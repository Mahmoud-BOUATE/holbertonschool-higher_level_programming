#!/usr/bin/env python3

"""
Docstring for restful-api.task_04_flask
"""

from flask import Flask, jsonify
from flask import request


app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():

    liste_clés = list(users.keys())

    return jsonify(liste_clés)
@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def user(username):
    if username in users:
        return jsonify(users[username])

    else:
        return {"error": "User not found"}, 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    new_user = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }

    users[username] = new_user

    # Retourner uniquement le dictionnaire utilisateur
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run()

