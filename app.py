from flask import Flask, session, render_template, request, redirect, g, url_for
from fetch_password import *
from input_to_database import *
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if(request.method == 'POST'):
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if(to_database(username, email, password)==-1):
            return render_template('warning.html')

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        session.pop('user', None)
        password = come_passwd(request.form['username'])
        if(password == -1):
            return redirect(url_for('signup'))
        if request.form['password'] == password:
            session['user'] = request.form['username']
            return redirect(url_for('protected'))
    return render_template('login.html')


@app.route('/protected')
def protected():
    if g.user:
        return render_template('protected.html', user=session['user'])
    return redirect(url_for('login'))

@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
