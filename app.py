
from flask import Flask, jsonify, render_template, request, redirect, url_for, session
import mysql.connector
import utils


from usuarios import usuarios_bp
from homes import home_bp
from rotas_testes import produtos_bp

app = Flask(__name__)
app.secret_key = 'segredo_maligno'
app.config['SESSION_PERMANENT'] = False



app.register_blueprint(usuarios_bp)
app.register_blueprint(home_bp)
app.register_blueprint(produtos_bp)
<<<<<<< HEAD

=======
>>>>>>> 79ce879a98c16ed441e62c46c001e172e33287cd

@app.route('/')
def index():
    return redirect(url_for('inicial'))  # Redireciona para /inicial


@app.route('/inicial', methods=['GET'])
def inicial():
    return redirect(url_for('home_bp.home'))

if __name__ == '__main__':
    app.run(debug=True)