from smartcar_api import *
from gm_api import *
import unittest
from unittest.mock import Mock, patch


from nose.tools import assert_true, assert_list_equal, assert_is_not_none
import requests


# Response.ok
# (Bool) True if no errors occurred during the request, and the status_code is kosher.
# If you invoke .raise_for_status(), an HTTPError will be raised for certain status codes. If the status code indicates a successful request, the program will proceed without that exception being raised.

# RUN IN TERMINAL: nosetests --verbosity=2 testing.py

# class Test_GM_Status_Code(unittest.TestCase):

#     GM_API_URL = "http://gmapi.azurewebsites.net"

#     GM_endpoints = ["getVehicleInfoService", "getSecurityStatusService", "getEnergyService", "actionEngineService"]


#     def test_status_code(self):

#         response = requests.get(f"{GM_API_URL}/getSecurityStatusService")
        

#         try:
#             assert_true(response.status_code == 200)
#             response.raise_for_status()

#         except HTTPError as http_err:
#             print(f'HTTP error occurred: {http_err}') 

#     def test_request_response(self):

#         response = requests.get(f"{GM_API_URL}/getSecurityStatusService")

#         try:
#             assert_is_not_none(response)
#         except:
#             print("No response.")

# @patch('gm_api.requests.get')
# def test_status_code(mock_get):

#     mock_get.return_value.ok = True

#     response = requests.get(f"{GM_API_URL}/getSecurityStatusService")

#     assert_is_not_none(response)


class TestGMAPIs(object):
    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = patch('gm_api.requests.get')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()

    def test_GM_status_code(self):

        self.mock_get.return_value.ok = True

        self.mock_get.return_value = Mock()
        
        self.mock_get.return_value.json.return_value = data

        # Call the service, which will send a request to the server.
        response = gm_get_vehicle_info('1234')

        # If the request is sent successfully, then I expect a response to be returned.
        assert_equal(response.json(), data)

    # def test_getting_todos_when_response_is_not_ok(self):
    #     # Configure the mock to not return a response with an OK status code.
    #     self.mock_get.return_value.ok = False

    #     # Call the service, which will send a request to the server.
    #     response = get_todos()

    #     # If the response contains an error, I should get no todos.
    #     assert_is_none(response)




if __name__ == '__main__':
    unittest.main()


