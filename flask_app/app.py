from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/afrin/assignments/python/integration_test/flask_app/mydb.db'
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "connect_args": {"check_same_thread": False}
}
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


@app.route('/products', methods=['POST'])
def create_product():
    product = request.json
    if isinstance(product, list):
        products = []
        for p in product:
            new_product = Product(name=p['name'], price=p['price'])
            db.session.add(new_product)
            products.append(new_product)
        db.session.commit()
        return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products]), 201
    else:
        new_product = Product(name=product['name'], price=product['price'])
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'id': new_product.id, 'name': new_product.name, 'price': new_product.price}), 201
@app.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products])

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = db.session.get(Product, product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price})

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = db.session.get(Product, product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    product.name = request.json['name']
    product.price = request.json['price']
    db.session.commit()
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price})

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = db.session.get(Product, product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({}), 204

@app.route('/orders', methods=['POST'])
def create_order():
    order = request.json
    new_order = Order(product_id=order['product_id'], quantity=order['quantity'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'id': new_order.id, 'product_id': new_order.product_id, 'quantity': new_order.quantity}), 201

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    if order is None:
        return jsonify({'error': 'Order not found'}), 404
    return jsonify({'id': order.id, 'product_id': order.product_id, 'quantity': order.quantity})

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = Order.query.get(order_id)
    if order is None:
        return jsonify({'error': 'Order not found'}), 404
    order.product_id = request.json['product_id']
    order.quantity = request.json['quantity']
    db.session.commit()
    return jsonify({'id': order.id, 'product_id': order.product_id, 'quantity': order.quantity})

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if order is None:
        return jsonify({'error': 'Order not found'}), 404
    db.session.delete(order)
    db.session.commit()
    return jsonify({}), 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, use_reloader=False)
