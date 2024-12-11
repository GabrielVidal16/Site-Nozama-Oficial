
from flask import Flask, jsonify, render_template, request, redirect, url_for
import mysql.connector
import utils


from usuarios import usuarios_bp
from homes import home_bp
from rotas_testes import produtos_bp

app = Flask(__name__)
app.secret_key = 'segredo_maligno'


app.register_blueprint(usuarios_bp)
app.register_blueprint(home_bp)
app.register_blueprint(produtos_bp)


@app.route('/', methods=['GET'])
def inicial():
    return render_template('/home.html')

if __name__ == '__main__':
    app.run(debug=True)