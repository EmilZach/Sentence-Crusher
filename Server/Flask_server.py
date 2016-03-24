"""
   This is the Flask server.py
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    """
    Render homepage
    :return:
    """
    return render_template('index.html')


@app.route("/collect_data", methods=['POST'])
def collect_data():
    """
    Data collection from game client
    :return:
    """
    game = request.form.get("game")
    level = request.form.get("level")
    score = request.form.get("score")
    player = request.form.get("player")
    timestamp = request.form.get("timestamp")
    return render_template("data.html", game=game, level=level, score=score, player=player, timestamp=timestamp)


if __name__ == "__main__":
    app.run(debug=True)
