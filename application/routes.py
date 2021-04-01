import datetime

from flask import jsonify, request

from application import app
from application.databaseFunctions import get_car_json_data, add_new_car
from application.models import Car, Colour
from application.schema import cars_schema, car_schema


@app.route('/cars', methods=['GET'])
def cars() :
    cars_list = Car.query.all()
    result = cars_schema.dump(cars_list)
    return jsonify(result)


@app.route('/car/<int:car_id>', methods=["GET"])
def car_details(car_id: int) :
    car = Car.query.filter_by(id=car_id).first()
    if car :
        result = car_schema.dump(car)
        return jsonify(result)
    else :
        return jsonify(message="That car does not exists"), 404


@app.route('/car', methods=['POST'])
def add_car() :
    data = request.json

    if get_car_json_data(data):
        car_build_date, car_colour, car_make, car_model = get_car_json_data(data)
        colour = Colour.query.filter_by(name=car_colour).first()

        if car_build_date > (datetime.date.today() - datetime.timedelta(weeks=208)) :
            if colour :
                add_new_car(car_build_date, car_make, car_model, colour)
                return jsonify(message="You submitted a new car"), 201

            else :
                return jsonify(message="This colour doesn't exist"), 404

        else :
            return jsonify(message="This car is too old"), 406
    else:
        return jsonify(message="Incorrect Json"), 400


@app.route('/cars/<int:car_id>', methods=['DELETE'])
def remove_car(car_id: int) :
    car = Car.query.filter_by(id=car_id).first()
    if car :
        car.delete_from_db()
        return jsonify(message="You deleted a car"), 202
    else :
        return jsonify(message="This car does not exist"), 404
