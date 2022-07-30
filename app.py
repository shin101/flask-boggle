from boggle import Boggle
from flask import Flask, redirect, render_template, session, jsonify, request

boggle_game = Boggle()
app = Flask(__name__)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config["SECRET_KEY"] = "SECRET"

# current_score = 0

@app.route('/')
def homepage():
    board = boggle_game.make_board()
    session['board'] = board
    nplays = session.get("nplays", 0)

    return render_template("/homepage.html", board = board, nplays=nplays) 
    #  current_score = current_score)

@app.route('/check-word')
def check_word():
    word = request.args["word"]
    board = session['board'] 
    result  = boggle_game.check_valid_word(board,word)
    return jsonify({"result": result})

@app.route('/nplays', methods=['POST'])
def number_played():
    nplays = session.get("nplays",0)
    session['nplays'] = nplays+1
    return jsonify(nplays=nplays)