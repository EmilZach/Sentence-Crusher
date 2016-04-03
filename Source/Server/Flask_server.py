#!/usr/bin/env python
# coding: utf-8

"""
   This is the Flask server.py
"""

from flask import Flask, render_template, request
from serverdata import DataGuy
from storage import StorageGuy


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

@app.route("/lastdata")
def data():
    """
    Render page with raw_data from game client
    """
    return render_template('data.html', user=data.user, points=data.points, 
                             timestamp=data.time_stamp, clockdiff=data.clock_diff, 
                                      level=data.level, game=data.game)


# ---------- INCOMMING DATA from game-client -------- # 

@app.route("/check-link", methods=['POST'])
def check_link():
    return "SERVER ONLINE!"


@app.route("/store-data", methods=['POST'])
def collect_data():
    """ Collecting incomming data in the data-class,
    so it can be stored in a file.
    :return:
    """
    new_data = [request.form.get("points"),
                request.form.get("username"),
                request.form.get("timestamp"),
                request.form.get("clockdiff"),
                request.form.get("level"),
                request.form.get("game")]

    data = DataGuy(new_data)
    storage = StorageGuy()

    storage.store_data(data)


    return "DATA STORED ON THE SERVER!."


if __name__ == "__main__":
    app.run(debug=True)





""" 
    session 21:25  """