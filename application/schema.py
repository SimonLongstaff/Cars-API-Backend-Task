from flask_marshmallow import Marshmallow

ma = Marshmallow()


class CarSchema(ma.Schema) :
    class Meta :
        fields = ('id', 'make', 'model', 'build_date', 'colour.name')


car_schema = CarSchema()
cars_schema = CarSchema(many=True)
