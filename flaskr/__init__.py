from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os 

# Init App
app = Flask(__name__)

from flaskr import config

# Init db
db = SQLAlchemy(app)

#Init Ma
ma = Marshmallow(app)


from flaskr import route


# RUN SERVER
if __name__ == '__main__':
	app.run(debug=True)
