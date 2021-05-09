import os.path
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(Debug=True)
