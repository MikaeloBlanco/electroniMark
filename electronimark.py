from flask import Flask, abort, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'electronimark.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
db = SQLAlchemy(app)

# Declaraciones de clases #

class Empleados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    sede = db.Column(db.String(50), nullable=False)

class Carritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    preciototal = db.Column(db.Double, nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    fecha = db.Column(db.String(20), nullable=False)

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(255), nullable=False)

# Endpoints empleados #

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

# Fin de endpoints empleados #

##############################

# Endpoints carrito #

@app.route("/carritoLista", methods=["GET"])
def obtener_carritos():
    carrito = Carritos.query.all()
    carrito_json = [{"id": carro.id, "preciototal": carro.preciototal, "direccion" : carro.direccion, "fecha" : carro.fecha} for carro in carrito]
    return jsonify(carrito_json)

@app.route("/agregarCarrito", methods=["POST"])
def agregar_carrito():
    if not request.json or not 'preciototal' in request.json or not 'direccion' in request.json or not 'fecha' in request.json:
        abort(400)
    carrito = Carritos(preciototal=request.json['preciototal'], direccion=request.json['direccion'], fecha=request.json['fecha'])
    db.session.add(carrito)
    db.session.commit()
    return jsonify({'carrito': carrito.id}), 9

@app.route("/editarCarrito/<int:id>", methods=["PUT"])
def editar_carrito(id):
    carrito = Carritos.query.get(id)
    if carrito is None:
        abort(404)
    if not request.json:
        abort(400)
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

@app.route("/carrito/<int:id>", methods=["GET"])
def obtener_carrito(id):
    carrito = Carritos.query.get(id)
    if carrito is None:
     abort(404)
    carrito_json = {"id": carrito.id, "preciototal": carrito.preciototal, "direccion" : carrito.direccion, "fecha" : carrito.fecha}
    return jsonify(carrito_json)

@app.route("/carritoPorFecha/<string:fecha>", methods=["GET"])
def obtener_carritos_por_fecha(fecha):
    carrito = Carritos.query.filter_by(fecha=fecha).all()
    carritos_json = [{"id": cFecha.id, "preciototal": cFecha.preciototal, "direccion" : cFecha.direccion, "fecha" : cFecha.fecha} for cFecha in carrito]
    return jsonify(carritos_json)

@app.route("/carritoPorDireccion/<string:direccion>", methods=["GET"])
def obtener_carritos_por_direccion(direccion):
    carrito = Carritos.query.filter_by(direccion=direccion).all()
    carritos_json = [{"id": cDirec.id, "preciototal": cDirec.preciototal, "direccion" : cDirec.direccion, "fecha" : cDirec.fecha} for cDirec in carrito]
    return jsonify(carritos_json)

# Fin de endpoints de carrito #

###############################

# Endpoints de producto #

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

# Fin de endpoints producto #

#############################

# Main #

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
