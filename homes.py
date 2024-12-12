from flask import Blueprint, Flask, jsonify, render_template, request, redirect, url_for, session
import mysql.connector
from utils import *

home_bp = Blueprint('home_bp',__name__)

@home_bp.route('/home')
def home():
    logged_in = 'user_id' in session
    return render_template('home.html', logged_in=logged_in)

