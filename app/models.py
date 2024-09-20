# Importación de la instancia de la base de datos
from app import db

# Definición del modelo Inventory
class Inventory(db.Model):
    # Definición de los campos de la tabla
    id = db.Column(db.Integer, primary_key=True)# ID del elemento (clave primaria)
    name = db.Column(db.String(100), nullable=False)# Nombre del elemento
    price = db.Column(db.Float, nullable=False)# Precio del elemento
    mac_address = db.Column(db.String(50), nullable=True)  # Asegúrate de que nullable=True si es opcional
    serial_number = db.Column(db.String(100), nullable=False)# Número de serie
    manufacturer = db.Column(db.String(100), nullable=False)# Fabricante
    description = db.Column(db.Text, nullable=True)# Descripción del elemento

    def __repr__(self):
        # Representación del objeto Inventory
        return f'<Inventory {self.name}>'