from application.database import db


class Colour(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    cars = db.relationship('Car', backref='colour')

    def save_to_db(self) :
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) :
        db.session.delete(self)
        db.session.commit()


class Car(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(20))
    model = db.Column(db.String(20))
    build_date = db.Column(db.DateTime)
    colour_id = db.Column(db.Integer, db.ForeignKey('colour.id'))

    def save_to_db(self) :
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) :
        db.session.delete(self)
        db.session.commit()