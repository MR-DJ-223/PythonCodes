from flask import Flask, render_template, request
from FlamesBackEnd import FlamesGame

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    player1 = None
    player2 = None
    if request.method == 'POST':
        player1 = request.form['player1']
        player2 = request.form['player2']
        game = FlamesGame()
        result = game.Flames(player1, player2)
    return render_template('index.html', result=result, player1=player1, player2=player2)

if __name__ == '__main__':
    app.run(debug=True)
