from flask import Flask, jsonify, request

app = Flask(__name__)

# Stockage des utilisateurs en mémoire
users = {}

# Endpoint racine
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Endpoint pour vérifier le status
@app.route("/status")
def status():
    return "OK"

# Endpoint pour récupérer tous les utilisateurs
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

# Endpoint pour récupérer un utilisateur spécifique
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Endpoint pour ajouter un nouvel utilisateur
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    # Retourner seulement l'objet utilisateur
    return jsonify(data), 201

# Lancer le serveur Flask
if __name__ == "__main__":
    app.run(debug=True)
