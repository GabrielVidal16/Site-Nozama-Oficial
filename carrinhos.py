from flask import Blueprint, Flask, jsonify, render_template, request, redirect, url_for, session
import mysql.connector
from utils import *

itens = [{}]
itens.clear()

carrinho_bp = Blueprint('carrinho_bp', __name__)

@carrinho_bp.route('/carrinho', methods=['POST', 'GET'])
def carrinho():
    return render_template('carrinho_de_compras.html', itens=itens)

@carrinho_bp.route('/adicionar/<int:produto_id>', methods=['POST'])
def adicionar_ao_carrinho(produto_id):
    if request.method == 'POST':
        produtos = [
            {"id": 1, "nome": "Elefante Psíquico de Guerra Pré-Histórico", "preco": 99.90, "imagem": "produto 1.jpeg"},
            {"id": 2, "nome": "Lamina do Caos", "preco": 149.90, "imagem": "produto 2.jpeg"},
            {"id": 3, "nome": "Livro Misterioso", "preco": 199.90, "imagem": "produto 3.jpg"},
        ]
        # Encontrar o produto com o id correspondente
        for produto in produtos:
            if produto_id == produto["id"]:   
                
                itens.append({"id": produto["id"],"nome": produto["nome"], "preco": produto["preco"]})


        return redirect(url_for('home_bp.home'))



    
    