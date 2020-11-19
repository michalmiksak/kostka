from random import choice
from flask import Flask, render_template, session
import random

app = Flask(__name__)
app.debug = True
app.secret_key = 'miksakjebuh'
@app.route('/')
def vyber():
    return render_template("kostky.html")

@app.route('/kostka/<pocet_kostek>')
def kostky(pocet_kostek):
    hrac = []
    pocitac = []
    hrac1 = 0
    pocitac1 = 0

    for i in range(int(pocet_kostek)):
        hrac.append (random.randint (1, 6))
        pocitac.append (random.randint(1,6))
        hrac1 += hrac[i]
        pocitac1 += pocitac[i]
    Remiza = "Remíza"
    Prohra = "Počítač vyhrává"
    Vyhra = "Hráč vyhrává"
    vysledek = choice([Prohra, Vyhra, Remiza])
    if not 'vr_hr' in session:
        session['vr_hr'] = 0


    if not 'vr_pc' in session:
        session['vr_pc'] = 0

    if not 'vr_no' in session:
        session['vr_no'] = 0


    if pocitac1 > hrac1:
        vysledek = Prohra
        session['vr_pc'] = session['vr_pc']+1
    if pocitac1 < hrac1:
        vysledek = Vyhra
        session['vr_hr'] = session['vr_hr']+1
    if pocitac1 == hrac1:
        vysledek = Remiza
        session['vr_no'] = session['vr_no']+1


    return render_template("index.html",pocitac=pocitac,hrac=hrac,hrac1=hrac1,pocitac1=pocitac1,vysledek=vysledek,pc=session['vr_pc'],hr=session['vr_hr'],no=session['vr_no'])

if __name__ == '__main__':
    app.run()