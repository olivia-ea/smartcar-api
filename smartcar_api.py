from flask import Flask
from flask_restful import Api, Resource, reqparse
import json
from gm_api import *
from logger_util import logger


app = Flask(__name__)
api = Api(app)
app.debug = True


# Smartcar API endpoints
class VehicleID(Resource):
    def get(self, id):
        vehicle = gm_get_vehicle_info(id)
        jsonified = json.loads(vehicle)

        if jsonified["status"] == "200":
            smartcar_response = {
                    "vin": (jsonified
                            ["data"]["vin"]["value"]),
                    "color": (jsonified
                              ["data"]["color"]["value"]),
                    "doorCount": (4
                                  if (jsonified
                                      ["data"]["fourDoorSedan"]["value"]
                                      == 'True')
                                  else 2),
                    "driveTrain": (jsonified
                                   ["data"]["driveTrain"]["value"])
                   }
            logger.info(f"Request with id: {id}: \n{smartcar_response}")
            return smartcar_response, 200

        if jsonified["status"] == "404":
            logger.error(f"Request with id: {id}: \n{jsonified}")
            return jsonified, 404
        else:
            # Catch all case
            logger.critical(f"Unexpected response from GM API")
            return "Critical Error: Unexpected response from GM API", 404


api.add_resource(VehicleID, "/vehicles/<string:id>")


class Security(Resource):
    def get(self, id):
        vehicle = gm_get_security_info(id)
        jsonified = json.loads(vehicle)

        if jsonified["status"] == "200":
            try:
                smartcar_response = [
                        {
                          "location": (jsonified
                                       ["data"]["doors"]["values"][1]
                                       ["location"]["value"]),
                          "locked": (True
                                     if (jsonified
                                         ["data"]["doors"]["values"][1]
                                         ["locked"]["value"]
                                         == 'True')
                                     else False)
                        },
                        {
                          "location": (jsonified
                                       ["data"]["doors"]["values"][0]
                                       ["location"]["value"]),
                          "locked": (True
                                     if (jsonified
                                         ["data"]["doors"]["values"][0]
                                         ["locked"]["value"]
                                         == 'True')
                                     else False)
                        }
                    ]

            except:
                pass
            try:
                smartcar_response = [
                        {
                          "location": (jsonified
                                       ["data"]["doors"]["values"][1]
                                       ["location"]["value"]),
                          "locked": (True
                                     if (jsonified
                                         ["data"]["doors"]["values"][1]
                                         ["locked"]["value"]
                                         == 'True')
                                     else False)
                        },
                        {
                          "location": (jsonified
                                       ["data"]["doors"]["values"][0]
                                       ["location"]["value"]),
                          "locked": (True
                                     if (jsonified
                                         ["data"]["doors"]["values"][0]
                                         ["locked"]["value"]
                                         == 'True')
                                     else False)
                        },
                        {
                          "location": (jsonified
                                       ["data"]["doors"]["values"][2]
                                       ["location"]["value"]),
                          "locked": (True
                                     if (jsonified
                                         ["data"]["doors"]["values"][2]
                                         ["locked"]["value"]
                                         == 'True')
                                     else False)
                        },
                        {
                          "location": (jsonified
                                       ["data"]["doors"]["values"][3]
                                       ["location"]["value"]),
                          "locked": (True
                                     if (jsonified
                                         ["data"]["doors"]["values"][3]
                                         ["locked"]["value"]
                                         == 'True')
                                     else False)
                        }
                    ]
            except:
                pass
            finally:
                logger.info(f"Request with id: {id}: \n{smartcar_response}")
                return smartcar_response, 200

        if jsonified["status"] == "404":
            logger.error(f"Request with id: {id}: \n{jsonified}")
            return jsonified, 404
        else:
            # Catch all case
            logger.critical(f"Unexpected response from GM API")
            return "Critical Error: Unexpected response from GM API", 404


api.add_resource(Security, "/vehicles/<string:id>/doors")


class FuelService(Resource):
    def get(self, id):
        vehicle = gm_get_fuel_battery_level(id)
        jsonified = json.loads(vehicle)

        if jsonified["status"] == "200":
            smartcar_response = {
                    "percent": (float(jsonified
                                ["data"]["tankLevel"]["value"])
                                if (jsonified
                                    ["data"]["tankLevel"]["value"]
                                    != "null")
                                else "null")
                    }
            logger.info(f"Request with id: {id}: \n{smartcar_response}")
            return smartcar_response, 200

        if jsonified["status"] == "404":
            logger.error(f"Request with id: {id}: \n{jsonified}")
            return jsonified, 404
        else:
            # Catch all case
            logger.critical(f"Unexpected response from GM API")
            return "Critical Error: Unexpected response from GM API", 404


api.add_resource(FuelService, "/vehicles/<string:id>/fuel")


class EnergyService(Resource):
    def get(self, id):
        vehicle = gm_get_fuel_battery_level(id)
        jsonified = json.loads(vehicle)

        if jsonified["status"] == "200":
            smartcar_response = {
                    "percent": (float(jsonified
                                      ["data"]["batteryLevel"]["value"])
                                if (jsonified
                                    ["data"]["batteryLevel"]["value"]
                                    != "null")
                                else "null")
                    }
            logger.info(f"Request with id: {id}: \n{smartcar_response}")
            return smartcar_response, 200

        if jsonified["status"] == "404":
            logger.error(f"Request with id: {id}: \n{jsonified}")
            return jsonified, 404
        else:
            # Catch all case
            logger.critical(f"Unexpected response from GM API")
            return "Critical Error: Unexpected response from GM API", 404


api.add_resource(EnergyService, "/vehicles/<string:id>/battery")


class EngineService(Resource):
    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("action")
        args = parser.parse_args()
        cmd = ""

        if args["action"] == "START":
            cmd = "START_VEHICLE"

        if args["action"] == "STOP":
            cmd = "STOP_VEHICLE"

        vehicle = gm_start_stop_engine(id, cmd)
        jsonified = json.loads(vehicle)

        if jsonified["status"] == "200":
            logger.info(f"Request with id: {id}: \n{jsonified}")
            status = ""

            if jsonified["actionResult"]["status"] == "EXECUTED":
                status = "success"

            if jsonified["actionResult"]["status"] == "FAILED":
                status = "error"
            return {
                    "status": status
                    }, 200
        if jsonified["status"] == "404":
            logger.error(f"Request with id: {id}: \n{jsonified}")
            return jsonified, 404
        else:
            # Catch all case
            logger.critical(f"Unexpected response from GM API")
            return "Critical Error: Unexpected response from GM API", 404


api.add_resource(EngineService, "/vehicles/<string:id>/engine")
