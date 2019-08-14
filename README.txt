README

The tasks are as follows:

-Implement the Smartcar spec by making HTTP requests to the GM API
-Implement the Smartcar API specification using any frameworks or libraries as necessary
-Provide tests for your API implementation
-Write your code to be well structured and documented

Client --> request => Smartcar API --> request => GM API

The general workflow is as follows:
RESTful API that is used to store users details, which will have CRUD (Create, Read, Update, Delete) functions, allowing us to create new user, get details of existing user, update details of existing user and delete existing user.

The following endpoints:
1. Vehicle info
    -GET /vehicles/:id
2. Security 
    -GET /vehicles/:id/doors
3. Fuel range
    -GET /vehicles/:id/fuel
4. Battery range
    -GET /vehicles/:id/battery
5. Start/Stop Engine
    -POST /vehicles/:id/engine
    Content-Type: application/json
    {
        "action": "START|STOP"
    }


File structure:

constants.py
-This houses all the constants including the relevent Smartcar URLs, URI and API keys.
-To ensure privacy and discourage unwarranted use of the Smartcar API, the API keys are hidden as environment variables.

server.py
-This contains code only relating to the server.

views.py
-This file contains all the routing.

smartcar_utils.py
-This file handles all the requests.


Last problem:
Post because it was more difficult to test and was more involved because it required a request body
look at reqparse 
learning how to use flask restful 


What I learned:
Ternary operator

Enhancements:
Instead of creating a function for each GM API call, make a general one that takes in the unique params; much of the code is repeated 



Testing:
Unit testing
End to end testing
Integration testing







