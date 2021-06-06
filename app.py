import os.path
import pandas as pd
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
    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    c=pd.read_csv(url)
    d=c['Eponym']
    #names = df['Eponym']
    names = ["John", "Mary", "Wes", "Sally"]
    return render_template('alphabet.html', names=d)

@app.route('/categories')
def cat():
    return render_template('categories.html')

@app.route('/diseases')
def dis():
    names = ["Barrett's oesophagus", "Babcock forceps", "Crohn's disease", "DeBakey forceps"]
    return render_template('diseases.html', names=names)

@app.route('/journal')
def journal():
    return render_template('journals.html')

@app.route('/operations')
def ops():
    return render_template('ops.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')


if __name__ == "__main__":
    app.run(Debug=True)
