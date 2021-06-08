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
    df1=pd.read_csv(url)
    df2=df1.sort_values(by=['Operation'], ascending=True)
    df3=df2['Operation'].dropna()
    string = df3.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)
    V = list(U)
    W = pd.Series(V).rename('Operation')
    X = W[1:]
    Y = pd.Series(X)
    Y.reset_index(inplace=True, drop=True)
    Z = pd.DataFrame(Y)
    d = Z['Operation']

    

    #W = pd.DataFrame(V) #maybe you need DataFrame
    #W.name = 'Operation'
    #X = W.iloc[1:]
    #d = X.reset_index(drop=True)
    #d=df2['Eponym_easy']
    return render_template('ops.html', names=d)

@app.route('/maps')
def maps():
    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    df1=pd.read_csv(url)
    df2=df1.sort_values(by=['Eponym'], ascending=True)
    d=df2['Eponym_easy']
    return render_template('maps.html', names=d)


if __name__ == "__main__":
    app.run(Debug=True)
