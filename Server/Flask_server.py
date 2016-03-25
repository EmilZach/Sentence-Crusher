"""
   This is the Flask server.py
"""

from flask import Flask, render_template, request

app = Flask(__name__)


# -------- SEND HTML FILES TO BROWSER ---------
@app.route("/")
def index():
    """
    Render homepage
    :return:
    """
    return render_template('index.html')

@app.route("/data")
def data():
    """
    Render page with raw_data from game client
    """
    return render_template('data.html')


@app.route("/collect_data", methods=['POST'])
def collect_data():
    """
    Data collection from game client
    :return:
    """
    game = request.form.get("game")
    print(game)
    level = request.form.get("level")
    print(level)
    score = request.form.get("score")
    print(score)
    player = request.form.get("player")
    print(player)
    timestamp = request.form.get("timestamp")
    print(timestamp)
    return render_template("data.html", game=game, level=level, score=score, player=player, timestamp=timestamp)


if __name__ == "__main__":
    app.run(debug=True)




""" 
    session 21:25  """