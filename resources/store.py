from flask_restful import Resource
from models.store import StoreModel

# ini gunanya untuk extend Resource class
# cara kita extend itu dengan masukin nama class didalam parenthesis


class Store(Resource):
    # karena store yang punya primary, kalo kita update namanya, bisa error

    # get method ini return a specific store
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'ga ada tokonya, boss !'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "toko '{}' udah terdaftar !".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            {'message': "udah ada toko dengan nama tersebut !"}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': "the store has been deleted !"}


class StoreList(Resource):
    def get(self):
        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
