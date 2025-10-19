# HBNB PART 2 - API / BUSINESS LOGIC / TESTING & DEBUGGING

## INTRODUCTION
In this part 2 of the HBNB project, we were asked to implement de business logic and API of our AirBNB-like application :
- Core business logic
- API endpoints
- Tests and validations with UNITTEST

The files in this repos will show you my work on thoses aspects, on the basis of the file organisation and some files contents (__init__ files, repository...) given by Holberton School.
Feel free to visit this repo if you want to take a look at this work basis : https://github.com/Holberton-Uy/hbnb-doc/tree/main/part2


## REQUIEREMENTS: 

The following instruction will help you to install this app on your computer. 

**System:**

This app was built from Ubuntu. 

**Cloning the repository:**

> git clone https://github.com/MathieuMjr/holbertonschool-hbnb.git

Don't forget to go in the proper directory before going further :

> cd part2/hbnb

**Virtual environnement**

Some modules requieres the creation of a virtual environement. Here are the steps to follow in order to install your virtual environnement. 

All the following commands must be executed from `part2/hbnb` directory


|Step | Command
|--|--|
|V env creation | `python3 -m venv venv`
|V env activation | `source venv/bin/activate`
|Modules installation | `pip -r requirements.txt` `VALIDER LA REDACTION DU REQUIEREMENTS.TXT`

\
You should have `(venv)` written at the very beginning of your line commands if it has been activated successfully. 

If you need to install on your own the required modules, here are the versions used :

|Module |Version
|--|--|
| Flask | 3.1.2
| Flask-restx | 1.3.2

## ARCHITECTURE DESIGN:
The project use the **facade pattern** :

API  -->  FACADE  -->  REPOSITORY/MODELS

API calls for facade function to fulfill requests. Facade functions orchestrate function calls to MODELS or REPOSITORY according to the requests. 

Repository methods are related to objects storage and retrieving. 
Models methods are in charge to create object and update them. Although, update method from models is called by a repository



## SUPPORTED FEATURES:

Since this is a simple version of AirBNB with the purpose to practice alone and in a limited amount of time, not everything is perfect and some HTTP methods are not handled yet as well as some attributes and objects are missing.

Notice: 
-  `DELETE` HTTP methods are not handled except for `reviews`.
- All object inherits from Base Model


| MODELS OBJECTS | ATTRIBUTES | API ENDPOINTS | METHODS |
|--|--|--|--|
|**Base Model** | `id` (str(UUID)),<br> `creation_date` (date),<br> `update_date` (date) | / | update(object),<br> save(object)
|**User** | `first_name` (str),<br> `last_name` (str),<br> `email` (str),<br> `is_admin` (bool),<br> `places` (list[ids]) | **POST** `/users` - create user<br> **GET** `/users` - all users<br> **GET** `/users/<user_id>` - get user by id <br>**PUT** `/users/<user_id>` update a user | /
|**Place** | `title` (str),<br> `description` (str), <br> `price` (float),<br> `latitude` (float),<br> `longitude` (float),<br> `owner_id` (str(UUID))| **POST** `/places` - create place<br> **GET** `/places` - all places<br> **GET** `/places/<place_id>` - get place by id <br>**GET** `/places/<place_id>/reviews` - get all reviews of a place <br>**PUT** `/places/<place_id>` update a place | add_review(review_id),<br> add_amenity(amenity_id)
|**Amenity** | `name`(str) | **POST** `/amenities` - create amenity<br> **GET** `/amenities` - all amenities<br> **GET** `/amenities/<amenity_id>` - get amenity by id <br>**PUT** `/amenities/<amenity_id>` update  amenity | /
| **Review** | `comment` (str), <br> `rating` int, <br>`place_id` (str(UUID)), <br> `user_id` (str(UUID)) | **POST** `/reviews` - create amenity<br> **GET** `/reviews` - all amenities<br> **GET** `/reviews/<review_id>` - get amenity by id <br>**PUT** `/reviews/<review_id>` update  amenity | /

## HOW TO USE IT:

### Running the API:

Use the following command to start the application :
> python run.py

### Sending HTTP methods:

Here are some example of request you can make to the API using `Curl` and the data send in response when the request succeed. 

`user creation`: 
> curl -X POST http://localhost:5000/api/v1/users/ -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"}'

Keep the user ID from the JSON response to create a place that he owns.

**JSON response:**
> {"id" : <`user_id`>, "first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"}

`amenities creation`:
> curl -X POST http://localhost:5000/api/v1/amenities/ -H "Content-Type: application/json" -d '{"name": "Wi-Fi"}'

> curl -X POST http://localhost:5000/api/v1/amenities/ -H "Content-Type: application/json" -d '{"name": "Pool"}'

Keep the IDs so you can use them to create a place - notice amenities are optional to create a place.

**JSON response:**
> {"id" : <`amenity_id`>, "name": "Pool"}

`place creation` - once you've created a user, use its ID from the json response:
>  curl -X POST http://localhost:5000/api/v1/places/
-H "Content-Type: application/json" -d '{"title": "Cozy Apartment", "description": "A nice place to stay", "price": 100.0, "latitude": 37.7749, "longitude": -122.4194, "owner_id": "`<owner id>`", "amenities": ["`<amenity_id>`", "`<amenity_id>`"]}'

Keep the place ID from the JSON response so you can use it in review creation.

**JSON response:**
> {"id" : <`amenity_id`>, "title": "Cozy Apartment", "description": "A nice place to stay", "price": 100.0, "latitude": 37.7749, "longitude": -122.4194, "owner_id": "`<owner id>`", "amenities": ["`<amenity_id>`", "`<amenity_id>`"]}

`review creation`
> curl -X POST http://localhost:5000/api/v1/reviews/ -H "Content-Type: application/json" -d '{"comment": "Great place to stay!", "rating": 5, "user_id": "`<user_id>`", "place_id": "`<place_id>`"}'

**JSON response:**
{"id" : <`amenity_id`>, "comment": "Great place to stay!", "rating": 5, "user_id": "`<user_id>`", "place_id": "`<place_id>`"}

`more requests`

For more request, you can refer to the api routes in the `supported features` section up above. Then, here is the syntax to use for a get request :

> curl http://localhost:5000<`api.route`>

for POST requests :

> curl -X POST http://localhost:5000<`api.route`> -H "Content-Type: application/json" -d '{`<required values for object creation>`}

for PUT requests: 

> curl -X PUT http://localhost:5000<`api.route`> -H "Content-Type: application/json" -d '{`<values to update>`}

**Status code** 

Here is a quick recap of the different status code you should get in return :

| HTTP Method | Status code
|--|--|
|**POST**| `201` object successfully created<br> `400` Invalid input data - an attribute value is out of range or wrong type <br> `404` Not found - the object ID you've indicated refer to an unexisting object
| **GET** | `200` object(s) successfully retrieved <br> `404` object not found - ID must be wrong
| **PUT** | `200` object successfully updated <br> `400` Invalid input data - an attribute value is out of range or wrong type <br> `404` Object not found - the object to udpate ID refers to an unexisting object <br> `409` Conflict with another existing object

## TESTS AND VALIDATION

In the test directory, four files performs unittest of a bunch of HTTP methods adn their returns. 

You can run the tests with the following command, launched from the `/part2/hbnb` repository :
> pytest -v

The `-v` option will give details on the test performed : normal creation, creation with wrong value, get with wrong ID, etc. 

## AUTHOR:
Mathieu Majérus