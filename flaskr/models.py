from flaskr import db, ma

# Class/Model 
class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), unique=True) 
	description = db.Column(db.String(240))
	quantity = db.Column(db.Integer)
	cost = db.Column(db.Float)

	def __init__(self, name, description, quantity, cost):
		self.name = name
		self.description = description
		self.quantity = quantity
		self.cost = cost

	# def __repr__(self):
	# 	return "Product Name: " + self.name


# Product Schema
class ProductSchema(ma.Schema):
	class Meta:
		fields = ( 'id', 'name', 'description' , 'quantity', 'cost')


# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
