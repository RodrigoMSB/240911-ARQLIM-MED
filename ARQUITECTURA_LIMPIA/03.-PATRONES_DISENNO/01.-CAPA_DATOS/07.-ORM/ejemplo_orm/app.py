from flask import Flask, render_template, request, redirect
from models import db, Usuario
from service import UsuarioService

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basededatos.db'  # Esto crea un archivo local llamado mi_basededatos.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos la base de datos
db.init_app(app)
usuario_service = UsuarioService()

@app.before_request
def create_tables():
    db.create_all()

# Rutas
@app.route('/')
def index():
    usuarios = usuario_service.obtener_usuarios()
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        usuario_service.agregar_usuario(nombre)
        return redirect('/')
    return render_template('agregar.html')

if __name__ == '__main__':
    app.run(debug=True)