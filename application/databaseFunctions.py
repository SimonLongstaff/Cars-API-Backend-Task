import datetime

from application.models import Car, Colour


def get_car_json_data(data) :
    try:
        car_make = data['car_make']
        car_model = data['car_model']
        car_build_year = int(data['car_build_year'])
        car_build_month = int(data['car_build_month'])
        car_build_day = int(data['car_build_day'])
        car_colour = data['car_colour'].lower()
        car_build_date = datetime.date(car_build_year, car_build_month, car_build_day)
        return car_build_date, car_colour, car_make, car_model
    except KeyError:
        return None


def add_new_car(car_build_date, car_make, car_model, colour) :
    new_car = Car(make=car_make,
                  model=car_model,
                  build_date=car_build_date,
                  colour=colour)
    new_car.save_to_db()


def insert_base_colours() :
    red = Colour(name='red').save_to_db()
    blue = Colour(name='blue').save_to_db()
    white = Colour(name='white').save_to_db()
    black = Colour(name='black').save_to_db()