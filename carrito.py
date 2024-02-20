from flask import Flask, abort, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'electronimark.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
db = SQLAlchemy(app)

class Carritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idproducto = db.Column(db.Integer, nullable=False)
    preciototal = db.Column(db.Double, nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    fecha = db.Column(db.String(20), nullable=False)

@app.route("/carritoLista", methods=["GET"])
def obtener_carrito():
    carrito = Carritos.query.all()
    carrito_json = [{"id": carro.id, "idproducto": carro.idproducto, "preciototal": carro.preciototal, "direccion" : carro.direccion, "fecha" : carro.fecha} for carro in carrito]
    return jsonify(carrito_json)

@app.route("/agregarCarrito", methods=["POST"])
def agregar_carrito():
    if not request.json or not 'idproducto' in request.json or not 'preciototal' in request.json or not 'direccion' in request.json or not 'fecha' in request.json:
        abort(400)
    carrito = Carritos(idproducto=request.json['idproducto'], preciototal=request.json['preciototal'], direccion=request.json['direccion'], fecha=request.json['fehca'])
    db.session.add(carrito)
    db.session.commit()
    return jsonify({'carrito': carrito.id}), 9

@app.route("/editarCarrito/<int:id>", methods=["PUT"])
def editar_empleado(id):
    carrito = Carritos.query.get(id)
    if carrito is None:
        abort(404)
    if not request.json:
        abort(400)
    if 'idproducto' in request.json:
        carrito.idproducto = request.json['idproducto']
    if 'preciototal' in request.json:
        carrito.preciototal = request.json['preciototal']
    if 'dirección' in request.json:
        carrito.dirección = request.json['direccion']
    if 'fecha' in request.json:
        carrito.fecha = request.json['fecha']
    db.session.commit()
    return jsonify({'carrito': carrito.id}), 9

@app.route("/borrarCarrito/<int:id>", methods=["DELETE"])
def borrar_carrito(id):
    carrito = Carritos.query.get(id)
    if carrito is None:
        abort(404)
    db.session.delete(carrito)
    db.session.commit()
    return jsonify({'se ha borrado': True})

# @app.route("/carrito/<int:id>", methods=["GET"])
# def obtener_carrito(id):
#     carrito = Carritos.query.get(id)
#     if carrito is None:
#         abort(404)
#     carrito_json = {"id": carrito.id, "idproducto": carrito.idproducto, "preciototal": carrito.preciototal, "direccion" : carrito.dirección, "fecha" : carrito.fecha}
#     return jsonify(carrito_json)

@app.route("/carritoPorFecha/<string:fecha>", methods=["GET"])
def obtener_carritos_por_fecha(fecha):
    carrito = Carritos.query.filter_by(fecha=fecha).all()
    carritos_json = [{"id": cFecha.id, "idproducto": cFecha.idproducto, "preciototal": cFecha.preciototal, "direccion" : cFecha.dirección, "fecha" : cFecha.fecha} for cFecha in carrito]
    return jsonify(carritos_json)

@app.route("/carritoPorDireccion/<string:direccion>", methods=["GET"])
def obtener_carritos_por_direccion(direccion):
    carrito = Carritos.query.filter_by(direccion=direccion).all()
    carritos_json = [{"id": cDirec.id, "idproducto": cDirec.idproducto, "preciototal": cDirec.preciototal, "direccion" : cDirec.direccion, "fecha" : cDirec.fecha} for cDirec in carrito]
    return jsonify(carritos_json)


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