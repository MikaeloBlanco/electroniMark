from flask import Flask, abort, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'productos.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
db = SQLAlchemy(app)

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(255), nullable=False)

@app.route("/productosLista", methods=["GET"])
def obtener_productos():
    productos = Productos.query.all()
    productos_json = [{"id": prod.id, "nombre": prod.nombre, "precio": prod.precio, "categoria": prod.categoria} for prod in productos]
    return jsonify(productos_json)

@app.route("/agregarProducto", methods=["POST"])
def agregar_producto():
    if not request.json or not 'nombre' in request.json or not 'precio' in request.json or not 'categoria' in request.json:
        abort(400)
    producto = Productos(nombre=request.json['nombre'], precio=request.json['precio'], categoria=request.json['categoria'])
    db.session.add(producto)
    db.session.commit()
    return jsonify({'producto': producto.nombre}), 201

@app.route("/editarProducto/<int:id>", methods=["PUT"])
def editar_producto(id):
    producto = Productos.query.get(id)
    if producto is None:
        abort(404)
    if not request.json:
        abort(400)
    if 'nombre' in request.json:
        producto.nombre = request.json['nombre']
    if 'precio' in request.json:
        producto.precio = request.json['precio']
    if 'categoria' in request.json:
        producto.categoria = request.json['categoria']
    db.session.commit()
    return jsonify({'producto': producto.nombre}), 200

@app.route("/borrarProducto/<int:id>", methods=["DELETE"])
def borrar_producto(id):
    producto = Productos.query.get(id)
    if producto is None:
        abort(404)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({'se ha borrado': True})

@app.route("/producto/<int:id>", methods=["GET"])
def obtener_producto(id):
    producto = Productos.query.get(id)
    if producto is None:
        abort(404)
    producto_json = {"id": producto.id, "nombre": producto.nombre, "precio": producto.precio, "categoria": producto.categoria}
    return jsonify(producto_json)

@app.route("/productosPorCategoria/<string:categoria>", methods=["GET"])
def obtener_productos_por_categoria(categoria):
    productos = Productos.query.filter_by(categoria=categoria).all()
    productos_json = [{"id": prod.id, "nombre": prod.nombre, "precio": prod.precio, "categoria": prod.categoria} for prod in productos]
    return jsonify(productos_json)

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
