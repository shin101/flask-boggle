from boggle import Boggle
from flask import Flask, redirect, render_template, session, jsonify, request

boggle_game = Boggle()
app = Flask(__name__)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config["SECRET_KEY"] = "SECRET"

@app.route('/')
def homepage():
    board = boggle_game.make_board()
    session['board'] = board

    return render_template("/homepage.html", board = board)

@app.route('/check-word')
def check_word():
    word = request.args["word"]
    board = session['board'] 
    return jsonify({"result": boggle_game.check_valid_word(board,word)})
