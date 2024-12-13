from flask import Blueprint, Flask, jsonify, render_template, request, redirect, url_for, session
import mysql.connector
from utils import *

itens = []
carrinho_bp = Blueprint('carrinho_bp',__name__)

@carrinho_bp.route('/carrinho', methods=['POST', 'GET'])
def carrinho():
    return redirect(url_for('home_bp.'))

@carrinho_bp.route('/adicionar/<int:produto_id>', methods=['POST', 'GET'])
def adicionar_ao_carrinho(produto_id):
    if request.method == 'GET' :
        return render_template('carrinho_de_compras.html')
    
    if request.method == 'POST':
        # Adiciona o produto ao carrinho (apenas o ID para simplificar)
        itens.append(produto_id)
        return redirect(url_for('carrinho_bp.carrinho'))
    