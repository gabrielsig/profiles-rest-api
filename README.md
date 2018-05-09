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

`http://localhost:8000/api/``

There you can find the different endpoints provided by the API.

## API use cases
#### List user profiles
* Request
HTTP GET http://localhost:8000/api/profile/
* Response
JSON Document with the list of registered user profiles
