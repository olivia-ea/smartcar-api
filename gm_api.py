import requests

GM_API_URL = 'http://gmapi.azurewebsites.net'

# Functions that fetch JSON from respective GM API endpoints
def gm_get_vehicle_info(id):

    url = f"{GM_API_URL}/getVehicleInfoService"
    data = {"id": id,"responseType": "JSON"}
    headers = {'Content-type': 'application/json'}
    response_data = requests.post(url, json=data, headers=headers)

    return response_data.text

def gm_get_security_info(id):

    url = f"{GM_API_URL}/getSecurityStatusService"
    data = {"id": id,"responseType": "JSON"}
    headers = {'Content-type': 'application/json'}
    response_data = requests.post(url, json=data, headers=headers)
    
    return response_data.text

def gm_get_fuel_battery_level(id):

    url = f"{GM_API_URL}/getEnergyService"
    data = {"id": id,"responseType": "JSON"}
    headers = {'Content-type': 'application/json'}
    response_data = requests.post(url, json=data, headers=headers)
    
    return response_data.text

def gm_start_stop_engine(id, command):

    url = f"{GM_API_URL}/actionEngineService"
    data = {"id": id, "command": command, "responseType": "JSON"}
    headers = {'Content-type': 'application/json'}
    response_data = requests.post(url, json=data, headers=headers)
    
    return response_data.text


