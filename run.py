
from project_library_api.app import app
from flask import Flask, render_template

@app.route('/')
def login():
    return render_template('login.html')
    
@app.route('/login')
def login_v2():
    return render_template('login.html')

@app.route('/inicial_user')
def inicial_user():
    return render_template('inicial_user.html')

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

@app.route('/meus_livros')
def meus_livros():
    return render_template('meus_livros.html')

@app.route('/estoque')
def estoque():
    return render_template('estoque.html')

@app.route('/conta_admin')
def conta_admin():
    return render_template('conta_admin.html')

@app.route('/adicionar_livro')
def adicionar_livro():
    return render_template('adicionar_livro.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/conta_user')
def conta_user():
    return render_template('conta_user.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
