# -*- coding: utf-8 -*-
from flask import Flask, request, url_for, redirect, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/resultat")
def resultat():
    return render_template("resultat.html")

@app.route("/resultat_abstention_T1")
def resultat_abstention_T1():
    return render_template("Abstention_T1.html")

@app.route("/resultat_abstention_T2")
def resultat_abstention_T2():
    return render_template("Abstention_T2.html")

@app.route("/resultat_candidat_T1_Sarkozy")
def resultat_candidat_T1_Sarkozy():
    return render_template("Candidat_T1_SARKOZY.html")

@app.route("/resultat_candidat_T2_Sarkozy")
def resultat_candidat_T2_Sarkozy():
    return render_template("Candidat_T2_SARKOZY.html")

@app.route("/resultat_repartition_taux_de_pauvrete_fr")
def resultat_repartition_taux_de_pauvrete_fr():
    return render_template("Taux_de pauvreté.html")

if __name__ == '__main__':
    app.run(debug=True)

#'/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6' 'myapp.py'    
