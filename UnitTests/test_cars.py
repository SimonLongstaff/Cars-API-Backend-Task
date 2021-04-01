import json
import unittest

import app

BASE_URL = "http://127.0.0.1:5000"


class TestFlaskApi(unittest.TestCase) :

    def setUp(self) :
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_all(self) :
        response = self.app.get(BASE_URL + '/cars')
        self.assertEqual(200, response.status_code)

    def test_get_car_failure(self) :
        response = self.app.get(BASE_URL + '/car/999999')
        self.assertEqual(404, response.status_code)

        exp_resp = '{"message": "That car does not exists"}'
        resp_json = json.loads(exp_resp)
        self.assertEqual(resp_json, response.json)

    def test_insert_car_correct(self) :
        car = '{ "car_make" : "Nissan", "car_model" : "Skyline GT-R", "car_build_year" : "2020", "car_build_month" : ' \
              '"1", "car_build_day" : "3", "car_colour" : "black" } '

        exp_resp = '{"message" : "You submitted a new car"}'

        car_json = json.loads(car)
        resp_json = json.loads(exp_resp)

        response = self.app.post(BASE_URL + '/car', json=car_json)
        self.assertEqual(201, response.status_code)
        self.assertEqual(resp_json, response.json)

    def test_insert_car_incorrect(self) :
        car = '{ "nonsenseJson" : "garbageData" } '

        exp_resp = '{"message": "Incorrect Json"}'

        car_json = json.loads(car)
        resp_json = json.loads(exp_resp)

        response = self.app.post(BASE_URL + '/car', json=car_json)
        self.assertEqual(400, response.status_code)
        self.assertEqual(resp_json, response.json)

    def test_inset_car_too_old(self) :
        car = '{ "car_make" : "Toyota ", "car_model" : "Sprinter Trueno AE86", "car_build_year" : "1984", ' \
              '"car_build_month" : "1", "car_build_day" : "3", "car_colour" : "white" } '
        exp_resp = '{"message": "This car is too old"}'

        car_json = json.loads(car)
        resp_json = json.loads(exp_resp)

        response = self.app.post(BASE_URL + '/car', json=car_json)
        self.assertEqual(406, response.status_code)
        self.assertEqual(resp_json, response.json)

    def test_insert_car_wrong_colour(self) :
        car = '{ "car_make" : "Mazda ", "car_model" : "RX-7 Twin-Turbo", "car_build_year" : "2020", "car_build_month" : ' \
              '"1", "car_build_day" : "3", "car_colour" : "yellow" } '
        exp_resp = '{ "message": "This colour doesn\'t exist"}'

        car_json = json.loads(car)
        resp_json = json.loads(exp_resp)

        response = self.app.post(BASE_URL + '/car', json=car_json)
        self.assertEqual(404, response.status_code)
        self.assertEqual(resp_json, response.json)

    # A problem with this test is that it only passes after one failed run on an empty database
    # Obviously because it's got nothing to delete until the insertion test has ran
    # I'm tentatively aware that there are a few workaround but since you set a limit of two hours I
    # decided not to spend time on this particular problem.
    def test_delete(self) :
        exp_suc_resp = '{"message" : "You deleted a car"}'
        exp_fail_resp = '{"message": "This car does not exist"}'

        suc_json = json.loads(exp_suc_resp)
        fail_json = json.loads(exp_fail_resp)

        response = self.app.delete(BASE_URL + '/cars/1')
        self.assertEqual(202, response.status_code)
        self.assertEqual(suc_json, response.json)

        response = self.app.delete(BASE_URL + '/cars/999999')
        self.assertEqual(404, response.status_code)
        self.assertEqual(fail_json, response.json)
