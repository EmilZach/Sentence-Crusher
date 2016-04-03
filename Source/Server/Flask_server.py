#!/usr/bin/env python
# coding: utf-8

"""
   This is the Flask server.py
"""

from flask import Flask, render_template, request
from s_data import DataGuy
from s_storage import StorageGuy


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

@app.route("/level_history", methods=['POST'])

    level = request.form.get("level")
    data.level_history = read_from_file(level)
    return data.level_history

@app.route("/collect_data", methods=['POST'])
def collect_data():
    """ Collecting incomming data in the data-class,
    so it can be stored in a file.
    :return:
    """
    data.new_data = request.form.get("new_data")
    print(data.new_data)

    # Deliver list to game client
    return_this = "Data received. Scorelist from web server: %s" % data.sorted_highscorelist
    return return_this


if __name__ == "__main__":
    data = DataGuy()
    storage = StorageGuy()
    app.run(debug=True)





""" 
    session 21:25  """