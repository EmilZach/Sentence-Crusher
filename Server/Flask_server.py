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

@app.route("/last-input")
def data():
    """
    Render page with raw_data from game client
    """
    return render_template('data.html', game=cache.game, level=cache.level, score=cache.score, player=cache.player, timestamp=cache.timestamp)


@app.route("/collect_data", methods=['POST'])
def collect_data():
    """
    Data collection from game client
    :return:
    """
    cache.game = request.form.get("game")
    cache.level = request.form.get("level")
    cache.score = request.form.get("score")
    cache.player = request.form.get("player")
    cache.timestamp = request.form.get("timestamp")
    
    return "<h1> Recieved the data </h1>" 


class CacheData:
    def __init__(self):
        self.game = ''
        self.level = 0
        self.score = 0
        self.player = ''
        self.timestamp = ''


if __name__ == "__main__":
    cache = CacheData()
    app.run(debug=True)





""" 
    session 21:25  """