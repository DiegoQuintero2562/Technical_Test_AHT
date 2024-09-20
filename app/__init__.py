from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Configurar la base de datos MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@db/inventory_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db = SQLAlchemy(app)

# Importar las rutas después de definir la aplicación y la base de datos
from app import routes