from flask import Blueprint, Flask, jsonify, render_template, request, redirect, url_for, session
import mysql.connector
from utils import *

home_bp = Blueprint('home_bp',__name__)

@home_bp.route('/home')
def home():
    produtos = [
        {"id": 1, "nome": "Elefante Psíquico de Guerra Pré-Histórico", "preco": 99.90, "imagem": "produto 1.jpeg"},
        {"id": 2, "nome": "Lamina do Caos", "preco": 149.90, "imagem": "produto 2.jpeg"},
        {"id": 3, "nome": "Livro Misterioso", "preco": 199.90, "imagem": "produto 3.jpg"},
    ]
    logged_in = 'user_id' in session
    return render_template('home.html', produtos=produtos,logged_in=logged_in)

