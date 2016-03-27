"""
   This is the Flask server.py
"""

from flask import Flask, render_template, request
from Server.db import DataGuy, DatabaseGuy

D = DataGuy()
DB = DatabaseGuy()

app = Flask(__name__)

# -------- INITIATE HTML-paths --------- #
@app.route("/")
def index():
    """
    Render homepage
    :return:
    """
    return render_template('index.html')

@app.route("/Level2")
def level2():
    return render_template('Level2.html')

@app.route("/Level3")
def level3():
    return render_template('Level3.html')

@app.route("/Level4")
def level4():
    return render_template('Level4.html')

@app.route("/last-input")
def data():
    """
    Render page with raw_data from game client
    """
    return render_template('data.html', game=cache.game, level=cache.level, score=cache.points, player=cache.user, timestamp=cache.time_stamp)


# ---------- INCOMMING DATA from game-client -------- # 
@app.route("/collect_data", methods=['POST'])
def collect_data():
    """
    Data collection from game client
    :return:
    """
    D.game = request.form.get("game")
    D.level = int(request.form.get("level"))
    D.points = int(request.form.get("points"))
    D.user = request.form.get("user")
    D.time_stamp = request.form.get("time_stamp")

    # Store data from game client
    DB.store_data(D)

    # Extract a list of scores
    scorelist = DB.list_highscore(D, DB)

    # Deliver list to game client
    return "Data received.\n" \
           "Scorelist from web server: %s" % scorelist


class CacheData:
    def __init__(self):
        self.game = ''
        self.level = 0
        self.points = 0
        self.user = ''
        self.time_stamp = ''


if __name__ == "__main__":
    cache = CacheData()
    app.run(debug=True)





""" 
    session 21:25  """