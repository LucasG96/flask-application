from flask import Flask, render_template, request, redirect, session, flash, url_for

# __name__ representa o nome do nosso módulo
app = Flask(__name__)
# chave secreta, necessária para utilizar o flash
app.secret_key = 'lucas'

listaJogos = list()

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

usuario1 = Usuario('usuario1', '123')
usuario2 = Usuario('usuario2', '345')
usuario3 = Usuario('usuario3', '234')

listaUsuarios = {usuario1.usuario: usuario1, usuario2.usuario: usuario2, usuario3.usuario: usuario3}

# Define uma rota para o sistema
@app.route('/jogos')
def index():
    # Renderiza uma página html que se encontra na pasta templates
    # e manda as variáveis titulo e jogos no response
    return render_template('lista.html', titulo='Jogos', jogos=listaJogos)

@app.route('/jogos/novo')
def formulario():
    if 'usuario' not in session or session['usuario'] == None:
        flash('Favor efeturar login.')
        return redirect(url_for('login', proxima=url_for('formulario')))
    else:
        return render_template('novo.html', titulo='Novo Jogo')

@app.route('/jogos/novo', methods=['POST',])
def novoJogo():
    # request nos possibilita capturar o que está vindo da requisição
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    listaErros = list()
    listaErros.append("O campo nome não pode estar vazio") if nome == "" else ""
    listaErros.append("O campo categoria não pode estar vazio") if categoria == "" else ""
    listaErros.append("O campo console não pode estar vazio") if console == "" else ""

    if(len(listaErros) > 0):
        return render_template('novo.html', listaErros=listaErros, nome=nome, categoria=categoria, console=console)
    else:
        jogo = Jogo(nome, categoria, console)
        listaJogos.append(jogo)
        # redirect permite redicionar para páginas diversas
        return redirect(url_for('index'))

@app.route('/login')
def login():
    # Captura um parâmetro passado pela url
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/login', methods=['POST',])
def logar():
    usuario = request.form['usuario'] 
    senha = request.form['senha']
    proxima = request.form['proxima']

    if usuario in listaUsuarios and listaUsuarios[usuario].senha == senha:
        session['usuario'] = usuario
        flash('Usuário ' + usuario + ' logado com sucesso!')
        return redirect(proxima)

    # flash define uma mensagem rápida para o retorno
    flash('Credenciais de login incorretas!')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario'] = None
    flash('Usuário deslogado com sucesso!')
    return redirect(url_for('login'))

# Faz com que o modo de desenvolvimento seja ativado, isso 
# permite que qualquer alteração no código reinicie o servidor 
app.run(debug=True)