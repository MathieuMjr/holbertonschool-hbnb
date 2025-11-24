# HBNB PART 3 - Enhanced Backend with Authentication and Database Integration

## INTRODUCTION
In this part 3 of the HBNB project, we were asked to implement authentication and authorization through JWT tokens, to move from in-memory storage to database storage via SQLAlchemy,work on SQL diagram. 

The files in this repos will show you my work on those aspects, on the basis of instructions given by Holberton School.
Feel free to visit this repo if you want to take a look at the materials : https://github.com/Holberton-Uy/hbnb-doc/tree/main/part3

**What changes since part2 ?**

- Security : implemented password management with bcrypt
- Authorization : somes routes are now protected with roles authorizations - check `SUPPORTED FEATURES` part to see which route ask for JWT tokens
- Persistence : InMemoryRepository has transitioned to a database layer via SQLAlchemyRepository, containing SQALchemy methods to perform request ; Python objects have been turned into ORM models.
- Persistence bis : new files appeared "user_repository", "place_repository"... dedicated to table specific methods/request in addition of the basic CRUDs operations in SQAlchemyRepository

## OVERVIEW

In order to get a good overview of the project, this section provides:
- the overall directories and files organization
- details on the purpose of each files
- the SQL diagram of the implemented database

```
part3/
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── amenities.py
│   │       ├── auth.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       └── users.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── amenity.py
│   │   ├── base.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── user.py
│   ├── persistence/
│   │   ├── __init__.py
│   │   ├── amenity_repository.py
│   │   ├── place_repository.py
│   │   ├── repository.py
│   │   ├── review_repository.py
│   │   └── user_repository.py
│   └── services/
│       ├── __init__.py
│       └── facade.py
├── tests/
├── config.py
├── hbnb.db
├── README.md
├── requirements.txt
├── run.py
└── SQL-script.sql
```

Directory | Filename | Responsibility |
-- | --| -- | 
| part3 | `run.py` | runs the app and create a base admin.
| part3 | `config.py` | contains some classes to run the app with different configs (for development, or not).
| part3 | `requirements.txt` | contains information about modules versions.
| part3 | `SQL-script.sql` | is a script that shows in pure SQL the database schema and some first creations : Admin user and some amenities.<br> Could use it to generate your own database.<br> Contains **some basic tests** in comments.
| part3| `hbnb.db` | is the database created via SQL-script.sql to check if the schema works well. Feel free to try it.
| app | `__init__.py` | define the app creation function according to the desired configuration. Contains initialization for database, tokens and bcrypt + register the namespaces of the API.
| app | `extensions.py` | contains extensions object creation like jwt, db and bcrypt.
| api/v1/ | `auth.py` | is where the api routes to authentications are written.
| api/v1/ | `amenities.py`<br> `places.py`<br> `reviews.py`<br> `users.py` | contains api routes to make create, retrieve, update, delete requests.
| models | `amenity.py`<br> `places.py`<br> `reviews.py`<br> `users.py` | contains the ORM models for each entity and their methods.
| services | `__init__.py` |contain the code that instanciate the facade object.
| services | `facade.py` | define the functions that allow the facade to orchestrate API requests and database storage/data retrieval.
| persistence | `repository.py` | define the basic CRUD functions to interact with database.
| persistence | `amenity_repository.py` <br> `palce_repository.py`<br> `review_repository.py`<br> `user_repository.py` | define for each entities specific functions to interact with database, for exemple, `get_user_by_email` that other entities can't do.

**SQL Diagram**

<img src=SQL_Diagram.jpg>

## REQUIREMENTS: 

The following instruction will help you to install this app on your computer. 

**System:**

This app was built on Ubuntu. 

**Cloning the repository:**

In order ton install the app on your computer, install it via this command :

> git clone https://github.com/MathieuMjr/holbertonschool-hbnb.git

Don't forget to go in the proper directory before going any further :

> cd part3/

**Virtual environnement**

Some modules are required and needs the creation of a virtual environement. Here are the steps to follow in order to install your virtual environnement. 

All the following commands must be executed from `part3` directory.


|Step | Command
|--|--|
|V env creation | `python3 -m venv venv`
|V env activation | `source venv/bin/activate`
|Modules installation | `pip -r requirements.txt`

