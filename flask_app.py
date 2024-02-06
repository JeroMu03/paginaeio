from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash


app = Flask(__name__)



@app.route('/',) #PAGINA DE INICIO
def usuario():
    return render_template('index.html')

@app.route('/menu') 
def bienvenida():
    return render_template('menu.html')

@app.route('/cinfo') 
def cinfo():
    return render_template('cinfo.html')

@app.route('/libbioga') 
def libbioga():
    return render_template('libbioga.html')

@app.route('/anpat') 
def anpat():
    return render_template('antpat.html')

@app.route('/biogca') 
def biogca():
    return render_template('biogca.html')

@app.route('/biogcb') 
def biogcb():
    return render_template('biogcb.html')

@app.route('/fecha')
def fecha():
    return render_template('fecha.html')

@app.route('/intodonto') 
def intodonto():
    return render_template('intodonto.html')

@app.route('/fundquima') 
def fundquima():
    return render_template('funquima.html')

@app.route('/fundquimb')
def fundquimb():
    return render_template('funquimb.html')

@app.route('/metod')
def metod():
    return render_template('metodologia.html')

if __name__ == '__main__': 
    app.run(debug = True)