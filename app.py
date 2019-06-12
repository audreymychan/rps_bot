import numpy as np
from flask import Flask, request, render_template

from markov_chain_bot import MarkovChainBot
from utils import emoji_to_text, evaluate

app = Flask(__name__)
bot = MarkovChainBot()
results = []
game = {}
print_results = False
game_round = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global bot
    global results
    global game
    global print_results
    global game_round

    if request.method == 'GET':
        bot = MarkovChainBot()
        results = []
        game = {}
        print_results = False
        game_round = 0
        return render_template('index.html')

    if request.form['submit'] == '👊' or request.form['submit'] == '✋' or request.form['submit'] == '✌️':
        game_round += 1
        player_throw = emoji_to_text(request.form['submit'])
        bot_throw = bot.throw(player_throw)
        result = evaluate(player_throw, bot_throw)
        results.append(result)
        game['result'] = result
        game['player'] = player_throw
        game['bot'] = bot_throw
        return render_template('index.html', game=game, game_round=game_round, print_results=print_results, results=results)

    if request.form['submit'] == 'show results':
        print_results = not print_results
        return render_template('index.html', game=game, game_round=game_round, print_results=print_results, results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
