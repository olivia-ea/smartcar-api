# Smartcar API Challenge

## Table of Contents
* [Tasks](#tasks)
* [Tech Stack](#tech-stack) 
* [Setting Up/Installation](#installation)
* [Files Explained](#files-explained)
* [How Handle the Post Request](#post-request)
* [Testing](#testing)
* [Personal](#personal)

## Tasks
* Implement the Smartcar spec by making HTTP requests to the GM API.
* Implement the Smartcar API specification using any frameworks or libraries as necessary.
* Provide tests for your API implementation.
* Write your code to be well structured and documented.

Desired workflow: 
Client --> request => Smartcar API --> request => GM API

## Tech Stack
* Backend: Python, Flask
* APIs: GM API

## Installation 

To run the Smartcar API on your local computer, follow these steps:

Clone repository: 
```
$ git clone https://github.com/olivia-ea/smartcar-api.git
```

Set up virtual environment: 

```
$ virtualenv venv
```

Activate virtual envirnoment:
```
$ source venv/bin/activate
```

Install dependencies:
```
$ pip3 install -r requirements.txt
```

Run from the command line:
```
$ python3 server.py
```

Open localhost:5000 on browser. 


## Files Explained
### server.py
* This file contains code only relating to the Smartcar server.

### gm_api.py
* This file contains the all the GM functions that makes HTTP post requests to the GM API (http://gmapi.azurewebsites.net). 
* The functions return the contents of the response object.
* The functions hit the following endpoints: 
    * /getVehicleInfoService
    * /getSecurityStatusService
    * /getEnergyService
    * /actionEngineService  

### smartcar_api.py
* This file constructs all the Smartcar API endpoints using the flask_restful library. 
* When each Smartcar endpoint is hit, the request runs the respective get/post request by first making an API call to the GM API then casting the response into json. The return statement then parses through the json to give the desired Smartcar format. 

### testing.py
* Contains unit testing for above files. There is an individual function to test each Smartcar API endpoint using assert statements. The valid id tests are checking for a 200 status code and if a response is present whereas the invalid id tests are checking for a 404 status code.

## Post Request

Use Postman to access the post request for the Smartcar API. 

1. Run the Smartcar server

```
$ python3 server.py
```

2. Select "Post" request and enter 'http://localhost:5000/vehicles/1234/engine'
3. Select headers and for key put 'Content-Type' and for value put 'application/json'
4. Select body and for key put 'action' and for value put 'START' or 'STOP'
5. Press send

## Testing

In order to run the unit tests in the testing.py file, first run the Smartcar server and then the nosetest.

```
$ python3 server.py
```

```
$ nosetests --verbosity=2 testing.py
```

## Personal 

### Major challenges
Building the last Smartcar endpoint was the most challenging because it was a post request which was more involved than the previous endpoints that just required get requests. It was also more difficult to test because it required a request body for the START/STOP commands. I was able to solve this problem by using the reqparse library that enabled me to add an "action" argument. Essentially, the reqparse created a parser that added the "action" argument to the parser and stored the parse arguement in a variable.  From there, I was able to build out the endpoint that returned "success" if executed and "error" if failed. 


### New things I learned:
* Ternary operators.
* Using the flask_restful library to build out endpoints.


### Future enhancements:
* Use a different tool instead of reqparser because it is going to be obsolete.
* It's good practices to have a constants.py file to store all constant URLs. However, it felt unnecessary because there was only one (GM_API_URL = 'http://gmapi.azurewebsites.net').
* Use mocking for testing to avoid having to run the server to execute the tests.






