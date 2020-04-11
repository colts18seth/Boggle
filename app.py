from boggle import Boggle
from flask import Flask, render_template, session, request, redirect, flash, jsonify
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

    if "times_played" in session:
        played = session["times_played"]
    else:
        played = 0
        session["times_played"] = played

    if "high_score" in session:
        score = session["high_score"]
    else:
        score = 0
        session["high_score"] = score
  
    return render_template("index.html", board=board, played=played, score=score) 

@app.route('/guess', methods=["POST"])
def guess():
    """ handle guess """    
    raw = request.get_json()
    guess = raw["guess"]
    board = session["board"]    
    check_word = boggle_game.check_valid_word(board, guess)
    
    return check_word

@app.route('/save', methods=["POST"])
def save():
    """ save highscore and times played """
    raw = request.get_json()
    played = raw["played"]
    session['times_played'] = played   
    score = raw["score"]
    high_score = session["high_score"]

    if int(score) > int(high_score):
        high_score = score
        session["high_score"] = high_score
         
    return jsonify(high_score)