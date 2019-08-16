from smartcar_api import *
import unittest
from unittest.mock import Mock, patch
from nose.tools import assert_true, assert_list_equal, assert_is_not_none
import requests

from smartcar_api import app

# PRIOR TO RUNNING testing.py: python3 server.py 
# RUN IN TERMINAL: nosetests --verbosity=2 testing.py


# TODO: do json validation to make sure the output is correct, put coverage % in README
# Example: battery sometimes gives null so test for that edge case
# To look up: how to test post?


SMARTCAR_API = "http://localhost:5000/vehicles"
INVALID_ID = f"{SMARTCAR_API}/0000"
VALID_ID = f"{SMARTCAR_API}/1234"

class TestSmartcarAPI(unittest.TestCase):

    def test_valid_vehicle_info(self):

        response = requests.get(f"{VALID_ID}")

        try:
            assert_true(response.status_code == 200)
            assert_is_not_none(response)
            response.raise_for_status()

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 

    def test_invalid_vehicle_info(self):

       response = requests.get(f"{INVALID_ID}")

        try:
            assert_true(response.status_code == 404)
            assert_is_not_none(response)    # assert is none? or just error code?
            response.raise_for_status()

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 


    def test_valid_vehicle_doors():

            response = requests.get(f"{VALID_ID/doors}")

        try:
            assert_true(response.status_code == 200)
            assert_is_not_none(response)
            response.raise_for_status()

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 


    def test_invalid_vehicle_doors():

       response = requests.get(f"{INVALID_ID}")

        try:
            assert_true(response.status_code == 404)
            assert_is_not_none(response)    # assert is none? or just error code?
            response.raise_for_status()

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 

    def test_valid_vehicle_fuel():

        response = requests.get(f"{VALID_ID/fuel}")

        try:
            assert_true(response.status_code == 200)
            assert_is_not_none(response)
            response.raise_for_status()

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 


    def test_invalid_vehicle_fuel():


       response = requests.get(f"{INVALID_ID}/fuel")

        try:
            assert_true(response.status_code == 404)
            assert_is_not_none(response)    # assert is none? or just error code?
            response.raise_for_status()

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 

    def test_valid_vehicle_battery():

        response = requests.get(f"{VALID_ID/battery}")

        try:
            assert_true(response.status_code == 200)
            assert_is_not_none(response)
            response.raise_for_status()

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 


    def test_invalid_vehicle_battery():


       response = requests.get(f"{INVALID_ID}/battery")

        try:
            assert_true(response.status_code == 404)
            assert_is_not_none(response)    # assert is none? or just error code?
            response.raise_for_status()

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 


    def test_valid_vehicle_engine():

        response = requests.get(f"{VALID_ID/engine}")

        try:
            assert_true(response.status_code == 200)
            assert_is_not_none(response)
            response.raise_for_status()

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 


    def test_invalid_vehicle_engine():


       response = requests.get(f"{INVALID_ID}/engine")

        try:
            assert_true(response.status_code == 404)
            assert_is_not_none(response)    # assert is none? or just error code?
            response.raise_for_status()

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 



# @patch('gm_api.requests.get')
# def test_status_code(mock_get):

#     mock_get.return_value.ok = True

#     response = requests.get(f"{GM_API_URL}/getSecurityStatusService")

#     assert_is_not_none(response)


# class TestGMAPIs(object):
#     @classmethod
#     def setup_class(cls):
#         cls.mock_get_patcher = patch('gm_api.requests.get')
#         cls.mock_get = cls.mock_get_patcher.start()

#     @classmethod
#     def teardown_class(cls):
#         cls.mock_get_patcher.stop()

#     def test_GM_status_code(self):

#         self.mock_get.return_value.ok = True

#         self.mock_get.return_value = Mock()

#         self.mock_get.return_value.json.return_value = data

#         # Call the service, which will send a request to the server.
#         response = gm_get_vehicle_info('1234')

#         # If the request is sent successfully, then I expect a response to be returned.
#         assert_is_not_none(response)

    # def test_getting_todos_when_response_is_not_ok(self):
    #     # Configure the mock to not return a response with an OK status code.
    #     self.mock_get.return_value.ok = False

    #     # Call the service, which will send a request to the server.
    #     response = get_todos()

    #     # If the response contains an error, I should get no todos.
    #     assert_is_none(response)




# class TestSmartcarAPI(unittest.TestCase):

#     # def setUp(self):
#     #     self.backup_items = deepcopy(app.items)  # no references!
#     #     self.app = app.app.test_client()
#     #     self.app.testing = True

#     def test_get_all(self):
#         response = self.app.get(BASE_URL)
#         data = json.loads(response.get_data())
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(data['items']), 3)

#     def test_get_one(self):
#         response = self.app.get(BASE_URL)
#         data = json.loads(response.get_data())
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(data['items'][0]['name'], 'laptop')

#     def test_item_not_exist(self):
#         response = self.app.get(BAD_ITEM_URL)
#         self.assertEqual(response.status_code, 404)

#     def test_post(self):
#         # missing value field = bad
#         item = {"name": "some_item"}
#         response = self.app.post(BASE_URL,
#                                  data=json.dumps(item),
#                                  content_type='application/json')
#         self.assertEqual(response.status_code, 400)
#         # value field cannot take str
#         item = {"name": "screen", "value": 'string'}
#         response = self.app.post(BASE_URL,
#                                  data=json.dumps(item),
#                                  content_type='application/json')
#         self.assertEqual(response.status_code, 400)
#         # valid: both required fields, value takes int
#         item = {"name": "screen", "value": 200}
#         response = self.app.post(BASE_URL,
#                                  data=json.dumps(item),
#                                  content_type='application/json')
#         self.assertEqual(response.status_code, 201)
#         data = json.loads(response.get_data())
#         self.assertEqual(data['item']['id'], 4)
#         self.assertEqual(data['item']['name'], 'screen')
#         # cannot add item with same name again
#         item = {"name": "screen", "value": 200}
#         response = self.app.post(BASE_URL,
#                                  data=json.dumps(item),
#                                  content_type='application/json')
#         self.assertEqual(response.status_code, 400)

   
#     def tearDown(self):
#         # reset app.items to initial state
#         app.items = self.backup_items





if __name__ == '__main__':
    unittest.main()


