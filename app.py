import os.path
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def indexed():
    return render_template('index.html')

@app.route('/alphabet')
def alphabet():
    return render_template('alphabet.html')

@app.route('/categories')
def cat():
    return render_template('categories.html')

@app.route('/diseases')
def dis():
    return render_template('diseases.html')

@app.route('/journal')
def journal():
    return render_template('journal.html')


if __name__ == "__main__":
    app.run(Debug=True)
