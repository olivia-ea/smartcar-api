README.txt

The tasks are as follows:
-Implement the Smartcar spec by making HTTP requests to the GM API
-Implement the Smartcar API specification using any frameworks or libraries as necessary
-Provide tests for your API implementation
-Write your code to be well structured and documented


Desired workflow: 
Client --> request => Smartcar API --> request => GM API


File structure:
server.py
-This file contains code only relating to the server.

gm_api.py
-This file contains the all the GM functions that makes HTTP post requests to the GM API (http://gmapi.azurewebsites.net). 
-The functions return the contents of the response object.
-The functions hit the following endpoints: 
    getVehicleInfoService
    getSecurityStatusService
    getEnergyService
    actionEngineService  

smartcar_api.py
-This file constructs all the Smartcar API endpoints using the flask_restful library. 
-When each Smartcar endpoint is hit, the request runs the respective get/post request by first making an API call to the GM API then casting the response into json. The return statement then parses through the json to give the desired Smartcar format. 


Major challenges
Building the last Smartcar endpoint was the most challenging because it was a post request. It was more difficult to test and was more involved because it required a request body. 


New things I learned:
Ternary operators
Using the flask_restful library to build out endpoints.


Future enhancements:
Instead of creating a function for each GM API call, make a general one that takes in the unique params as much of the code is repeated 
Use a different tool instead of reqparser because it is going to be obsolete.


Testing:
Unit testing







