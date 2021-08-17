from flask import Flask, request, jsonify
from flaskr.models import Product, ProductSchema, product_schema, products_schema
from flaskr import app,db,ma

# GET ALL PRODUCTS
@app.route('/product', methods=['GET'])
def get_products():
	all_items = Product.query.all()
	result = products_schema.dump(all_items)
	return jsonify(result)


# GET SINGLE PRODUCT
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
	item = Product.query.get(id)
	return product_schema.jsonify(item)


# CREATE A PRODUCT
@app.route('/product', methods=['POST'])
def create():
	name = request.json['name']
	description = request.json['description']
	quantity = request.json['quantity']
	cost = request.json['cost']

	new_product = Product(name, description, quantity, cost)

	db.session.add(new_product)
	db.session.commit()

	return product_schema.jsonify(new_product)


# UPDATE A PRODUCT
@app.route('/product/<id>', methods=['PUT'])
def update(id):
	product = Product.query.get(id)

	product.name = request.json['name']
	product.description = request.json['description']
	product.quantity = request.json['quantity']
	product.cost = request.json['cost']

	db.session.commit()

	return product_schema.jsonify(product)


# DELETE A PRODUCT 
@app.route('/product/<id>', methods=['DELETE'])
def delete(id):
	product = Product.query.get(id)
	db.session.delete(product)
	db.session.commit()

	return product_schema.jsonify(product)
