#!/usr/bin/env python
# coding: utf-8

"""
   This is the Flask server.py
"""

from flask import Flask, render_template, request
from db import DataGuy, StorageGuy

data = DataGuy()
storage = StorageGuy()

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
    data.game = request.form.get("game")
    data.level = int(request.form.get("level"))
    data.points = int(request.form.get("points"))
    data.user = request.form.get("user")
    data.time_stamp = request.form.get("time_stamp")

    # Store data from game client
    storage.store_data(data)

    # Extract a list of scores
    scorelist = storage.list_highscore(data, storage)

    # Deliver list to game client
    return "Data received.\n" \
           "Scorelist from web server: %s" % scorelist


if __name__ == "__main__":
    app.run(debug=True)





""" 
    session 21:25  """