\
You should have `(venv)` written at the very beginning of your line commands if it has been activated successfully. 

If you need to install on your own the required modules, here are the versions used :

|Module |Version
|--|--|
| Flask | 3.1.2
| Flask-restx | 1.3.2
| flask-bcrypt | 1.0.1
| Flask-JWT-Extended | 4.7.1
| SQLAlchemy |2.0.44
| Flask-SQLAlchemy|  3.1.1


## ARCHITECTURE DESIGN:
The project uses the **facade pattern** :

API  -->  FACADE  -->  REPOSITORY/MODELS

API calls for facade function to fulfill requests. Facade functions orchestrate function calls to MODELS or REPOSITORY according to the requests. 

Repository methods are related to objects storage and retrieving. 
Models methods are in charge to create object and update them. Although, update method from models is called by a repository method.


## SUPPORTED FEATURES:

Since this is a simple version of AirBNB with the purpose to practice alone and in a limited amount of time, some features are intentionally simplified due to time constraints.

Notice: 
-  `DELETE` HTTP methods are not handled except for `reviews`.
- All objects inherit from Base Model

New features since part 2: 
- Admin creation require admin privilege
- User can only create a place with his ID has owner_id ; admin can create any place
- User can only update a place he owns ; admin can update any place
- Only Admins can manage amenities
- Only a logged in user can review a place he does not own.
- Logged users can update their own reviews.
- Admins has no specific privilege on reviews.


| MODELS OBJECTS | ATTRIBUTES | API ENDPOINTS | METHODS |
|--|--|--|--|
|**Base Model** | `id` (str(UUID)),<br> `creation_date` (date),<br> `update_date` (date) | / | update(object),<br> save(object)
|**User** | `first_name` (str),<br> `last_name` (str),<br> `email` (str),<br> `is_admin` (bool),<br> `places` (list[ids]) | **POST** `/users` - create user - *Admin role required for admin creation*<br> **GET** `/users` - all users - *Admin role required*<br> **GET** `/users/<user_id>` - get user by id<br>**PUT** `/users/<user_id>` update a user - *JWT required* | /
|**Place** | `title` (str),<br> `description` (str), <br> `price` (float),<br> `latitude` (float),<br> `longitude` (float),<br> `owner_id` (str(UUID))| **POST** `/places` - create place *JWT required*<br> **GET** `/places` - all places<br> **GET** `/places/<place_id>` - get place by id <br>**GET** `/places/<place_id>/reviews` - get all reviews of a place <br>**PUT** `/places/<place_id>` update a place- *JWT required* | add_review(review_id),<br> add_amenity(amenity_id)
|**Amenity** | `name`(str) | **POST** `/amenities` - create amenity - *Admin role required*<br> **GET** `/amenities` - all amenities<br> **GET** `/amenities/<amenity_id>` - get amenity by id <br>**PUT** `/amenities/<amenity_id>` update amenity - *Admin role required* | /
| **Review** | `comment` (str), <br> `rating` int, <br>`place_id` (str(UUID)), <br> `user_id` (str(UUID)) | **POST** `/reviews` - create review - *JWT required*<br> **GET** `/reviews` - all reviews<br> **GET** `/reviews/<review_id>` - get review by id <br>**PUT** `/reviews/<review_id>` update  review *JWT required*<br> **DELETE** `/reviews/<review_id>` - delete review *JWT required*| /
| / | / | **POST** `/auth` - loggin and generate access token |/

## HOW TO USE IT:

### Database creation:
In order to run the app, I recommend you to follow thoses steps so it match the database URI in `config.py`:

1. open the flask shell

> flask shell

2. import the db

> from app.extensions import db

3. create the SQLite database with tables :

> db.create_all()

Please, notice that an admin is created by default so you can try admin operations. Check `run.py` to find the credentials. 

**About the SQL-script**

You might have notice a SQL script `SQL-script.sql` is provided. It is a file asked fo pedagogical purpose only. 
It won't match the actual database :
- created_at and udpated_at columns are missing ; I'm not sure SQLite can manage TIMESTAMP
- you'd have to change the database name and URI in `config.py`
- admin's password has been hashed via an online hash generator. You would raise a 500 Invalid salt at loggin. 

Might fixe this later so you could use a pre-made database. 

