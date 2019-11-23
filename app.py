from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity

from resources.item import Item, ItemList
from resources.user import UserRegister
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# kita bikin jadi false supaya ga nabrak sama yang udah ada.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "jose"
api = Api(app)

# ini function kita pake supaya kita ga perlu running create_tables.py
# command di terminal secara manual terus
@app.before_first_request
def create_tables():
    db.create_all()


# untuk process authentication app.py kita
jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

# kalo kita run app.py kita, baru flask app ini dijalanin
# kalo kita run misalnya file lain, yang ini ga dijalanin
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
