import numpy as np
import os.path
import pandas as pd
import matplotlib.pyplot as plt      #[v 3.2.1]
import plotly.express as px          #[v 0.4.1]
import plotly.graph_objects as go    #[v 4.8.1]
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alphabet')
def alphabet():

    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    sp1=pd.read_csv(url)
    sp2=sp1.sort_values(by=['Topic'], ascending=True)
    sp3=sp2['Topic'].dropna()
    Sp_string = sp3.str.cat(sep=',')
    Sp_splits = Sp_string.split(",")
    Sp_S = set(Sp_splits)
    Sp_T = np.array(list(Sp_S)).astype(object)
    Sp_U = np.sort(Sp_T)
    Sp_V = list(Sp_U)
    Sp_W = pd.Series(Sp_V).rename('Topic')
    Sp_X = Sp_W[1:]
    Sp_Y = pd.Series(Sp_X)
    Sp_Y.reset_index(inplace=True, drop=True)
    Sp_Z = pd.DataFrame(Sp_Y)
    specs = Sp_Z['Topic']
    specs

    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    df1=pd.read_csv(url)
    df2=df1.sort_values(by=['Eponym'], ascending=True)
    d=df2['Eponym_easy']
    return render_template('alphabet.html', specs=specs, names=d)


@app.route('/categories', methods=["POST", "GET"])
def cat():

    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    sp1=pd.read_csv(url)
    sp2=sp1.sort_values(by=['Topic'], ascending=True)
    sp3=sp2['Topic'].dropna()
    Sp_string = sp3.str.cat(sep=',')
    Sp_splits = Sp_string.split(",")
    Sp_S = set(Sp_splits)
    Sp_T = np.array(list(Sp_S)).astype(object)
    Sp_U = np.sort(Sp_T)
    Sp_V = list(Sp_U)
    Sp_W = pd.Series(Sp_V).rename('Topic')
    Sp_X = Sp_W[1:]
    Sp_Y = pd.Series(Sp_X)
    Sp_Y.reset_index(inplace=True, drop=True)
    Sp_Z = pd.DataFrame(Sp_Y)
    specs = Sp_Z['Topic']
    specs
    
    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    df1=pd.read_csv(url)
    df2=df1.sort_values(by=['Eponym'], ascending=True)
    d=df2['Eponym_easy']

    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    tp1=pd.read_csv(url)
    tp2=tp1.sort_values(by=['Type'], ascending=True)
    tp3=tp2['Type'].dropna()
    Tp_string = tp3.str.cat(sep=',')
    Tp_splits = Tp_string.split(",")
    Tp_S = set(Tp_splits)
    Tp_T = np.array(list(Tp_S)).astype(object)
    Tp_U = np.sort(Tp_T)
    Tp_V = list(Tp_U)
    Tp_W = pd.Series(Tp_V).rename('Type')
    Tp_X = pd.Series(Tp_W)
    Tp_X.reset_index(inplace=True, drop=True)
    Tp_Y = pd.DataFrame(Tp_X)
    cats = Tp_Y['Type']

    return render_template('categories.html', specs=specs, names=d, cats=cats)


@app.route('/diseases')
def dis():

    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    sp1=pd.read_csv(url)
    sp2=sp1.sort_values(by=['Topic'], ascending=True)
    sp3=sp2['Topic'].dropna()
    Sp_string = sp3.str.cat(sep=',')
    Sp_splits = Sp_string.split(",")
    Sp_S = set(Sp_splits)
    Sp_T = np.array(list(Sp_S)).astype(object)
    Sp_U = np.sort(Sp_T)
    Sp_V = list(Sp_U)
    Sp_W = pd.Series(Sp_V).rename('Topic')
    Sp_X = Sp_W[1:]
    Sp_Y = pd.Series(Sp_X)
    Sp_Y.reset_index(inplace=True, drop=True)
    Sp_Z = pd.DataFrame(Sp_Y)
    specs = Sp_Z['Topic']
    specs
    
    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"

    ds1=pd.read_csv(url)
    ds2=ds1.sort_values(by=['Disease'], ascending=True)
    ds3=ds2['Disease'].dropna()
    Ds_string = ds3.str.cat(sep=',')
    Ds_splits = Ds_string.split(",")
    Ds_S = set(Ds_splits)
    Ds_T = np.array(list(Ds_S)).astype(object)
    Ds_U = np.sort(Ds_T)
    Ds_V = list(Ds_U)
    Ds_W = pd.Series(Ds_V).rename('Disease')
    Ds_X = Ds_W[1:]
    Ds_Y = pd.Series(Ds_X)
    Ds_Y.reset_index(inplace=True, drop=True)
    Ds_Z = pd.DataFrame(Ds_Y)
    diseases = Ds_Z['Disease']
    diseases

    df1=pd.read_csv(url)
    df2=df1.sort_values(by=['Eponym'], ascending=True)
    d=df2['Eponym_easy']
    
    return render_template('diseases.html', specs=specs, names=d, diseases=diseases)

