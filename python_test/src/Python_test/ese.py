# -*- coding: utf-8 -*-
'''
Created on 11 mag 2017

@author: id686qfh
'''
''' Applicazione web iniziale '''
from flask import Flask,request,render_template
import random
app = Flask (__name__) # app è un ' applicazione web

@app.route ( '/', methods=['GET', 'POST']) # helloWorld è associato all ' url '/ '
def startPage():
    if request.method == 'POST':
        if request.form['submit'] == 'False':
            if valori[0]=="1":
                ricomincia(valori)
                giusto='false'
            if valori[0]=="0":
                continua(valori)
                giusto='true'
        elif request.form['submit'] == 'True':
            if valori[0]=="0":
                 ricomincia(valori)
                 giusto='false'
            if valori[0]=="1":
                continua(valori)
                giusto='true'
    elif request.method == 'GET':
        giusto=''
        if errori==10:
             restart()
        elif valori=='':
            restart()
    return  render_template('Starting.html',valori=valori,errori=errori,giusto=giusto,startseq=startseq)

def incrementa_errori():
    global errori
    errori=errori+1

def initSequenza():
    global valori
    valori = (str(random.getrandbits(1))+str(random.getrandbits(1))+str(random.getrandbits(1)))
    global startseq
    startseq=valori
    print(startseq)
def prosegui():
    global valori
    valori=valori[1:3]
    
def continua(valori):
    prosegui()
    
def ricomincia(valori):
    initSequenza()
    incrementa_errori()

def restart():
    global errori
    initSequenza()
    errori=0
    
if __name__ == '__main__': # se il modulo è invocato direttamente
    errori=0
    initSequenza()
    app.run (debug=True) # attiva il web server con questa ap