# BOS UP jobboard - Milestone Project 3

## Introduction
Welcome to [BOS UP](https://jobboard-milestone3.herokuapp.com/)! This site is created to let potential candidates know who we are and what we do. And also we want to give the option to see if they want to come and join us! If a candidate registers on our site and our recruiter has had contact with them, the candidate can apply on several cool and interesting vacancies. At all time they can see where they are in the application process, which will get them more engaged with the whole team. I hope you take a look at the site and maybe we will see you at the meeting!

![alt text](static/img/responsive.jpg)

## Contents
1. [UX](#UX)
2. [Features](#Features)
3. [Technologies Used](#Technologies-Used)
4. [Testing](#Testing)
5. [Deployment](#Deployment)
6. [Credits](#Credits)

## UX

### Project Goals
[BOS UP](https://jobboard-milestone3.herokuapp.com/) is part of my Code Institute Full Stack Software Development course, the Data Centric Development module. The scope for this milestone project is to "Build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain." So I created a jobboard where visitors can access the vacancies and register, candidates can login and apply and admins can admin. All CRUD operations are implemented in the site, where I made a distinctive choice about what user can do which operation. The target audience is for people around all ages who are looking for a job in our branche (utility sector).

### User stories
<details>
<summary>General website user (visitor)</summary>

1. As a visitor, I want to be able to see which vacancies are available at the company
2. As a visitor, I want to be able to see general information about the company so I get a 'feel' about the corporate culture
3. As a visitor, I want to be able to register so I can get a log in for the site
4. As a visitor, I want to be able to get in contact so I can get more information about a partically subject

</details>
<details>
<summary>Candidate (logged in) user</summary>

1. As a user, I want to be able to log in my user environment so I can see all information applicable to me
2. As a user, I want to be able to log out my user environment
3. As a user, I want to be able to see which vacancies are available at the company, so I can apply to them
4. As a user, I want to be able to apply to a open vacancy, so I can join the company
5. As a user, I want to be able to see my application history, so I can know which applications are still ongoing
6. As a user, I want to be able to change my profile information, so this is up to date
7. As a user, I want to be able to change my password
</details>
<details>
<summary>Administrator</summary>

1. As the admin, I want to be able to see and do all the user stories of a logged in user so I can control the data and the environment
2. As the admin, I want to be able to have an overview of vacancies, applications and user in the environment
3. As the admin, I want to be able to add vacancies so that they are available for website and candidate user
4. As the admin, I want to be able to close, edit and delete vacancies
5. As the admin, I want to be able to add applications for candidates and vacancies so that they are available for the candidate user
6. As the admin, I want to be able to close, edit and delete applications
7. As the admin, I want to be able to add users so that I can give candidates login credentials
8. As the admin, I want to be able to approve new registrations so no one can get access without permission/controle
9. As the admin, I want to be able to delete user so that they cannot login anymore
10. As the admin, I don't want other people to be able to use pages from where changes to the database can be made.

</details>

### WireFrames
During the project I got a lot of feedback and strayed away from the initial wireframes. The login, register and contct pages are replaced by modals instead of the initial pages.
<details>
<summary>Home Page</summary>
<br>

<p>Visitor</p>

![Home Page Visitor](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/index_visitor.html.png?raw=true)

<p>User</p>

![Home Page User](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/index_user.html.png?raw=true)

<p>Admin</p>

![Home Page Admin](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/index_admin.html.png?raw=true)

</details>

<details>
<summary>Vacancies</summary>
<br>

<p>Visitor</p>

![Vacancies Page Visitor](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/vacancies_visitor.html.png?raw=true)

<p>User</p>

![Vacancies Page User](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/vacancies_user.html.png?raw=true)

<p>Admin</p>

![Vacancies Page Admin](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/vacancies_admin.html.png?raw=true)

<p>Admin add vacancy</p>

![Add Vacancy Page Admin](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/add_vacancy_admin.html.png?raw=true)

<p>Admin edit vacancy</p>

![Edit Vacancy Page Admin](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/edit_vacancy_admin.html.png?raw=true)
</details>

<details>
<summary>Applications</summary>
<br>
<p>User</p>

![Applications Page User](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/applications_user.html.png?raw=true)

<p>User Add Application</p>

![Applications Page User](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/add_application_user.html.png?raw=true)

<p>Admin</p>

![Applications Page Admin](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/applications_admin.html.png?raw=true)

<p>Admin Add Application</p>

![Applications Page Admin](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/add_application_admin.html.png?raw=true)

<p>Admin Edit Application</p>

![Applications Page Admin](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/edit_application_admin.html.png?raw=true)

</details>
<details>
<summary>Users</summary>
<br>
<p>User Profile</p>

![Profile Page User](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/profile_user.html.png?raw=true)

<p>User Edit User</p>

![Edit User Page Admin](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/edit_user_user.html.png?raw=true)

<p>Admin</p>

![Users Page Admin](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/users_admin.html.png?raw=true)

<p>Admin Add User</p>

![Users Page Admin](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/add_user_admin.html.png?raw=true)

<p>Admin Edit User</p>

![Users Page Admin](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/edit_user_admin.html.png?raw=true)

</details>

<details>
<summary>Contact</summary>
<br>
<p>All</p>

![Contact Page User](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/contact_visitor.html.png?raw=true)

</details>

<details>
<summary>Register</summary>
<br>
<p>Visitor</p>

![Register Page Visitor](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/register_visitor.html.png?raw=true)

</details>

<details>
<summary>Login</summary>
<br>
<p>Visitor</p>

![Login Page Visitor](https://github.com/VolkovBos/milestone3_jobboard/blob/master/wireframes/login_visitor.html.png?raw=true)

</details>

### Design
<ins>Color Scheme</ins><br/>
The color scheme is chosen because of the corporate identity of BOS UP, which contains a blue pallet of colors.

The two most important colors are lightskyblue and cadetblue. To make the site easy to read, I used these two colors on the most pages. For buttons I used custom bootstrap design, to let them stand out. For instance; I do want to make the delete button red!

- ![#5F9EA0](https://placehold.it/15/5F9EA0/000000?text=+) `#5F9EA0 - CadetBlue`
- ![#87CEFA](https://placehold.it/15/87CEFA/000000?text=+) `#87CEFA - LightSkyBlue`

For texts I used three main colors; the standard black, a grey one and a white one. I used the standard and the grey to get a bit of contrast between them. The white one is for sections where the background is darker, for instance a jumbotron.
- ![#000000](https://placehold.it/15/000000/000000?text=+) `#000000 - Black`
- ![#777777](https://placehold.it/15/777777/000000?text=+) `#777777 - Grey`
- ![#FAFAFA](https://placehold.it/15/FAFAFA/000000?text=+) `#FAFAFA - Offset white`

I used a body background color for contrast so cards and tables stand out more, also this gives a less cheaper and easier on the eye look to the site.
- ![#E2E8F0](https://placehold.it/15/E2E8F0/000000?text=+) `#E2E8F0 - very light grey `

For error messages I used a yellow background to really stand out.

<ins>Typography</ins><br/>
The font I selected to this page is Play from [GoogleFonts](https://fonts.google.com/), because it is professional but not as common used. The font is simple but yet adds some character.


### Database
This website has a [MongoDB](https://www.mongodb.com) databases called jobboard_milestone3, within this database I've used 5 tables (or collections). I used [MongoDB](https://www.mongodb.com) on advise of my mentor and CodeInstitute for this project and for this phase of the development of the website this works fine. However I must add; whenever expanding your business processes further in this portal, I would highly recommend taking a new look to your chosen database. For example if you want to add more HR and employee processes it is my advice to do this with an relationship based database.

#### Tables
The most tables are self explanatory, but I consciously chose to use one table for candidates and users due to the size of the project and the simplicity of the current business processes. I allready created a profiles table, this simplifies editing or creating a new user by the admin and prevents a typo but also this anticipates on the possibility of implementing new user profiles. 

#### Tables design
<details>
<summary>Vacancies</summary>
<br>

![Vacancies](https://github.com/VolkovBos/milestone3_jobboard/blob/master/static/img/Vacancy_table.jpg?raw=true)

</details>
<details>
<summary>Candidates/users</summary>
<br>

![Candidates/users](https://github.com/VolkovBos/milestone3_jobboard/blob/master/static/img/Candidate_table.jpg?raw=true)

</details><details>
<summary>Application</summary>
<br>

![Application](https://github.com/VolkovBos/milestone3_jobboard/blob/master/static/img/Application_table.jpg?raw=true)

</details><details>
<summary>Statusses</summary>
<br>

![Statusses](https://github.com/VolkovBos/milestone3_jobboard/blob/master/static/img/Statusses_table.jpg?raw=true)

</details><details>
<summary>Profiles</summary>
<br>

![Profiles](https://github.com/VolkovBos/milestone3_jobboard/blob/master/static/img/Profiles_table.jpg?raw=true)

</details>

## Features

### Existing Features
- [x] Vacancies on site
- [x] Registration form
- [x] Login form
- [x] Hashed passwords
- [x] Contact form
- [x] Login for candidates
- [x] Admin environment
- [x] CRUD Vacancies
- [x] CRUD Applications
- [x] Approve new registrated users
- [x] Close Vacancies and/or Applications
- [x] Change password
- [x] Profile section
- [x] Quick action menu
- [x] 403, 404, 500 Error handling (and pages)
- [x] CRUD Users/candidates

### Features Left to Implement
- [ ] Trashbin
- [ ] CRUD Status and profiles
- [ ] Manual search option
- [ ] Cloning of records
- [ ] Forgot password
- [ ] Userprofile: office employee

## Technologies Used
I have used the following technologys for this project:

### Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML5), Semantic markup language as the shell of the site
* [CSS3](https://en.wikipedia.org/wiki/CSS), Cascading Style Sheets as the design of the site
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript), for the contact form and preventing prefilled forms
* [jQuery](https://jquery.com/), for some initializing and support of [Materialize](https://materializecss.com/)
* [Python](https://www.python.org), for the backend
    - Flask, for custom functions
    - flask_pymongo for connection to my [MongoDB](https://www.mongodb.com)
    - bson.objectid
    - werkzeug.security, for hashed passwords
    - functools, for my own view decorators
* [BSON](https://en.wikipedia.org/wiki/BSON), to store my data

### Apps, Api
* [MongoDB](https://www.mongodb.com), for my database
* [Heroku](https://heroku.com), to deploy my app
* [Gitpod](https://gitpod.io), for development
* [Github](https://github.com), for version control
* [EmailJS](https://www.emailjs.com/), to let the user be able to contact me
* [Balsamiq](https://balsamiq.com/wireframes/desktop/), for creating the wireframes
* [TinyPNG](https://tinypng.com/), for reducing the filesizes on my images

### Framework
* [Materialize](https://materializecss.com/), for icons
* [Bootstrap](https://getbootstrap.com/), for CSS and HTML framework for ex. modals
* [Bootstrap Icons](https://icons.getbootstrap.com/), for icons
* [Google Fonts](https://fonts.google.com/), to choose and combine my fonts

### Resources
* [Iconmonstr](https://iconmonstr.com/), for social svg images
* [Encycolorpedia](https://encycolorpedia.nl/), for coloring the svg images
* [Unsplash](https://unsplash.com/), for images

## Testing

### Error pages
I tested the 404 error with [seositecheckup](https://seositecheckup.com/seo-audit/custom-404-error-page-test/jobboard-milestone3.herokuapp.com). Further more I tested these page by temporary using abort(nr) in a view to see if it would redirect correctly.

### Validators
To make sure there where nog syntax errors, I've used the following validators on my pages:
* [HTML validator](https://validator.w3.org/#validate_by_input)
* [CSS validator](https://jigsaw.w3.org/css-validator/)
* [PEP8](http://pep8online.com/checkresult)

### Testing User Stories
- Visitor
    1. As a visitor, I want to be able to see which vacancies are available at the company
        - By using the navigation menu I can visit the vacancies page to see the open vacancies
    2. As a visitor, I want to be able to see general information about the company so I get a 'feel' about the corporate culture
    3. As a visitor, I want to be able to register so I can get a log in for the site
        - By using the navigation menu I can visit the register page to register me as a candidate/user
    4. As a visitor, I want to be able to get in contact so I can get more information about a partically subject
        - I can use the menu to go to the contact page.
        - On the contact page I can fill in my name e-mailadress and message.
        - The contact form will let me know all fields are manditory.
        - I can send in the form by clicking the Submit button.

### Login/Register Validation
There are some login checks with error message shown, you will get redirected to the index page and the message is shown in the top off the page. The error with message:
- Wrong password; "Your password is incorrect"
- User isn't approved yet by admin; "Your registration is not processed yet"
- User isn't approved yet by admin; "This user is inactive, please contact the administrator"
- Username is incorrect; "The username provided is not known"

Registration; the error with message:
- Username exists; "{username} already exists! Please choose a different username."
- User isn't created; "There was a problem saving your registration. If this happens again, please use the contactform to contact the administrator of the website."
- Two different passwords; "Passwords are not identical. Please try again."
- Username is shorter then 8 characters; "Username should be at least 8 characters"

If the registration is a succes you will get the message:"Your registration is saved, we will get in touch with you."

### Unittesting
For the Unittests I focussed mostly on authorisation, page loads and the error pages. Besides this I also tested the login, logout and register functionality. Because of time I chose to do test the button, actions, queries and database modifiers in the user storie testing. 

### Further testing
* Tested this website on laptop and mobile.
* Tested this website on Google Chrome, Firefox and Safari browsers.
* I've asked colleagues and friends to give feedback.
* I've asked for peer reviews on Slack.
* During testing I used "inspect" function on different OS, devices and browsers.


### Issues found (all solved)
* When implementing the sidebar nav form materialize I came accross the issue that the sidebar was greyed out. I found the solution [here](https://github.com/Dogfalo/materialize/issues/3844)
* Visitors and users can see urls from which they should have no access rights. I wouldn't want to solve this with several if-else statements in every route/view. So I asked arround and with a little help I created my own decorator for this. 


## Deployment
This project was created using Github, from there I used Gitpod to write my code.
Then I used commits to git followed by pushes to my GitHub repository.
I've deployed this project to Heroku and used automated pushes to make sure my pushes to GitHub were also made to Heroku.
For deployment on Heroku I've used the following steps:
* Using the terminal command pip freeze > requirements.txt I have created a requirements.txt file.
* Using the terminal command echo web: python app.py > Procfile I have created a procfile.
* I've used git add, git commit and git push to push the requirements and procfile to GitHub.
* I've created a new app on the Heroku website by using the "new" button on my dashboard.
* I gave the app a name of jobboard-milestone3 and set the region to Europe.
* From the Heroku dashboard I've clicked "Deploy" > "Deployment method" and selected GitHub.
* Confirm the linking of the Heroku app to the correct GitHub repository.
* In the Heroku dashboard I've clicked "Settings" > "Reveal Config Vars".
* I've added the config vars for my IP, PORT, MONGO_URI and SECRET_KEY.
* In the "Manual Deployment" section of this page I've made sure the master branch is selected and I've clicked "Deploy Branch".
* The site was now successfully deployed.

### MongoDB
Create a MongoDB database with the tables(collections):
- applications
- candidates
- profiles
- status
- vacancies

Then you can use below code to create the first admin user. From there on, you can use the site to add, modify or delete users.

```
import os
from flask import Flask
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash

app = Flask(__name__)
MONGO_URI = "mongodb+srv://root:<PASSWORD_MONGODB>@myfirstcluster.vwkuk.mongodb.net/<NAME_MONGODB>?retryWrites=true&w=majority"
app.config["MONGO_DBNAME"] = '<NAME_MONGODB>'
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)

username = 'TESTROBBERT'
user_password = 'TESTROBBERT'
email = 'bos@bos.bos'
hash_pass = generate_password_hash(user_password)

mongo.db.candidates.insert_one(
    {
        'user_name': username,
        'email': email,
        'password': hash_pass,
        'approved': True,
        'status': 'active',
        'profile': 'admin',
        'user_id': 1
    }
)
```

### Env.py
In Gitpod I used a env.py file for my settings of the site, connection to [MongoDB](https://www.mongodb.com). I also used this for the Flask Unittests. I used the code below (with <> substituted for my string).

```
import os

os.environ["MONGO_URI"] = "mongodb+srv://root:<PASSWORD_MONGODB>@myfirstcluster.vwkuk.mongodb.net/<NAME_MONGODB>?retryWrites=true&w=majority"
os.environ["SECRET_KEY"] = "justtasecretkeyforme"

# For testing
os.environ["USERNAME_ADMIN"] = '<USERNAME_ADMIN>'
os.environ["USERNAME_USER"] = '<USERNAME_USER>'
os.environ["SPW_ONE"] = '<PASSWORD_ADMIN>'
os.environ["SPW_TWO"] = '<PASSWORD_USER>'
```

### For my assessors
03-10-2020 :<br>
I had an issue with my credentials appearing in cached Python files/folders. So I had to remove the <span>__ Pycache __</span> folder and all history. I did this with:
```
git filter-branch --tree-filter 'rm -f __Pycache__/*' -- --all
git push force
```

## Credits
### Content
The idea, content and development for this project was written or designed by myself.

### Media
The logo was designed en made by myself. 
I used images from [Unsplash](https://unsplash.com/) throughout my site.

Thanks to:
[Albert Dera](https://unsplash.com/@albertdera), for a profile image
[Clem Onojeghuo](https://unsplash.com/@clemono), for a vacancy image
[Florian Olivio](https://unsplash.com/@florianolv), for a vacancy image
[Glenn Carstens-Peters](https://unsplash.com/@glenncarstenspeters), for a vacancy image
[Jimmy Fermin](https://unsplash.com/@jimmyferminphotography), for a profile image
[Marvin Meyer](https://unsplash.com/@marvelous), for the main index background image
[Shahadat Rahman](https://unsplash.com/@hishahadat), for a vacancy image

### Acknowledgements
Thanks to [Tim (Justim)](https://github.com/justim) for some deeper explanation about Python views and decorators. Helped me with the login view decorator.

Specail thanks to [Paul Friel](https://github.com/Spagettileg) who repeatedly and thoroughly gave me feedback on my site during the project.

And a thanks to my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) who gave me honest and good feedback on my site/code and helped me te complete this project.

[w3schools](https://www.w3schools.com/) and [StackOverflow](https://stackoverflow.com/) for research.