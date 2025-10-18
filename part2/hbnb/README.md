# HBNB PART 2 - API / BUSINESS LOGIC / TESTING & DEBUGGING

## INTRODUCTION
In this part 2 of the HBNB project, we were asked to implement de business logic and API of our AirBNB-like application :
- Core business logic
- API endpoints
- Tests and validations with UNITTEST

The files in this repos will show you my work on thoses aspects, on the basis of the file organisation and some files contents (__init__ files, repository...) given by Holberton School.
Feel free to visit this repo if you want to take a look at this work basis : https://github.com/Holberton-Uy/hbnb-doc/tree/main/part2

**Perimeter of the project : HTTP methods and object attributes:**

Since this is a simple version of AirBNB with the purpose to practice alone and in a limited amount of time, not everything is perfect and some HTTP methods are not handled yet as well as some attributes and objects are missing.

Notice: 
-  `DELETE` HTTP methods are not handled except for `reviews`.
- All object inherits from Base Model


| OBJECT | ATTRIBUTES | API REQUESTS | METHODS | 
|--|--|--|--|
|Base Model | `id` (str(UUID)), `creation_date`, `update_date` | / | update(object), save(object)
|User | `first_name` (str), `last_name` (str), `email` (str), `is_admin` (bool), `places` (list[ids]) | POST: create a new user \GET: all users \GET: user by id \PUT: update a user | /
|Place | `title` (str), `description` (str), `price` (float), `latitude` (float), `longitude` (float), 

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

## HOW TO USE IT:

**Running the API:**

Use the following command to start the application :
> python run.py

**Sending HTTP methods**



