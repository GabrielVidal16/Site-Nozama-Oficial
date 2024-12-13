from flask import Blueprint, Flask, jsonify, render_template, request, redirect, url_for,session
import mysql.connector
from utils import *
from werkzeug.security import generate_password_hash, check_password_hash

produtos_bp = Blueprint('produtos_bp',__name__)
# Simulação de uma base de dados simples
carrinho = []

<<<<<<< HEAD
@produtos_bp.route('/')
=======
@produtos_bp.route('/produtos')
>>>>>>> 79ce879a98c16ed441e62c46c001e172e33287cd
def home():
    produtos = [
        {"id": 1, "nome": "Elefante Psíquico de Guerra Pré-Histórico", "preco": 99.90, "imagem": "produto 1.jpeg"},
        {"id": 2, "nome": "Lamina do Caos", "preco": 149.90, "imagem": "produto 2.jpeg"},
        {"id": 3, "nome": "Livro Misterioso", "preco": 199.90, "imagem": "produto 3.jpg"},
    ]
    return render_template('home.html', produtos=produtos, logged_in=session.get('logged_in', False))

@produtos_bp.route('/adicionar_ao_carrinho/<int:produto_id>', methods=['POST'])
def adicionar_ao_carrinho(produto_id):
    # Adiciona o produto ao carrinho (apenas o ID para simplificar)
    carrinho.produtos_bpend(produto_id)
    return redirect(url_for('home'))

@produtos_bp.route('/comprar/<int:produto_id>', methods=['POST'])
def comprar(produto_id):
    # Simula a compra do produto
    produto_comprado = next((p for p in carrinho if p['id'] == produto_id), None)
    if produto_comprado:
        return f"Produto {produto_comprado['nome']} comprado com sucesso!"
    return redirect(url_for('home'))

if __name__ == '__main__':
    produtos_bp.run(debug=True)
