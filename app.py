from boggle import Boggle
from flask import Flask, render_template

app = Flask(__name__)
boggle_game = Boggle()

@app.route('/')
def index():
    """return homepage"""
    board = boggle_game.make_board()
    return render_template("index.html", board=board) 