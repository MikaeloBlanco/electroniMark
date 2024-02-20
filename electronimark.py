from flask import Flask, abort, request, jsonify
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

@app.route("/agregarEmpleado", methods=["POST"])
def agregar_empleado():
    if not request.json or not 'nombre' in request.json or not 'rol' in request.json or not 'sede' in request.json:
        abort(400)
    empleado = Empleados(nombre=request.json['nombre'], rol=request.json['rol'], sede=request.json['sede'])
    db.session.add(empleado)
    db.session.commit()
    return jsonify({'empleado': empleado.nombre}), 201

@app.route("/editarEmpleado/<int:id>", methods=["PUT"])
def editar_empleado(id):
    empleado = Empleados.query.get(id)
    if empleado is None:
        abort(404)
    if not request.json:
        abort(400)
    if 'nombre' in request.json:
        empleado.nombre = request.json['nombre']
    if 'rol' in request.json:
        empleado.rol = request.json['rol']
    if 'sede' in request.json:
        empleado.sede = request.json['sede']
    db.session.commit()
    return jsonify({'empleado': empleado.nombre}), 200

@app.route("/borrarEmpleado/<int:id>", methods=["DELETE"])
def borrar_empleado(id):
    empleado = Empleados.query.get(id)
    if empleado is None:
        abort(404)
    db.session.delete(empleado)
    db.session.commit()
    return jsonify({'se ha borrado': True})

@app.route("/empleado/<int:id>", methods=["GET"])
def obtener_empleado(id):
    empleado = Empleados.query.get(id)
    if empleado is None:
        abort(404)
    empleado_json = {"id": empleado.id, "nombre": empleado.nombre, "rol": empleado.rol, "sede" : empleado.sede}
    return jsonify(empleado_json)

@app.route("/empleadosPorRol/<string:rol>", methods=["GET"])
def obtener_empleados_por_rol(rol):
    empleados = Empleados.query.filter_by(rol=rol).all()
    empleados_json = [{"id": emp.id, "nombre": emp.nombre, "rol": emp.rol, "sede" : emp.sede} for emp in empleados]
    return jsonify(empleados_json)

@app.route("/empleadosPorSede/<string:sede>", methods=["GET"])
def obtener_empleados_por_sede(sede):
    empleados = Empleados.query.filter_by(sede=sede).all()
    empleados_json = [{"id": emp.id, "nombre": emp.nombre, "rol": emp.rol, "sede" : emp.sede} for emp in empleados]
    return jsonify(empleados_json)


if __name__ == "__main__":
    print("Crear tablas")
    with app.app_context():
        db.create_all()
    print("Tablas creadas")
    print("Comprobando que la base de datos existe")
    if os.path.exists(db_path):
        print("La base de datos existe")
    else:
        print("La base de datos no existe")
    app.run(debug=True)
