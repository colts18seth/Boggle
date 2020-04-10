from boggle import Boggle
from flask import Flask, render_template, session, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET"
debug = DebugToolbarExtension(app)
boggle_game = Boggle()

@app.route('/')
def index():
    """make new board"""
    board = boggle_game.make_board()
    session["board"] = board
    return render_template("index.html", board=board) 

@app.route('/home')
def home():
    """ play board """
    board = session["board"]
    return render_template("index.html", board=board)

@app.route('/guess', methods=["POST"])
def guess():
    """ handle guess """    
    raw = request.get_json()
    guess = raw["guess"]
    board = session["board"]    
    check_word = boggle_game.check_valid_word(board, guess)
    
    return check_word

@app.route('/save', methods=['POST'])
def save():
    """ save highscore and times played """
    