### Running the API:

Use the following command to start the application :
> python run.py

### Sending HTTP methods:

Here are some example of curl request made in part2. Since token authorizations have been implemented in part3, they are no longer usefull.
If you want to make some tries, please check `TEST AND VALIDATIONS`, below. 

<details>
<summary> Click here to take a look at curl request written in part2</summary>
Here are some example of requests you can make to the API using `Curl` and the data send in response when the request succeed. 

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

`More requests`

For more request, you can refer to the api routes in the `supported features` section up above. Then, here is the syntax to use for a get request :

> curl http://localhost:5000<`api.route`>

for POST requests :

> curl -X POST http://localhost:5000<`api.route`> -H "Content-Type: application/json" -d '{`<required values for object creation>`}

for PUT requests: 

> curl -X PUT http://localhost:5000<`api.route`> -H "Content-Type: application/json" -d '{`<values to update>`}
</details>

**Status code** 

Here is a quick recap of the different status code you should get in return :

| HTTP Method | Status code
|--|--|
|**POST**| `201` object successfully created<br> `400` Invalid input data - an attribute value is out of range or wrong type <br> `404` Not found - the object ID you've indicated refer to an unexisting object<br> `403` Unauthorized action
| **GET** | `200` Object(s) successfully retrieved <br> `404` Object not found - ID must be wrong<br> `403` Admin privileges required
| **PUT** | `200` object successfully updated <br> `400` Invalid input data - an attribute value is out of range or wrong type <br> `404` Object not found - the object to udpate ID refers to an unexisting object <br> `409` Conflict with another existing object<br> `403` Unauthorized action

## TESTS AND VALIDATION

Unittest from part2 are no longer functional since we've implemented authentication - unfortunately, due to time constraint, they have not been updated.

During the development, I have used Postman ; you can find below the JSON file to import in order to perform the tests I did on my own code.
Don't forget to import en environment too.
<details>
<summary> Click to get the json code </summary>

