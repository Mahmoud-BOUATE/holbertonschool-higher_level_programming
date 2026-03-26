import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    # Lire le fichier JSON
    with open('items.json', 'r') as f:
        data = json.load(f)

    # Récupérer la liste
    items_list = data.get("items", [])

    # Envoyer au template
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)