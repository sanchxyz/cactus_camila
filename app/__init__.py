from flask import Flask, render_template

def create_app():
    # Crear la aplicación Flask
    app = Flask(__name__)

    # Configuración de la aplicación
    app.config.from_pyfile('config.py')  # Cargar configuración desde config.py
    app.config['SECRET_KEY'] = 'supersecretkey'  # Clave secreta (mejor usar variables de entorno)

    # Ruta principal (página de inicio)
    @app.route('/')
    def home():
        return render_template('index.html')

    # Ruta de login
    @app.route('/login')
    def login():
        return render_template('login.html')

    # Ruta de productos (ejemplo)
    @app.route('/products')
    def products():
        return render_template('producto.html')  # Cambia esto según tu lógica

    # Ruta de administración (ejemplo)
    @app.route('/admin/dashboard')
    def admin_dashboard():
        return render_template('admin/dashboard.html')  # Cambia esto según tu lógica

    return app