# Profiles and Feed REST API

## Description
This repository contains the code for a REST API built with Django Rest Framework that provides basic user profile management functionalities, such as register, login, authentication and profile updates. Users are also able to post and edit status updates that then can be viewed by other users in a feed format.

## Requirements
* Python 3.6.5
* Django 1.11.9
* Django Rest Framework

## Running the server
1. Verify that you have the necessary packages installed
2. Clone this repository
3. Go to the folder `src/profiles_project`
4. Open a terminal window and type the following command: `python manage.py runserver`
5. That\`s it

## Browsable API Interface
The Django Rest Framework provides us a browsable interface for the API. Make sure that your local sever is running and type the following link on your favorite browser to access it:

`http://localhost:8000/api/`

There you can find the different endpoints provided by the API.

## API use cases

### List user profiles
**Functionality**

Retrieves the full list of registered user profiles

**Request**

* HTTP Method: GET
* URL: http://localhost:8000/api/profile/

**Response**

JSON Document with the list of registered user profiles

### Get details of a user profile
**Functionality**

Get the details (id, name and email) of a given user profile

**Request**

* HTTP Method: GET
* URL: http://localhost:8000/api/profile/<profile_id>

**Response**

JSON Document with details of the profile

### Search user profiles
**Functionality**

Search the user profile database by name or email

**Request**

* HTTP Method: GET
* URL: http://localhost:8000/api/profile/?search=<name_or_email>

**Response**

JSON Document with the details of the user profiles that matched the search

### Register user profile
**Functionality**

Register a new user profile to the database with the given name, email and password

**Request**

* HTTP Method: POST
* URL: http://localhost:8000/api/profile/
* Body: JSON Document
```json
{
    "email": "test@test.com",
    "name": "Tester",
    "password": "tested1"
}
 ```

**Response**

JSON Document with the id, name and email of the generated user profile

### Login
**Functionality**

Login with the credentials (email and password) of a registered user.

**Request**

* HTTP Method: POST
* URL: http://localhost:8000/api/login/
* Body: JSON Document
```json
{
    "username": "test@test.com",
    "password": "tested1"
}
```

**Response**

JSON Document with the authentication Token for the user

### Update profile (authenticated users only)
**Functionality**

Let the user change his/her profile details, given that the user Token is provided in the request for authentication.

**Request**

* HTTP Method: PUT
* URL: http://localhost:8000/api/login/<user_id>
* Headers:
```
Authentication: Token <user_token>
```
* Body: JSON Document
```json
{
    "email": "new@test.com",
    "name": "new",
    "password": "tested2"
}
 ```

**Response**

JSON Document with the updated user details

### View status update feed (authenticated users only)
**Functionality**

Display the status updates posted by the users

**Request**

* HTTP Method: GET
* URL: http://localhost:8000/api/feed
* Headers:
```
Authentication: Token <user_token>
```

**Response**

JSON Document with the details of the status updates posted in the feed

### View details of a status (authenticated users only)
**Functionality**

Display the details of the selected status update

**Request**

* HTTP Method: GET
* URL: http://localhost:8000/api/feed/<status_id>
* Headers:
```
Authentication: Token <user_token>
```

**Response**

JSON Document with the details of the selected status update

### Create a new status update (authenticated users only)
**Functionality**

Create a new status update from the authenticated user with the given message

**Request**

* HTTP Method: POST
* URL: http://localhost:8000/api/feed
* Headers:
```
Authentication: Token <user_token>
```
* Body: JSON Document
```json
{
"status_text": "Another test message!"
}
 ```

**Response**

JSON Document with the details of newly created status

### Edit a status update (authenticated users only)
**Functionality**

Edit a status update that was created by the authenticated user

**Request**

* HTTP Method: PUT
* URL: http://localhost:8000/api/feed/<status_id>
* Headers:
```
Authentication: Token <user_token>
```
* Body: JSON Document
```json
{
"status_text": "Another (edited) test message!"
}
 ```

**Response**

JSON Document with the details of edited status

### Delete a status update (authenticated users only)
**Functionality**

Delete a status update that was created by the authenticated user

**Request**

* HTTP Method: DELETE
* URL: http://localhost:8000/api/feed/<status_id>
* Headers:
```
Authentication: Token <user_token>
```

**Response**

Confirmation that the status was deleted
