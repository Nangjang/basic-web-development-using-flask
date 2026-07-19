from flask import Flask, render_template, request
from db import Database

app = Flask(__name__)


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

    dbo = Database()
    response = dbo.register_user(name, email, password)

    if response:
        return render_template('index.html', message="Registration successful")
    else:
        return render_template('index.html', message="Registration failed")

if __name__ == '__main__':
    app.run(debug=True)
