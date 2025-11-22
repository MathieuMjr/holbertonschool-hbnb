# HBNB PROJECT 

HBNB project's purpose is to build an AirBNB clone on my own from scratch, but guided through the different steps thanks to Holberton School curriculus. 

## 1. Technical documentation and UML diagrams 
Files related to this part can be found in the `part1` directory.

In order to anticipate our coding, we were asked to get familiar with 3 types of UML diagrams : 
- `Highlevel package diagram`
- `Class diagram`
- `Sequence diagrams`

Those three diagrams constitute the technical documentation, informing users about the architecture layers and their depending relations (`package diagram`), class models and their relations (`class diagrams`) and sequences of layers interactions (`sequence diagrams`) in 4 scenarios : user registration, place creation, review submission and list of places request. 

## 2. Implementing business logic core and API Endpoint :
Part 2 contains files written to implement businees logic core and API endpoint with the facade design architecture. 
A specific readme explain how it works. 

Four object have been created : user, place, amenity, review. All inherit from a base model. 

API routes handle the CRUDS operations (except DELETE operations that only review object can handle) and return the apropriate status code. 

## 3. Implementing authentication, JWT access, Admin privileges and remove InMemory Repository to a SQLite database
In part 3, we've implemented authentication and authorization. Some API routes are now protected and only some user can perform some specific CRUD operations. Administrators have some privileges too. 

We've also replaced our classes to SQLAlchemy models, making our objects persistent on a SQLite database. 

## Work is still in progress, more content will come as the project goes further o/