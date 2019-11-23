from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # ini dinamain store karena 1 store bisa punya banyak items
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    # kita mau extract some of the get method code dan isi di method baru
    # kita buat method ini untuk nampung code yang ga berhubungan langsung dengan get method
    # class method ini bakalan banyak dipanggil di method lain
    @classmethod
    def find_by_name(cls, name):
        # ini perintah untuk select * from items where name=name
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
