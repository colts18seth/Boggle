from boggle import Boggle
from flask import Flask, render_template

app = Flask(__name__)
boggle_game = Boggle()

@app.route('/')
def index():
    """return homepage"""

    return render_template("index.html", boggle_game=boggle_game) 