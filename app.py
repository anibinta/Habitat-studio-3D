from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route de la page d'accueil (Landing Page)
@app.route('/')
def index():
    return render_template('landing.html')

# Route de l'application 3D (le Studio)
@app.route('/studio')
def studio():
    return render_template('index.html')

# (Conservez ici votre route API d'évaluation existante /api/evaluate-habitat)

if __name__ == '__main__':
    app.run(debug=True)

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)