# BOS UP jobboard - Milestone Project 3

## Introduction
Welcome to [BOS UP](https://jobboard-milestone3.herokuapp.com/)! This site was created to get more interactive with our candidate and give them insights in the status of our vacancies and ongoing applications.

![alt text](static/img/responsive.jpg)

## Contents
1. [UX](#UX)
2. [Features](#Features)
3. [Technologies Used](#Technologies-Used)
4. [Testing](#Testing)
5. [Deployment](#Deployment)
6. [Credits](#Credits)

## UX

### User stories
- <ins>General website user (visitor)</ins>
    - As a visitor, I want to be able to see which vacancies are available at the company
    - As a visitor, I want to be able to see general information about the company so I get a 'feel' about the corporate culture
    - As a visitor, I want to be able to register so I can get a log in for the site
    - As a visitor, I want to be able to get in contact so I can get more information about a partically subject

- <ins>Candidate (logged in) user</ins>
    - As a user, I want to be able to log in my user environment so I can see all information applicable to me
    - As a user, I want to be able to log out my user environment
    - As a user, I want to be able to see which vacancies are available at the company, so I can apply to them
    - As a user, I want to be able to apply to a open vacancy, so I can join the company
    - As a user, I want to be able to see my application history, so I can know which applications are still ongoing
    - As a user, I want to be able to change my profile information, so this is up to date
    - As a user, I want to be able to change my password

- <ins>Administrator</ins>
    - As the admin, I want to be able to see and do all the user stories of a logged in user so I can control the data and the environment
    - As the admin, I want to be able to have an overview of vacancies, applications and user in the environment
    - As the admin, I want to be able to add vacancies so that they are available for website and candidate user
    - As the admin, I want to be able to close, edit and delete vacancies
    - As the admin, I want to be able to add applications for candidates and vacancies so that they are available for the candidate user
    - As the admin, I want to be able to close, edit and delete applications
    - As the admin, I want to be able to add users so that I can give candidates login credentials
    - As the admin, I want to be able to approve new registrations so no one can get access without permission/controle
    - As the admin, I want to be able to delete user so that they cannot login anymore
    - As the admin, I don't want other people to be able to use pages from where changes to the database can be made.

### WireFrames
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

<ins>Typography</ins><br/>
The font Barrio is chosen in the corporate identity so I used this on the logo. To get a nice contrast with this I chose for Montserrat for the main font on the website. The font is simple but yet adds some character.

<ins>Images</ins><br/>
Because the company is a startup there are no images available just yet. And also the goal of the site is more for recruitment processes and connection with the candidates then a global PR of the company. Maybe in the near future this can be adjusted due to growth.

### Database
This website has a MongoDb databases called jobboard_milestone3, within this database I've used 5 tables (or collections). I used MongoDb on advise of my mentor and CodeInstitute for this project and for this phase of the development of the website this works fine. However I must add; whenever expanding your business processes further in this portal, I would highly recommend taking a new look to your chosen database. For example if you want to add more HR and employee processes it is my advice to do this with an relationship based database.

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
* [HTML5](https://en.wikipedia.org/wiki/HTML5), Semantic markup language as the shell of the site
* [CSS3](https://en.wikipedia.org/wiki/CSS), Cascading Style Sheets as the design of the site
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript), for the contact form and preventing prefilled forms
* [jQuery](https://jquery.com/), for some initializing and support of [Materialize](https://materializecss.com/)
* [Python](https://www.python.org), for the backend
    - Flask, for custom functions
    - Pymongo, for connection to my [MongoDB](https://www.mongodb.com)
    - bson.objectid
    - werkzeug.security, for hashed passwords
* [MongoDB](https://www.mongodb.com), for my database
* [BSON](https://en.wikipedia.org/wiki/BSON), to store my data
* [Heroku](https://heroku.com), to deploy my app
* [Gitpod](https://gitpod.io), for development
* [Github](https://github.com), for version control
* [Materialize](https://materializecss.com/), to make my website responsive, mobile-first and have some out-of-the-box functionalities
* [Google Fonts](https://fonts.google.com/), to choose and combine my fonts
* [EmailJS](https://www.emailjs.com/), to let the user be able to contact me
* [Balsamiq](https://balsamiq.com/wireframes/desktop/), for creating the wireframes

## Testing

### Error pages
I tested the 404 error with [seositecheckup](https://seositecheckup.com/seo-audit/custom-404-error-page-test/jobboard-milestone3.herokuapp.com)

### Issues found
When implementing the sidebar nav form materialize I came accross the issue that the sidebar was greyed out. I found the solution here:<br>
https://github.com/Dogfalo/materialize/issues/3844



## Deployment
03-10-2020 :<br>
I had an issue with my credentials appearing in cached Python files/folders. So I had to remove the <span>__ Pycache __</span> folder and all history. I did this with:
```
git filter-branch --tree-filter 'rm -f __Pycache__/*' -- --all
git push force
```

## Credits