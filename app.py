import secrets

from flask import Flask, render_template, request, redirect, session
from db import Database

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
dbo = Database()

@app.route('/')
def index():  # put application's code here
    if session.get('logged_in'):
        return redirect("/profile")
    else:
        return render_template('index.html')

@app.route('/register')
def register():  # put application's code here
    if session.get('logged_in'):
        return redirect("/profile")
    else:
        return render_template('register.html')

@app.route('/perform_registration', methods=['POST'])
def perform_registration():  # put application's code here
    if session.get('logged_in'):
        return redirect("/profile")
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        response = dbo.register_user(name, email, password)

        if response:
            return render_template('index.html', message="Registration successful", color="green")
        else:
            return render_template('index.html', message="Registration failed", color="red")

@app.route('/perform_login', methods=['POST'])
def perform_login():  # put application's code here
    if session.get('logged_in'):
        return redirect("/profile")
    else:
        email = request.form.get('email')
        password = request.form.get('password')

        response = dbo.login_user(email, password)

        if response:
            session['logged_in'] = True
            session['email'] = email
            session['user'] = dbo.get_user(email)

            return redirect("/profile")
        else:
            return render_template("index.html", message="Login failed", color="red")

@app.route('/profile')
def profile():  # put application's code here
    if session.get('logged_in'):
        return render_template("profile.html", user=session['user'], email=session['email'])
    else:
        return redirect("/")

@app.route('/logout')
def logout():  # put application's code here
    session.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
