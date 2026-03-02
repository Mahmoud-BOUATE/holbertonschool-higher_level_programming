from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/user", methods=["POST"])
def user():
    username = request.form.get("username")
    # On renvoie une réponse JSON
    return jsonify({
        "message": f"Utilisateur {username} reçu !",
        "success": True
    })

if __name__ == "__main__":
    app.run(debug=True)