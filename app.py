from flask import Flask, render_template, request
from db import Database

app = Flask(__name__)

dbo = Database()

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/register')
def register():  # put application's code here
    return render_template('register.html')

@app.route('/perform_registration', methods=['POST'])
def perform_registration():  # put application's code here
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
    name = request.form.get('name')
    password = request.form.get('password')

    response = dbo.login_user(name, password)

    if response:
        return "Login successful"
    else:
        return "Login failed"

if __name__ == '__main__':
    app.run(debug=True)
