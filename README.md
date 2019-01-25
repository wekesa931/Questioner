# Questioner
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Build Status](https://travis-ci.com/wekesa931/Questioner.svg?branch=develop)](https://travis-ci.com/wekesa931/Questioner)  [![Coverage Status](https://coveralls.io/repos/github/wekesa931/Questioner/badge.png?branch=develop)](https://coveralls.io/github/wekesa931/Questioner?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/5094ec5c3c20ffc0d5bc/maintainability)](https://codeclimate.com/github/wekesa931/Questioner/maintainability)

This is an application that sources questions from different users over a given subject and meetups are organised to answer them.
## Project Details
The appliction has been developed with:
1. [Javascript]( https://www.javascript.com/)
2. [HTML]( https://www.w3schools.com/html/html_intro.asp)
3. [CSS]( https://www.w3schools.com/css/)
4. [FLASK]( http://flask.pocoo.org/)

## The Application has the following specifications
1. The application has a *Supperuser* user who is able to promote other users to admin status
2. The admin user has added privilledges to add meetup, delete meetup, view user details and and tags and images to meetup
3. A user should be able to register for a normal user account
4. Once registered, the user can log in to their dashboard
5. The admin user can create meetups which consist of a topic of discussion
6. A user can create reservations for a specific meetup and post questions they wish answered on the meetup
7. A question can be upvoted or downvoted by users and the more upvoted a question is, the more it is prioritized.
8. The user can comment on specific questions.
9. A user can update their password and other account settings

## Single page web application
This is a single page web application. An **SPA** is a website that re-renders its content in response to navigation actions (e.g. clicking a link) without making a request to the server to fetch new HTML. This means that it dynamically rewrites the current page rather than loading entire new pages hence making access faster and can work offline.

## The following are the API Endpoints
### User Authentication
| METHOD | END-POINT | DESCRIPTION |   PROTECTED |RIGHTS |
| :---         |     :---      |          :--- | :--- |:--- |
| POST         |/user/auth/signup |  Register a user   |FALSE|ALL USERS|
| POST         |/user/auth/login      | Log in a User     |FALSE|ALL USERS|
| GET         |/user/auth/users      | View all registered users|TRUE|ADMIN|
|PATCH |/user/auth/<user_id>/admin |Upgrades a user to admin status | TRUE |SUPERUSER|

### Meetups
| METHOD | END-POINT | DESCRIPTION |   PROTECTED |RIGHTS |
| :---         |     :---      |          :--- | :--- |:--- |
| POST         |/meetups    | Create a meetup record |TRUE|ADMIN|
| GET          |/meetups   | Gets all meetups records   |TRUE|ALL USERS|
| GET          |/meetups/<meetup_id>   | Fetch a specific meetup record    |TRUE|ALL USERS|
| DELETE|/meetups/<meetup_id>   | DELETES a specific meetup record |TRUE|ADMIN|
| POST         |/meetups/<meetup_id>/rsvp | User can book to join a meetup    |TRUE|ALL USERS|
| POST|/<meetup_id>/tags| Adds a tag to a meetup    |TRUE|ADMIN|
| POST|/<meetup_id>/image| Adds an image to a meetup    |TRUE|ADMIN|

### Questions
| METHOD | END-POINT | DESCRIPTION |   PROTECTED |RIGHTS |
| :---         |     :---      |          :--- | :--- |:--- |
| POST |/<meetup_id>/question | Create a question record     | TRUE|ALL USERS|
| GET |/<meetup_id>/questions | Gets all question records from a specific meetup    | TRUE|ALL USERS|
| POST |/<question_id>/comment | Adds a comment to a question| TRUE|ALL USERS|
| POST |/<question_id>/question | Gets a single question record| TRUE|ALL USERS|
| PATCH        |/<questions_id>/upvote   | upvote on a meetup question  |TRUE|ALL USERS|
| PATCH        |/<questions_id>/downvote   | downvote on a meetup question     |TRUE|ALL USERS|

## Running the Aplication
#### Requirements include
a. [python3]( https://www.python.org/download/releases/3.0/) <br />
b. [pip3]( https://pypi.org/project/pip/). This is a package manager for Python packages.

#### Installing the application
- Create a directory on your local machine and clone the repository
```
 $ git clone https://github.com/wekesa931/Questioner.git
 $ cd questioner
```
- Install a virtual Environment and activate it
```
 $ python virtualenv venv 	
 $ source venv/bin/activate
```
Install the reuirements
```
 $ pip3 install -r requirements.txt
```
- Run the application
```
 $ export api_database_url="postgres://wekesa@localhost/api_db"
 $ export flask_config="development"
 $ python run.py
```
## Testing the application
##### 1. To test your code locally;
Install pytest
```
 $ pip3 install pytest
```
To run the test
```
 $ pytest
```
To test the test coverage
```
 $ pytest --cov=app/api app/tests/ 
```
##### 2. Testig with Postman
Install the [Postman]( https://www.getpostman.com/) application  <br />
Test the api endpoints.

##### 3. Continued integration
- [Travis]( https://travis-ci.com/) was used for continous integration to build and test the application.
- [coveralls](https://coveralls.io/) checks the test coverage of your application.

### Hosting
The application is hosted on [HEROKU](https://wekesaapp.herokuapp.com/).Use postman for testing.

### Documentation
The application is documented on [SWAGGER](https://app.swaggerhub.com/apis/questioner4/wekesa-questioner/1.0.0#/).