```
{
	"info": {
		"_postman_id": "daa9d445-faec-4946-a178-1dc70bb2482b",
		"name": "My Collection",
		"description": "### Welcome to Postman! This is your first collection. \n\nCollections are your starting point for building and testing APIs. You can use this one to:\n\n• Group related requests\n• Test your API in real-world scenarios\n• Document and share your requests\n\nUpdate the name and overview whenever you’re ready to make it yours.\n\n[Learn more about Postman Collections.](https://learning.postman.com/docs/collections/collections-overview/)",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "49619338",
		"_collection_link": "https://lunar-module-architect-22703462-4935133.postman.co/workspace/Mathieu-Majerus's-Workspace~366bc12a-a01f-4f83-88d0-d3a8aedb5ffe/collection/49619338-daa9d445-faec-4946-a178-1dc70bb2482b?action=share&source=collection_link&creator=49619338"
	},
	"item": [
		{
			"name": "Login",
			"item": [
				{
					"name": "John Doe login",
					"event": [
						{
							"listen": "test",
							"script": {
								"exec": [
									"pm.test(\"Status code is 200\", function () {",
									"    pm.response.to.have.status(200);",
									"});",
									"const response = pm.response.json();",
									"pm.environment.set(\"user_token\", response.access_token);"
								],
								"type": "text/javascript",
								"packages": {},
								"requests": {}
							}
						}
					],
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\"email\": \"john.doe@example.com\", \"password\": \"12345\"}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://localhost:5000/api/v1/auth/login",
							"protocol": "http",
							"host": [
								"localhost"
							],
							"port": "5000",
							"path": [
								"api",
								"v1",
								"auth",
								"login"
							]
						},
						"description": "This is a GET request and it is used to \"get\" data from an endpoint. There is no request body for a GET request, but you can use query parameters to help specify the resource you want data on (e.g., in this request, we have `id=1`).\n\nA successful GET response will have a `200 OK` status, and should include some kind of response body - for example, HTML web content or JSON data."
					},
					"response": []
				},
				{
					"name": "user 2 login",
					"event": [
						{
							"listen": "test",
							"script": {
								"exec": [
									"pm.test(\"Status code is 200\", function () {",
									"    pm.response.to.have.status(200);",
									"});",
									"const response = pm.response.json();",
									"pm.environment.set(\"user2_token\", response.access_token);"
								],
								"type": "text/javascript",
								"packages": {},
								"requests": {}
							}
						}
					],
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\"email\": \"jaja.doe@example.com\", \"password\": \"12345\"}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://localhost:5000/api/v1/auth/login",
							"protocol": "http",
							"host": [
								"localhost"
							],
							"port": "5000",
							"path": [
								"api",
								"v1",
								"auth",
								"login"
							]
						},
						"description": "This is a GET request and it is used to \"get\" data from an endpoint. There is no request body for a GET request, but you can use query parameters to help specify the resource you want data on (e.g., in this request, we have `id=1`).\n\nA successful GET response will have a `200 OK` status, and should include some kind of response body - for example, HTML web content or JSON data."
					},
					"response": []
				},
				{
					"name": "By default admin login",
					"event": [
						{
							"listen": "test",
							"script": {
								"exec": [
									"const response = pm.response.json();\r",
									"pm.environment.set(\"admin_token\", response.access_token);"
								],
								"type": "text/javascript",
								"packages": {},
								"requests": {}
							}
						}
					],
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\"email\": \"admin@example.com\", \"password\": \"admin\"}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{base_url}}/auth/login",
							"host": [
								"{{base_url}}"
							],
							"path": [
								"auth",
								"login"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "User",
			"item": [
				{
					"name": "Create user John Doe",
					"event": [
						{
							"listen": "test",
							"script": {
								"exec": [
									"pm.test(\"Successful POST request\", function () {",
									"    pm.expect(pm.response.code).to.be.oneOf([200, 201]);",
									"});",
									"const response = pm.response.json();",
									"pm.environment.set(\"user_id\", response.id);",
									""
								],
								"type": "text/javascript",
								"packages": {},
								"requests": {}
							}
						},
						{
							"listen": "prerequest",
							"script": {
								"exec": [
									""
								],
								"type": "text/javascript",
								"packages": {},
								"requests": {}
							}
						}
					],
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{user2_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\"first_name\": \"John\", \"last_name\": \"Doe\", \"email\": \"john.doe@example.com\", \"password\": \"12345\"}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://localhost:5000/api/v1/users/",
							"protocol": "http",
							"host": [
								"localhost"
							],
							"port": "5000",
							"path": [
								"api",
								"v1",
								"users",
								""
							]
						},
						"description": "This is a POST request, submitting data to an API via the request body. This request submits JSON data, and the data is reflected in the response.\n\nA successful POST request typically returns a `200 OK` or `201 Created` response code."
					},
					"response": []
				},
				{
					"name": "Create user 2",
					"event": [
						{
							"listen": "test",
							"script": {
								"exec": [
									"pm.test(\"Successful POST request\", function () {",
									"    pm.expect(pm.response.code).to.be.oneOf([200, 201]);",
									"});",
									"const response = pm.response.json();",
									"pm.environment.set(\"user2_id\", response.id);",
									""
								],
								"type": "text/javascript",
								"packages": {},
								"requests": {}
							}
						},
						{
							"listen": "prerequest",
							"script": {
								"exec": [
									""
								],
								"type": "text/javascript",
								"packages": {},
								"requests": {}
							}
						}
					],
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{user_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\"first_name\": \"Jane\", \"last_name\": \"Doe\", \"email\": \"jaja.doe@example.com\", \"password\": \"12345\"}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://localhost:5000/api/v1/users/",
							"protocol": "http",
							"host": [
								"localhost"
							],
							"port": "5000",
							"path": [
								"api",
								"v1",
								"users",
								""
							]
						},
						"description": "This is a POST request, submitting data to an API via the request body. This request submits JSON data, and the data is reflected in the response.\n\nA successful POST request typically returns a `200 OK` or `201 Created` response code."
					},
					"response": []
				},
				{
					"name": "Get all",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{admin_token}}",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "http://localhost:5000/api/v1/users/",
							"protocol": "http",
							"host": [
								"localhost"
							],
							"port": "5000",
							"path": [
								"api",
								"v1",
								"users",
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "http://localhost:5000/api/v1/users/{{user_id}}",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{user_token}}",
									"type": "string"
								}
							]
						},
						"method": "PUT",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\"last_name\": \"Jaja\"}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://localhost:5000/api/v1/users/{{user_id}}",
							"protocol": "http",
							"host": [
								"localhost"
							],
							"port": "5000",
							"path": [
								"api",
								"v1",
								"users",
								"{{user_id}}"
							]
						}
					},
					"response": []
				},
				{
					"name": "Admin 2 creation",
					"event": [
						{
							"listen": "test",
							"script": {
								"exec": [
									"const response = pm.response.json();\r",
									"pm.environment.set(\"admin_id\", response.id);"
								],
								"type": "text/javascript",
								"packages": {},
								"requests": {}
							}
						}
					],
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{admin_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\"first_name\": \"admin\", \"last_name\": \"admin\", \"email\": \"admin2@example.com\", \"is_admin\": true, \"password\": \"admin\"}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{base_url}}/users",
							"host": [
								"{{base_url}}"
							],
							"path": [
								"users"
							]
						}
					},
					"response": []
				},
				{
					"name": "user by id",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://localhost:5000/api/v1/users/{{user_id}}",
							"protocol": "http",
							"host": [
								"localhost"
							],
							"port": "5000",
							"path": [
								"api",
								"v1",
								"users",
								"{{user_id}}"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Places",
			"item": [
				{
					"name": "Place 1 creation (no amenity)",
					"event": [
						{
							"listen": "test",
							"script": {
								"exec": [
									"const response = pm.response.json();\r",
									"pm.environment.set(\"place1_id\", response.id);"
								],
								"type": "text/javascript",
								"packages": {},
								"requests": {}
							}
						}
					],
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{user_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "{{user_token}}",
								"type": "text",
								"disabled": true
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\"title\": \"Pretty Apartment\", \"description\": \"A lovely place to stay\", \"price\": 200.0, \"latitude\": 50.7749, \"longitude\": -122.4194, \"owner_id\": \"{{user_id}}\"}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{base_url}}places",
							"host": [
								"{{base_url}}places"
							]
						}
					},
					"response": []
				},
				{
					"name": "Place 2 creation with amenity from user 2",
					"event": [
						{
							"listen": "test",
							"script": {
								"exec": [
									"const response = pm.response.json();\r",
									"pm.environment.set(\"place2_id\", response.id);"
								],
								"type": "text/javascript",
								"packages": {},
								"requests": {}
							}
						}
					],
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{user2_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\"title\": \"Cozy Apartment\", \"description\": \"A nice place to stay\", \"price\": 100.0, \"latitude\": 37.7749, \"longitude\": -122.4194, \"owner_id\":\"{{user2_id}}\", \"amenities\": [\"{{amenity_id}}\"]}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{base_url}}places",
							"host": [
								"{{base_url}}places"
							]
						}
					},
					"response": []
				},
				{
					"name": "{{base_url}}places/{{place1_id}}",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{user2_token}}",
									"type": "string"
								}
							]
						},
						"method": "PUT",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\"title\": \"Luxury Condo\", \"description\": \"An upscale place to stay\", \"price\": 200.0}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{base_url}}places/{{place1_id}}",
							"host": [
								"{{base_url}}places"
							],
							"path": [
								"{{place1_id}}"
							]
						}
					},
					"response": []
				},
				{
					"name": "Get all",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{base_url}}/places",
							"host": [
								"{{base_url}}"
							],
							"path": [
								"places"
							]
						}
					},
					"response": []
				},
				{
					"name": "Get by ID",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{base_url}}/places/{{place2_id}}",
							"host": [
								"{{base_url}}"
							],
							"path": [
								"places",
								"{{place2_id}}"
							]
						}
					},
					"response": []
				},
				{
					"name": "Get place 2 reviews",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{base_url}}places/{{place2_id}}/reviews",
							"host": [
								"{{base_url}}places"
							],
							"path": [
								"{{place2_id}}",
								"reviews"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Reviews",
			"item": [
				{
					"name": "review place 1 by user 2",
					"event": [
						{
							"listen": "test",
							"script": {
								"exec": [
									"const response = pm.response.json();\r",
									"pm.environment.set(\"review_id\", response.id);"
								],
								"type": "text/javascript",
								"packages": {},
								"requests": {}
							}
						}
					],
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{user2_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\"comment\": \"Great place to stay!\", \"rating\": 5, \"user_id\": \"{{user2_id}}\", \"place_id\": \"{{place1_id}}\"}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{base_url}}reviews",
							"host": [
								"{{base_url}}reviews"
							]
						}
					},
					"response": []
				},
				{
					"name": "Update review",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{user2_token}}",
									"type": "string"
								}
							]
						},
						"method": "PUT",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\"comment\": \"Amazing stay!\", \"rating\": 5}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{base_url}}/reviews/{{review_id}}",
							"host": [
								"{{base_url}}"
							],
							"path": [
								"reviews",
								"{{review_id}}"
							]
						}
					},
					"response": []
				},
				{
					"name": "Delete review",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{user2_token}}",
									"type": "string"
								}
							]
						},
						"method": "DELETE",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{base_url}}reviews/{{review_id}}",
							"host": [
								"{{base_url}}reviews"
							],
							"path": [
								"{{review_id}}"
							]
						}
					},
					"response": []
				},
				{
					"name": "Get all reviews",
					"request": {
						"auth": {
							"type": "noauth"
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{base_url}}reviews/",
							"host": [
								"{{base_url}}reviews"
							],
							"path": [
								""
							]
						}
					},
					"response": []
				},
				{
					"name": "review place 2 by John Doe",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{user_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\"comment\": \"Great place to stay!\", \"rating\": 5, \"user_id\": \"{{user_id}}\", \"place_id\": \"{{place2_id}}\"}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{base_url}}reviews/",
							"host": [
								"{{base_url}}reviews"
							],
							"path": [
								""
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Amenity",
			"item": [
				{
					"name": "Amenity creation 1",
					"event": [
						{
							"listen": "test",
							"script": {
								"exec": [
									"const response = pm.response.json();\r",
									"pm.environment.set(\"amenity_id\", response.id);"
								],
								"type": "text/javascript",
								"packages": {},
								"requests": {}
							}
						}
					],
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{admin_token}}",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\"name\": \"Wi-Fi\"}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{base_url}}/amenities",
							"host": [
								"{{base_url}}"
							],
							"path": [
								"amenities"
							]
						}
					},
					"response": []
				},
				{
					"name": "Update amenity",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "{{admin_token}}",
									"type": "string"
								}
							]
						},
						"method": "PUT",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\"name\": \"haunted\"}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{base_url}}/amenities/{{amenity_id}}",
							"host": [
								"{{base_url}}"
							],
							"path": [
								"amenities",
								"{{amenity_id}}"
							]
						}
					},
					"response": []
				},
				{
					"name": "Get all",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{base_url}}/amenities/",
							"host": [
								"{{base_url}}"
							],
							"path": [
								"amenities",
								""
							]
						}
					},
					"response": []
				}
			]
		}
	]
}
```
</details>
<details>
<summary> Postman environment </summary>

