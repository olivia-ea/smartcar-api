import unittest
from nose.tools import assert_true, assert_is_not_none
import requests

# PRIOR TO RUNNING testing.py: python3 server.py 
# RUN IN TERMINAL: nosetests --verbosity=2 testing.py

# Constants
SMARTCAR_API = "http://localhost:5000/vehicles"
INVALID_ID = f"{SMARTCAR_API}/0000"
VALID_ID = f"{SMARTCAR_API}/1234"

class TestSmartcarAPI(unittest.TestCase):
    def test_valid_vehicle_info(self):
        response = requests.get(f"{VALID_ID}")

        assert_true(response.status_code == 200)
        assert_is_not_none(response)


    def test_invalid_vehicle_info(self):
        response = requests.get(f"{INVALID_ID}")
        
        assert_true(response.status_code == 404)


    def test_valid_vehicle_doors(self):
        response = requests.get(f"{VALID_ID}/doors")

        assert_true(response.status_code == 200)
        assert_is_not_none(response)


    def test_invalid_vehicle_doors(self):
        response = requests.get(f"{INVALID_ID}")

        assert_true(response.status_code == 404)
        

    def test_valid_vehicle_fuel(self):
        response = requests.get(f"{VALID_ID}/fuel")

        assert_true(response.status_code == 200)
        assert_is_not_none(response)
           

    def test_invalid_vehicle_fuel(self):
        response = requests.get(f"{INVALID_ID}/fuel")
       
        assert_true(response.status_code == 404)


    def test_valid_vehicle_battery(self):
        response = requests.get(f"{VALID_ID}/battery")

        assert_true(response.status_code == 200)
        assert_is_not_none(response)
       

    def test_invalid_vehicle_battery(self):
        response = requests.get(f"{INVALID_ID}/battery")
       
        assert_true(response.status_code == 404)


    def test_valid_vehicle_engine(self):
        response = requests.post(f"{VALID_ID}/engine", data = {"action": "START"})

        assert_true(response.status_code == 200)
        assert_is_not_none(response)
        

    def test_invalid_vehicle_engine(self):
        response = requests.post(f"{VALID_ID}/engine", data = {"action": "HELLO"})

        assert_true(response.status_code == 404)
          

if __name__ == '__main__':
    unittest.main()


