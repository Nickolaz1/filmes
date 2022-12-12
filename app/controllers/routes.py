from app import app
from flask import render_template, request

from app.models import filmes

@app.route("/", methods=['GET', 'POST'], defaults={'id':None})
@app.route("/<int:id>")
def index(id):
    filmesList = filmes.filmes

    if request.method == "POST":
        filme = {
            'titulo': request.form.get('titulo'),
            'diretor': request.form.get('diretor'),
            'resumo': request.form.get('resumo'),
            'data': request.form.get('data'),
            'nota': request.form.get('nota')
        }
        filmesList.append(filme)

    if id is not None:
        try:
            del(filmesList[id])
        except:
            pass      
    return render_template("index.html", filmes=filmesList, qtde=len(filmesList))


@app.route('/cadastrar')
def cadastrar():
    return render_template("cadastro.html")


@app.route('/sobre')
def sobre():
    return render_template("sobre.html")