import unittest
from nose.tools import assert_true, assert_is_not_none, assert_equal
import requests

# PRIOR TO RUNNING testing.py: python3 server.py
# RUN IN TERMINAL: nosetests --verbosity=2 testing.py

# Constants
SMARTCAR_API = "http://localhost:5000/vehicles"
INVALID_ID = f"{SMARTCAR_API}/0000"
VALID_ID = f"{SMARTCAR_API}/1234"
ALT_VALID_ID = f"{SMARTCAR_API}/1235"


class TestSmartcarAPI(unittest.TestCase):
    def test_valid_vehicle_info(self):
        response = requests.get(f"{VALID_ID}")
        jsonified = response.json()
        assert_true(response.status_code == 200)
        assert_is_not_none(response)
        assert_equal(jsonified["vin"], "123123412412")

    def test_invalid_vehicle_info(self):
        response = requests.get(f"{INVALID_ID}")
        jsonified = response.json()
        assert_true(response.status_code == 404)
        assert_equal(jsonified["status"], "404")

    def test_valid_vehicle_doors(self):
        response = requests.get(f"{VALID_ID}/doors")
        jsonified = response.json()
        assert_true(response.status_code == 200)
        assert_is_not_none(response)
        assert_true(jsonified[0]["location"],
                    "frontLeft" or "frontRight" or
                    "backLeft" or "backRight")

    def test_invalid_vehicle_doors(self):
        response = requests.get(f"{INVALID_ID}")
        jsonified = response.json()
        assert_true(response.status_code == 404)
        assert_equal(jsonified["status"], "404")

    def test_valid_vehicle_fuel(self):
        response = requests.get(f"{ALT_VALID_ID}/fuel")
        jsonified = response.json()
        assert_true(response.status_code == 200)
        assert_is_not_none(response)
        assert_equal(jsonified["percent"], "null")

    def test_invalid_vehicle_fuel(self):
        response = requests.get(f"{INVALID_ID}/fuel")
        jsonified = response.json()
        assert_true(response.status_code == 404)
        assert_equal(jsonified["status"], "404")

    def test_valid_vehicle_battery(self):
        response = requests.get(f"{VALID_ID}/battery")
        jsonified = response.json()
        assert_true(response.status_code == 200)
        assert_is_not_none(response)
        assert_equal(jsonified["percent"], "null")

    def test_invalid_vehicle_battery(self):
        response = requests.get(f"{INVALID_ID}/battery")
        jsonified = response.json()
        assert_true(response.status_code == 404)
        assert_equal(jsonified["status"], "404")

    def test_valid_vehicle_engine(self):
        response = requests.post(f"{VALID_ID}/engine",
                                 data={"action": "START"})
        jsonified = response.json()
        assert_true(response.status_code == 200)
        assert_is_not_none(response)
        assert_true(jsonified["status"], "success" or "error")

    def test_invalid_vehicle_engine(self):
        response = requests.post(f"{INVALID_ID}/engine",
                                 data={"action": "HELLO"})
        jsonified = response.json()
        assert_true(response.status_code == 404)
        assert_equal(jsonified["status"], "404")


if __name__ == '__main__':
    unittest.main()
