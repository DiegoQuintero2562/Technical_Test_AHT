from app import app, db
from app.models import Inventory

if __name__ == '__main__':
    # Crear las tablas en la base de datos si no existen
    with app.app_context():
        db.create_all()

    # Ejecutar la aplicación Flask
    app.run(debug=True, host='0.0.0.0')