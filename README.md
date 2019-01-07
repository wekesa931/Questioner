# Questioner Application
Ths is an application that sources questions from different users over a given subject and meetups are organised to answer them. The Admin user creates a meetup for a specific subject and the users, once logged in, pose their questions and comments on the subject of discussion.

## Functionality of the application
This repository contains the static user interface templates for the application. They include:
  1. Sign up and Sign in pages
  2. The user dashboard
  3. The admin user dashoard
  4. The meetup page
## Working of the application
When the admin user creates a meetup, the user, once logged in, gets a notification of the questions on the meetup and they are prompted to join the meetup.

## Development
The static pages are created with:
[HTML]( https://www.w3schools.com/html/)
[CSS]( https://www.w3schools.com/css/)
[JavaScript]( https://www.w3schools.com/js/)

## Responsive Design
The responsive design is achieved with `media-queries` and `flexbox`. An illustration is as shown
```@media screen and (max-width: 480px) {
    .logo {
        width: 70%;
        margin-top: 23%;
    }
    .logo-holder {
        width: 10%;
    }
   }
   ```
**Media queries** enable the application adjust with screen width.
[Further documentation on media queries can be found  HERE]( https://www.w3schools.com/css/css_rwd_mediaqueries.asp)
**Flexbox** makes it easier to design flexible responsive layout structure without using float or positioning. The DOM elements can adjust automatically with changes in screen size hence achieving a responsive design.
[Further documentation on flexbox can be found  HERE]( https://www.w3schools.com/css/css3_flexbox.asp)

## Hosting
The static sites have been hosted on github pages:
[Admin Page]( https://wekesa931.github.io/Questioner/UI/routes/admin)
[User log-in and sign-up Page]( https://wekesa931.github.io/Questioner/UI/routes/user)
[User dashboard]( https://wekesa931.github.io/Questioner/UI/routes/dashboard)
[meetup page]( https://wekesa931.github.io/Questioner/UI/routes/meetup)

## Dependencies
I used the following fonts from google;
1. [Font Awesome]( https://maxcdn.bootstrapcdn.com/font-awesome/4.6.1/css/font-awesome.min.css)

## Running the application
1. Clone the repository to you local machine 
```
$ git clone https://github.com/wekesa931/Questioner.git
```
Run the application on your browser