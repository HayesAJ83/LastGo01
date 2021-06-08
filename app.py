import numpy as np
import os.path
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def indexed():
    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    df1=pd.read_csv(url)
    df2=df1.sort_values(by=['Eponym'], ascending=True)
    d=df2['Eponym_easy']
    return render_template('index.html', names=d)

@app.route('/alphabet')
def alphabet():
    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    df1=pd.read_csv(url)
    df2=df1.sort_values(by=['Eponym'], ascending=True)
    d=df2['Eponym_easy']
    return render_template('alphabet.html', names=d)

@app.route('/categories')
def cat():
    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    df1=pd.read_csv(url)
    df2=df1.sort_values(by=['Eponym'], ascending=True)
    d=df2['Eponym_easy']
    return render_template('categories.html', names=d)

@app.route('/diseases')
def dis():
    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    df1=pd.read_csv(url)
    df2=df1.sort_values(by=['Eponym'], ascending=True)
    d=df2['Eponym_easy']
    return render_template('diseases.html', names=d)

@app.route('/journal')
def journal():
    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    df1=pd.read_csv(url)
    df2=df1.sort_values(by=['Eponym'], ascending=True)
    d=df2['Eponym_easy']
    return render_template('journals.html', names=d)

@app.route('/operations')
def ops():
    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    op1=pd.read_csv(url)
    op2=op1.sort_values(by=['Operation'], ascending=True)
    op3=op2['Operation'].dropna()
    Op_string = op3.str.cat(sep=',')
    Op_splits = Op_string.split(",")
    Op_S = set(Op_splits)
    Op_T = np.array(list(Op_S)).astype(object)
    Op_U = np.sort(Op_T)
    Op_V = list(Op_U)
    Op_W = pd.Series(Op_V).rename('Operation')
    Op_X = Op_W[1:]
    Op_Y = pd.Series(Op_X)
    Op_Y.reset_index(inplace=True, drop=True)
    Op_Z = pd.DataFrame(Op_Y)
    ops = Op_Z['Operation']

    ns2=op1.sort_values(by=['Eponym'], ascending=True)
    names=ns2['Eponym_easy']
    
    return render_template('ops.html', ops=ops, names=names)

@app.route('/maps')
def maps():
    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    df1=pd.read_csv(url)
    df2=df1.sort_values(by=['Eponym'], ascending=True)
    d=df2['Eponym_easy']
    return render_template('maps.html', names=d)


if __name__ == "__main__":
    app.run(Debug=True)
