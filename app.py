from flask import Flask, render_template
import random

app = Flask(__name__)

COULEURS = {
    "rouge": "#FF0000",
    "vert": "#00FF00",
    "bleu": "#0000FF"
}

@app.route("/")
def index():
    couleur_nom, couleur_hex = random.choice(list(COULEURS.items()))
    return render_template("index.html", couleur=couleur_hex, nom=couleur_nom)

if __name__ == "__main__":
    app.run(debug=True)

