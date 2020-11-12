# BOS UP jobboard

## Introduction
Welcome to [BOS UP](https://jobboard-milestone3.herokuapp.com/)! This site is created to let potential candidates know who we are and what we do. And also we want to give the option to see if they want to come and join us! If a candidate registers on our site and our recruiter has had contact with them, the candidate can apply on several cool and interesting vacancies. At all time they can see where they are in the application process, which will get them more engaged with the whole team. I hope you take a look at the site and maybe we will see you at the meeting!

![Website design](static/img/responsive.jpg)

## Contents
1. [UX](#UX)
     - [Project Goals](#project-goals)
     - [User Stories](#user-stories)
     - [Wireframes](#wireframes)
     - [Design](#design)
     - [Database](#database)
        - [Tables](#tables)
        - [Tables design](#tables-design)
2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
3. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Apps-Api](#apps-api)
    - [Framework](#framework)
    - [Resources](#resources)
4. [Testing](#testing)
5. [Deployment](#deployment)
    - [MongoDB](#mongodb)
    - [Env.py](#env-py)
    - [For my assessors](#for-my-assessors)
6. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

## UX

### Project Goals
[BOS UP](https://jobboard-milestone3.herokuapp.com/) is part of my Code Institute Full Stack Software Development course, the Data Centric Development module. The scope for this milestone project is to "Build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain." So I created a jobboard where visitors can access the vacancies and register, candidates can login and apply and admins can admin. All CRUD operations are implemented in the site, where I made a distinctive choice about what user can do which operation. The target audience is for people around all ages who are looking for a job in our branche (utility sector).

### User Stories
<details>
<summary>General website user (visitor)</summary>

1. As a visitor, I want to be able to see general information about the company so I get a 'feel' about the corporate culture
2. As a visitor, I want to be able to see which vacancies are available at the company
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
6. As a user, I want to be able to see and change my profile information, so this is up to date
7. As a user, I want to be able to change my password
</details>
<details>
<summary>Administrator</summary>

1. As the admin, I want to be able to see and do all the user stories of a logged in user so I can perform regular actions.
2. As the admin, I want to be able to have an overview of vacancies, applications and user in the environment.
3. As the admin, I want to be able to add, close, edit and delete vacancies so that I can controle the content available for website and candidate users.
4. As the admin, I want to be able to add, close, edit and delete applications for candidates and vacancies that I can controle the content. available for website and candidate users
5. As the admin, I want to be able to add, deactivate, edit and delete users so that I can give candidates login credentials.
6. As the admin, I want to be able to approve new registrations so no one can get access without permission/controle.
7. As the admin, I don't want other profiles to be able to use pages from where important changes to the database can be made

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

#### Schema design
![Tables overview](schema/Schema.jpg)

## Features
All the features were developed with dynamic user content with appropriate restrictions. Features like create, update, delete, approve are hidden behind a registration wall or login portal, but this do not hinder visitors from viewing the overall content.

### Existing Features

#### Home Page + Footer (all users)
The Home page includes login and registration menu at the very top, you can see the general info about the company. In the navigation menu you have an option to search through all vacancies, this search will check the text, job title and location of all vacancies.
In the footer you'll find a contact option which gives you the option to send a email to the admin of the website. Also you'll find social links of the company and a link to the github page of the admin who created this website.

#### Contact
In the footer and on several places in the website there are links which open a contact modal. From here you can send an email to the owner of the website. The user wil receive a confirmation email that the message is sent.

#### Register
A visitor of the site can use the 'Register' option in the navigation menu to register for a login. This will open a modal where he can input some required fields and submit. Errorsmessages are shown when the visitor triggers an error and he'll get a success message if the registration is successful.

#### Login
A visitor of the site can use the 'Login' option in the navigation menu to login the website. This will open a modal where he can input some required fields and login with his credentials. Errorsmessages are shown when the visitor triggers an error.

#### Passwords
All use of passwords are secure and hashed. This is used for login, register and change password functions.

#### Vacancies
##### Vistors
The Vacancies page shows all vacancies which are not closed on cards with a nice header image. The page and vacancies are created based on call-2-action, so you'll find buttons to the contact modal.

##### User (logged in)
In stead off the contact buttons on vacancies on the visitor side of the site, users have the option to apply to a vacancy.

##### Admin (logged in)
Admins have the availability to add, edit or delete vacancies by using one of the buttons. They also have a button to direct 'Close' a vacancy and move this to the closed section. The button for creating a application is called application for an admin because they don't apply do the vacancies not as a candidate user.


#### Add & Edit Vacancy
##### Admin (logged in)
From the Vacancies page admins can add a new vacancy. On the Add Vacancy page the status and select photo fields are filled with records of setup tables. When changing the photo option, a preview of the photo will load on the page.

#### Applications
##### User (logged in)
The My Applications page shows all application of the candidate user on cards with a nice header image.

##### Admin (logged in)
Admins have the availability to add, edit or delete application by using one of the buttons. They also have a button to direct 'Close' a application and move this to the closed section. On the cards there is an extra header with the candidate name for the admins available.

#### Add & Edit Application
##### User (logged in)
From the Vacancies page users can apply to a vacancy. On the Add Application page the data of the vacancy is not changeable by the user only his availability date and comments can be changed. The Edit Application page is not available for candidate users.

##### Admin (logged in)
From the Vacancies page admins can add a new vacancy. On the Add Application page all the fields which were available on the Vacancy are prefilled. An admin can change these fields however on the appication, depending on which agreements were made with the candidate.
The status and select photo fields are filled with records of setup tables. When changing the photo option, a preview of the photo will load on the page. The job title and candidate name fields are filled with all options in those respectively tables. Closed and inactive records however are shown on the bottom of the selection with a seperator.
<br>
From the Applications page there is no vacancy data available from the start, so those fields aren't set or available yet. This is more a quick action for the admin.
<br>
When changing the vacancy on a application the data from the vacancy will be loaded to the application.

#### Profile
##### User & Admin(logged in)
Clicking on the name in the navigation menu, a user can open his user profile. On the Profile page you get sevral blocks of information, each designed for a specific goal. On the generic card are buttons for edit and change password and if available a profile photo of the candidate.

#### Users
##### Admin (logged in)
In the navigation menu the admin has the option 'Users'. On this page the admin can control who has access to the website. There is a button to manually add an user and there are three sections of users:
1. Users asking for approval; these are user which have registrated themselves on the wesite. A admin can either choose to approve or delete them using the buttons. Approving will set the user to the active users section.
2. Active user; these users can log on to the website. Either with admin or user privileges.
3. Inactive users; these users are set on inactive and cannot log on to the website anymore.

#### Edit user
##### User (logged in)
From the userprofile a user can click on the 'Edit' button to open the 'Edit Profile' page. Here he can change al his data except for the user account and save. He can also fill in a url for a profile photo and if he wants use the 'Load image' button for a preview.

##### Admin (logged in)
From the 'Users' page a admin can open a userprofile by clicking on the username or use the 'Edit' button, which is only available with active users. From both he opens the 'Edit Profile' page of that specific user. An admin can in addition to a user also change the user account info.

#### Add user
##### Admin (logged in)
From the users page an admin can use the 'Add User' button to open the 'Add User' page. Here he can fill in al his data. He can also fill in a url for a profile photo and if he wants use the 'Load image' button for a preview.


#### Change password
##### User & Admin (logged in)
From the profile page a user can change his password by using the 'Change Password' button. This opens a modal in which he can fill in his current password and a new one. A confirmation of the new password is required to prevent typos.


#### Setup
##### Admin (logged in)
In the navigation menu the admin has the option 'Setup'. On the 'Setup' page the admin can control fields or rather processes on the website. He can add, change or delete statusses and images as long as they are not required for running the website. A section for profiles is also added but additional functionality behind this is not yet added.

#### Error handling pages
##### All users
When stumbling on a 403, 404 or 500 error a visitor or user will be redirected to an error page. These pages are also used when some profile is trying to open a view for which he doesn't have the access rights for.

#### Logout
##### User & Admin (logged in)
A logged in user of the site can use the logout icon in the navigation menu to logout the site. When clicking on the icon the user (becomes a visitor and) gets redirected to the homepage.

### Features Left to Implement
- Trashbin; before finally deleting items I would like to implement a trash bin for admins.
- Cloning of records; a quick action which allows for fast duplication a record and changing some fields.
- Forgot password
- New/Other userprofiles; more selections on user level rights and delegating processes. For instance a office employee who can manage the vacancies and applications sections of the website.

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

### Apps-Api
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
See the [Testing MD file](TESTS.md)

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
- photos
- profiles
- status
- vacancies

Then you can use below code to create the first setup. The profiles are needed for a check on autorisation level and the statuses are needed for querying the database. Users and statuses can later be added by an admin user to use in selection fields, but not mandatory. As of yet profiles are static managed.

```
import os
from flask import Flask
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash

app = Flask(__name__)
MONGO_URI = "mongodb+srv://root:bos77@myfirstcluster.vwkuk.mongodb.net/jobboard_milestone3?retryWrites=true&w=majority"
app.config["MONGO_DBNAME"] = '<NAME_MONGODB>'
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)

username_admin = '<TEST_USER_ADMIN>'
password_admin = '<TEST_PASSWORD_ADMIN>'
username_user = '<TEST_USER_USER>'
password_user = '<TEST_PASSWORD_USER>'

hash_pass_admin = generate_password_hash(password_admin)
hash_pass_user = generate_password_hash(password_user)

mongo.db.candidates.insert_many([
    {
        'user_name': username_admin,
        'password': hash_pass_admin,
        'approved': True,
        'status': 'active',
        'profile': 'admin',
        'user_id': 11
    },
    {
        'user_name': username_user,
        'password': hash_pass_user,
        'approved': True,
        'status': 'active',
        'profile': 'user',
        'user_id': 12
    },
])
mongo.db.profiles.insert_many([
    {
        'name': 'admin'
    },
    {
        'name': 'user'
    }
])
mongo.db.statuses.insert_many([
    {
        'status_name': 'closed',
        'type': 'application'
    },
    {
        'status_name': 'closed',
        'type':'vacancy'
    },
    {
        'status_name': 'active',
        'type':'user'
    },
    {
        'status_name': 'inactive',
        'type':'user'
    }
])
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

Also I want to point out that more atomic commits are not possible for me with the use of Gitpod. During the course I experienced some 20+ issues thus far regarding 503 errors. 

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

Special thanks to [Paul Friel](https://github.com/Spagettileg) who repeatedly and thoroughly gave me feedback on my site during the project.

And a thanks to my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) who gave me honest and good feedback on my site/code and helped me te complete this project.

[w3schools](https://www.w3schools.com/) and [StackOverflow](https://stackoverflow.com/) for research.
