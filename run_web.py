from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify

#configuration

USERNAME = 'admin'
PASSWORD = 'pass'
SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():	
	return render_template('contact.html')

@app.route('/choose_color', methods=["POST"])
def choose_color():
	token = request.form.get('token','None', type=str)
	#session['player_color'] = token.upper()
	#print session['player_color']
	return jsonify(result=token)



@app.route('/game_board',methods=["GET"])
def game_board ():
	return render_template('game_board.html')

@app.route('/test_board',methods=["GET"])
def test_board ():
	return render_template('test_board.html')	


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
#            session['username'] = request.form['username']

            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('index.html', error=error)

@app.route('/logout')
def logout():

    session.pop('logged_in', None)
    #session.pop('username', None)
    #session.pop('player_color', None)
    #session.pop('modified', None)
    #session.pop('on_update', None)
    #session.clear()
    print "inside logout"
    flash('You were logged out')
    return redirect(url_for('index'))

@app.route('/game_board', methods=["POST"])
def tile_placement():
    x = request.form.get('x', 0, type=int)
    y = request.form.get('y', 0, type=int)
   # print session['username']
    return jsonify(result =(x,y))

@app.route('/test_board', methods=["POST"])
def test_tile_placement():
    x = request.form.get('x', 0, type=int)
    y = request.form.get('y', 0, type=int)
    print "test before"
    print session.__dict__
    print "test after"
    #print session['logged_in']
    return jsonify(result =(x,y))




if __name__ == '__main__':
#	app.run(host='0.0.0.0',debug=True)
    app.run(debug=True)