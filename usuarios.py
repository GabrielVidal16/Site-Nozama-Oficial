from flask import Blueprint, Flask, jsonify, render_template, request, redirect, url_for,session
import mysql.connector
from utils import *
from werkzeug.security import generate_password_hash, check_password_hash

usuarios_bp = Blueprint('usuarios_bp',__name__)

@usuarios_bp.route('/registro', methods=['GET','POST'])
def registrar_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']


        con = connect_to_database()
        if not con:
            return jsonify({'error': 'Failed to connect to database'}), 500
            
        try:
            cursor = con.cursor()

            cursor.execute('SELECT * FROM usuarios WHERE email = %s', (email,))
            usuario_existente = cursor.fetchone()

            if usuario_existente:
                return jsonify({"message": "Usuário já existe"}), 409
        
            hashed_password = generate_password_hash(senha, method='pbkdf2:sha256:600000')

            sql = "INSERT INTO usuarios (nome, email , senha) VALUES (%s, %s, %s)"
            cursor.execute(sql, ( nome , email , hashed_password ))
            con.commit()

            return redirect(url_for('usuarios_bp.login'))


        except mysql.connector.Error as error:
            print(f"Failed to insert record: {error}")
            return "Ocorreu um erro ao inserir os dados.", 500
        
        finally:
                
                if cursor:
                    cursor.close()
                if con.is_connected():
                    con.close()

    if request.method == 'GET':
        return render_template('cadastro_usuario.html')


@usuarios_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # Obter os dados enviados no formulário
        email = request.form.get('email')
        senha = request.form.get('senha')

        # Validação inicial
        if not email or not senha:
            return jsonify({"error": "Campos 'email' e 'senha' são obrigatórios"}), 400

        # Conectar ao banco de dados
        con = connect_to_database()
        if not con:
            return jsonify({"error": "Falha ao conectar ao banco de dados"}), 500

        try:
            cursor = con.cursor()
            # Consulta para buscar o usuário pelo e-mail
            cursor.execute('SELECT id, email , senha , nome FROM usuarios WHERE email = %s', (email,))
            usuario = cursor.fetchone()

            # Verificar se o usuário existe
            if not usuario:
                return jsonify({"error": "E-mail ou senha inválidos"}), 401

            # Comparar a senha criptografada
            senha_hash = usuario[2]
            if not check_password_hash(senha_hash, senha):
                return jsonify({"error": "E-mail ou senha inválidos"}), 401
            
            session['user_id'] = usuario[0]
            session['email'] = usuario[1]
            session['nome'] = usuario[3]
            

        except mysql.connector.Error as e:
            return jsonify({"error": "Erro ao consultar o banco de dados", "details": str(e)}), 500

        finally:
            # Fechar os recursos
            if cursor:
                cursor.close()
            if con.is_connected():
                con.close()
    if request.method == 'GET':
        return render_template('login_usuario.html')
    return redirect(url_for('home_bp.home'))



@usuarios_bp.route('/atualizar/<int:usuario_id>', methods=['PUT'])
def atualizar_usuario(usuario_id):
    # Obter os dados do formulário
    dados = request.json  # Assumindo que os dados são enviados em formato JSON

    # Validar os dados
    # ... (implementar a validação aqui)

    # Construir a consulta SQL
    sql = "UPDATE usuarios SET nome=%s, email=%s, senha =%s  WHERE id=%s"
    valores = (dados['nome'], dados['email'], dados['senha'], usuario_id)

    # Conectar ao banco de dados e executar a consulta
    try:
        con = connect_to_database()  # Assuming you have a function to get a valid con
        if not con:
            return jsonify({'error': 'Failed to connect to database'}), 500
        with con as mydb:
            mycursor = mydb.cursor()
            mycursor = mydb.cursor()
            mycursor.execute(sql, valores)
            mydb.commit()
            
            return jsonify({'': 'Usuário atualizado com sucesso'}), 200
    except mysql.connector.Error as error:
        return jsonify({'error': str(error)}), 500



@usuarios_bp.route('/listar', methods=['GET'])
def listar_usuarios():
    try:
        # Conectar ao banco de dados
        con = connect_to_database()  # Assuming you have a function to get a valid con
        if not con:
            return jsonify({'error': 'Failed to connect to database'}), 500
        with con as mydb:
            mycursor = mydb.cursor()

            # Executar a consulta SQL para selecionar todos os usuários
            sql = "SELECT * FROM usuarios"
            mycursor.execute(sql)

            # Obter os resultados da consulta
            resultados = mycursor.fetchall()

            # Formatar os resultados em um JSON
            usuarios = []
            for usuario in resultados:
                usuarios.append({'id': usuario[0], 'nome': usuario[1], 'email': usuario[2], 'senha': usuario[3]})

            return jsonify({'usuarios': usuarios}), 200
    except mysql.connector.Error as error:
        return jsonify({'error': str(error)}), 500



@usuarios_bp.route('/get_usuario/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):

    try:
        # Conectar ao banco de dados
        con = connect_to_database()  # Assuming you have a function to get a valid con
        if not con:
            return jsonify({'error': 'Failed to connect to database'}), 500
        with con as mydb:
            mycursor = mydb.cursor()

            # Executar a consulta SQL para selecionar todos os usuários
            sql = "SELECT * FROM usuarios where id=%s "
            valores = (usuario_id,)

            mycursor.execute(sql,valores)

            # Obter os resultados da consulta
            resultados = mycursor.fetchall()

            # Formatar os resultados em um JSON
            usuarios = []
            for usuario in resultados:
                usuarios.append({'id': usuario[0], 'nome': usuario[1], 'email': usuario[2], '': usuario[3]})

            return jsonify({'usuario': usuarios[0]}), 200
    except mysql.connector.Error as error:
        return jsonify({'error': str(error)}), 500


@usuarios_bp.route('/get_nome_usuarios', methods=['GET'])
def get_nome_usuarios():
    nome = request.args.get('nome')

    if nome:
        # Construir a consulta SQL com o parâmetro de pesquisa
        sql = "SELECT * FROM usuarios WHERE nome LIKE %s"
        valores = ('%' + nome + '%',)
        try:
            con = connect_to_database()  # Assuming you have a function to get a valid con
            if not con:
                return jsonify({'error': 'Failed to connect to database'}), 500
            with con as mydb:
                mycursor = mydb.cursor()
                mycursor.execute(sql, valores)
                resultados = mycursor.fetchall()

                # Formatar os resultados em um JSON
                usuarios = []
                for usuario in resultados:
                    usuarios.append({'id': usuario[0], 'nome': usuario[1], 'email': usuario[2], 'senha': usuario[3]})

                return jsonify({'usuarios': usuarios}), 200
        except mysql.connector.Error as error:
            return jsonify({'error': str(error)}), 500
    else:
        return jsonify({'': 'O parâmetro "nome" é obrigatório'}), 400



@usuarios_bp.route('/del_usuario/<int:usuario_id>', methods=['DELETE'])
def del_usuario(usuario_id):
    
    try:
        # Conectar ao banco de dados
        con = connect_to_database()  # Assuming you have a function to get a valid con
        if not con:
            return jsonify({'error': 'Failed to connect to database'}), 500
        with con as mydb:
            mycursor = mydb.cursor()

            # Executar a consulta SQL para selecionar todos os usuários
            sql = "DELETE from usuarios where id=%s "
            valores = (usuario_id,)

            mycursor.execute(sql,valores)


            return jsonify({'usuario deletado com sucesso':  str()}), 200
    except mysql.connector.Error as error:
        return jsonify({'error': str(error)}), 500