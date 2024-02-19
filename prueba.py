from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'electronimark.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
db = SQLAlchemy(app)

class Empleados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    sede = db.Column(db.String(50), nullable=False)

@app.route("/empleadosLista", methods=["GET"])
def obtener_empleados():
    empleados = Empleados.query.all()
    empleados_json = [{"id": emp.id, "nombre": emp.nombre, "rol": emp.rol, "sede" : emp.sede} for emp in empleados]
    return jsonify(empleados_json)

if __name__ == "__main__":
    print("Creando todas las tablas...")
    with app.app_context():
        db.create_all()
    print("Tablas creadas.")
    print("Verificando si la base de datos existe...")
    if os.path.exists(db_path):
        print("La base de datos existe.")
    else:
        print("La base de datos no existe.")
    app.run(debug=True)
