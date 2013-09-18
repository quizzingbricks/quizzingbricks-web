from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('starter_template.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/game_board')
def game_board():
	return render_template('game_board.html')



if __name__ == '__main__':
    app.run(debug=True)