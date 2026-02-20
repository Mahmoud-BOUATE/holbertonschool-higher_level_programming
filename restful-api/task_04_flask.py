#!/usr/bin/env python3
"""
Simple Flask API
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route("/")
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Status endpoint"""
    return "OK"


@app.route("/data")
def get_usernames():
    """Return list of all usernames"""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Return full user object by username"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user via POST"""
    try:
        data = request.get_json()
        if data is None:
            raise ValueError
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store full user object
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