```
{
	"id": "50587624-45fa-473d-9ed2-72c7c779d106",
	"name": "Dev",
	"values": [
		{
			"key": "user_id",
			"value": "",
			"type": "default",
			"enabled": true
		},
		{
			"key": "base_url",
			"value": "",
			"type": "default",
			"enabled": true
		},
		{
			"key": "user_token",
			"value": "",
			"type": "default",
			"enabled": true
		},
		{
			"key": "place1_id",
			"value": "",
			"type": "default",
			"enabled": true
		},
		{
			"key": "user2_id",
			"value": "",
			"type": "default",
			"enabled": true
		},
		{
			"key": "user2_token",
			"value": "",
			"type": "default",
			"enabled": true
		},
		{
			"key": "admin_id",
			"value": "",
			"type": "default",
			"enabled": true
		},
		{
			"key": "review_id",
			"value": "",
			"type": "any",
			"enabled": true
		},
		{
			"key": "admin_token",
			"value": "",
			"type": "default",
			"enabled": true
		},
		{
			"key": "amenity_id",
			"value": "",
			"type": "default",
			"enabled": true
		},
		{
			"key": "place2_id",
			"value": "",
			"type": "default",
			"enabled": true
		}
	],
	"_postman_variable_scope": "environment",
	"_postman_exported_at": "2025-11-05T15:25:53.671Z",
	"_postman_exported_using": "Postman/11.70.2"
}
```
</details>


## AUTHOR:
Mathieu Majérus