@app.route('/journal')
def journal():
    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    sp1=pd.read_csv(url)
    sp2=sp1.sort_values(by=['Topic'], ascending=True)
    sp3=sp2['Topic'].dropna()
    Sp_string = sp3.str.cat(sep=',')
    Sp_splits = Sp_string.split(",")
    Sp_S = set(Sp_splits)
    Sp_T = np.array(list(Sp_S)).astype(object)
    Sp_U = np.sort(Sp_T)
    Sp_V = list(Sp_U)
    Sp_W = pd.Series(Sp_V).rename('Topic')
    Sp_X = Sp_W[1:]
    Sp_Y = pd.Series(Sp_X)
    Sp_Y.reset_index(inplace=True, drop=True)
    Sp_Z = pd.DataFrame(Sp_Y)
    specs = Sp_Z['Topic']
    specs
    
    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    df1=pd.read_csv(url)
    df2=df1.sort_values(by=['Eponym'], ascending=True)
    d=df2['Eponym_easy']

    jn1=pd.read_csv(url)
    jn2=jn1.sort_values(by=['Journal'], ascending=True)
    jn3=jn2['Journal'].dropna()
    Jn_string = jn3.str.cat(sep=',')
    Jn_splits = Jn_string.split(",")
    Jn_S = set(Jn_splits)
    Jn_T = np.array(list(Jn_S)).astype(object)
    Jn_U = np.sort(Jn_T)
    Jn_V = list(Jn_U)
    Jn_W = pd.Series(Jn_V).rename('Journal')
    Jn_X = Jn_W[1:]
    Jn_Y = pd.Series(Jn_X)
    Jn_Y.reset_index(inplace=True, drop=True)
    Jn_Z = pd.DataFrame(Jn_Y)
    journals = Jn_Z['Journal']
    journals

    return render_template('journals.html', specs=specs, names=d, journals=journals)

@app.route('/operations')
def ops():
    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    sp1=pd.read_csv(url)
    sp2=sp1.sort_values(by=['Topic'], ascending=True)
    sp3=sp2['Topic'].dropna()
    Sp_string = sp3.str.cat(sep=',')
    Sp_splits = Sp_string.split(",")
    Sp_S = set(Sp_splits)
    Sp_T = np.array(list(Sp_S)).astype(object)
    Sp_U = np.sort(Sp_T)
    Sp_V = list(Sp_U)
    Sp_W = pd.Series(Sp_V).rename('Topic')
    Sp_X = Sp_W[1:]
    Sp_Y = pd.Series(Sp_X)
    Sp_Y.reset_index(inplace=True, drop=True)
    Sp_Z = pd.DataFrame(Sp_Y)
    specs = Sp_Z['Topic']
    specs
    
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
    
    return render_template('ops.html', specs=specs, ops=ops, names=names)

@app.route('/maps')
def maps():
    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    sp1=pd.read_csv(url)
    sp2=sp1.sort_values(by=['Topic'], ascending=True)
    sp3=sp2['Topic'].dropna()
    Sp_string = sp3.str.cat(sep=',')
    Sp_splits = Sp_string.split(",")
    Sp_S = set(Sp_splits)
    Sp_T = np.array(list(Sp_S)).astype(object)
    Sp_U = np.sort(Sp_T)
    Sp_V = list(Sp_U)
    Sp_W = pd.Series(Sp_V).rename('Topic')
    Sp_X = Sp_W[1:]
    Sp_Y = pd.Series(Sp_X)
    Sp_Y.reset_index(inplace=True, drop=True)
    Sp_Z = pd.DataFrame(Sp_Y)
    specs = Sp_Z['Topic']
    specs
    
    url="https://raw.githubusercontent.com/HayesAJ83/LastGo01/master/static/database/Eps4SN.csv"
    df1=pd.read_csv(url)
    df2=df1.sort_values(by=['Eponym'], ascending=True)
    d=df2['Eponym_easy']
    return render_template('maps.html', specs=specs, names=d)


if __name__ == "__main__":
    app.run(Debug=True)
