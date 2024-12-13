from flask import Blueprint, Flask, jsonify, render_template, request, redirect, url_for, session
import mysql.connector
from utils import *

carrinho_bp = Blueprint('carrinho_bp',__name__)

@carrinho_bp.route('/carrinho')
def carrinho():
    return render_template('carrinho_de_compras.html')