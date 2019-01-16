# Questioner
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Build Status](https://travis-ci.com/wekesa931/Questioner.svg?branch=develop)](https://travis-ci.com/wekesa931/Questioner)  [![Coverage Status](https://coveralls.io/repos/github/wekesa931/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/wekesa931/Questioner?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/5094ec5c3c20ffc0d5bc/maintainability)](https://codeclimate.com/github/wekesa931/Questioner/maintainability)

This is an application that sources questions from different users over a given subject and meetups are organised to answer them.
## Project Details
The appliction has been developed with:
1. [Javascript]( https://www.javascript.com/)
2. [HTML]( https://www.w3schools.com/html/html_intro.asp)
3. [CSS]( https://www.w3schools.com/css/)
4. [FLASK]( http://flask.pocoo.org/)

## The Application has the following specifications
1. A user should be able to register for a user account
2. Once registered, the user can log in to their dashboard
3. The admin user can create meetups which cosist of a topic of discussion
4. A user can RSVP for a specific meetup and post questions they wish answered on the meetup
5. A question can be upvoted or downvoted by users and the more upvoted a question is, the more it is prioritized.
6. The user can comment on specific questions.
7. A user can update their password and other account settings
## The following are the API Endpoints
| METHOD | END-POINT | DESCRIPTION |   PROTECTED |
| :---         |     :---      |          :--- | :--- |
| POST         |/api/v1/user/auth/signup |  Register a user   |FALSE|
| POST         |/api/v1/user/auth/login      | Log in a User     |FALSE|
| POST         |/api/v1/add_meetups     | Create a meetup record     |TRUE|
| GET          |/api/v1/get_meetups   | Gets all meetups records   |TRUE|
| GET          |/api/v1/meetups/<meetup_id>   | Fetch a specific meetup record    |TRUE|
| POST         |/api/v1/meetups/<meetup_id>/rsvps     | User can book to join a meetup    |TRUE|
| POST        |/api/v1/post_question    | Create a question record     | TRUE|
| PATCH        |/api/v1/<questions_id>/upvote   | upvote on a meetup question  |TRUE|
| PATCH        |/api/v1/<questions_id>/downvote   | downvote on a meetup question     |TRUE|

## Running the Aplication
#### Requirements include
a. [python3]( https://www.python.org/download/releases/3.0/) <br />
b. [pip]( https://pypi.org/project/pip/)
#### Installing the application
- Create a directory on your local machine and clone the repository
```
 $ git clone https://github.com/wekesa931/Questioner.git
```
- Install a virtual Environment and activate it
```
 $ python virtualenv venv 	
 $ source venv/bin/activate
```
Install the reuirements
```
 $ pip install -r requirements.txt
```
- Run the application
```
 $ export flask_config="development"
 $ python run.py
```
## Testing the application
##### 1. To test your code locally;
Install pytest
```
 $ pip install pytest
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
Create a project and test the endpoints.

##### 3. Continued integration
- [Travis]( https://travis-ci.com/) was used for continous integration to build and test the application.
- [coveralls](https://coveralls.io/) checks the test coverage of your application.

### Hosting
The application is hosted on [HEROKU]().Use postman for testing.
