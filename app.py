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

if __name__ == "__main__":
    app.run(Debug=True)
