import os.path
from flask import Flask, render_template, request, url_for, flash, redirect, json, jsonify, session

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/specialties', methods=['GET', 'POST'])
def specialties():
    return render_template('specialties.html')


@app.route('/categories', methods=['GET', 'POST'])
def categories():
    return render_template('categories.html')


@app.route('/diseases', methods=['GET', 'POST'])
def diseases():
    return render_template('diseases.html')


@app.route('/journals', methods=['GET', 'POST'])
def journals():
    return render_template('journals.html')


@app.route('/operations', methods=['GET', 'POST'])
def ops():
    return render_template('ops.html')


@app.route('/maps', methods=['GET', 'POST'])
def maps():
    return render_template('maps.html')


if __name__ == "__main__":
    app.run(Debug=True)
