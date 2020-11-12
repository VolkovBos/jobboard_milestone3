1. [Testing](#testing)
    - [Error pages](#error-pages)
    - [Validators](#validators)
    - [Testing User Stories](#testing-user-stories)
    - [Login-Register Validation](#login-register-validation)
    - [Unittesting](#unittesting)
    - [Further testing](#further-testing)
    - [Issues found (all solved)](#issues-found-all-solved)
    
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
    1. As a visitor, I want to be able to see general information about the company so I get a 'feel' about the corporate culture:
        - By using the navbar menu I can visit the Home page to see the main page.
    2. As a visitor, I want to be able to see which vacancies are available at the company:
        - By using the navigation menu I can visit the Vacancies page to see the open vacancies.
        - By using the search field in the navbar I can find vacancies with a quick search function on name, text or location.
    3. As a visitor, I want to be able to register so I can get a log in for the site:
        - By using the navigation menu I can open the Register modal to register me as a candidate/user.
        - I will get error messages on the Home page if my registration isn't processed.
        - I will get a succes message on the Home page if my egistration is processed.
    4. As a visitor, I want to be able to get in contact so I can get more information about a partically subject:
        - I can use the menu to go to open the Contact modal.
        - On the Contact modal I can fill in my name e-mailadress and message.
        - The contact form will let me know all fields are manditory.
        - I can send in the form by clicking the Submit button.


- User (candidate logged in)
    1. As the user, I want to be able to see and do all the user stories of a visitor:
        - See user stories visitor
    2. As a user, I want to be able to log in my user environment so I can see all information applicable to me:
        - By clicking the login button in the menu I will open the login modal.
        - As an user I can login by using my own username and personal password.
        - The form will let me know both fields are mandetory.
        - I will get error messages on the Home page if my login isn't processed.
        - I will be redirected to the Home page and my navbar will show My Application and my name to confirm I'm logged in.
    3. As a user, I want to be able to log out my user environment:
        - When I'm logged in I can logout by using the logout button in the navigation menu.
        - I will be redirected to the Home page and My Application and my name will dissappear form the navbar.
    4. As a user, I want to be able to apply to a open vacancy, so I can join the company:
        - By navigating to the Vacancies page I can use the 'Apply to this vacancy!' button on a vacancy to apply to that vacancy.
        - On the Application page I can fill in my availbility date and add some personal comments.
        - I also see some brief information of the vacancy.
        - I can Save to apply and get redirected to My Application.
        - I can Cancel and get redirected back to Open Vacancies.
    5. As a user, I want to be able to see my application history, so I can know which applications are still ongoing:
        - By using the navigation menu I can visit the My Applications page to see all of my applications.
    6. As a user, I want to be able to see and change my profile information, so this is up to date:
        - By using the navigation menu I can visit my Profile page by clicking on my name.
        - Here I can see all of my profile information:
            - User information
            - Photo
            - Candidate information
            - Address information
            - Social sites
            - Skills
        - I can edit my profile by clicking on the edit button.
        - On the Edit Profile page I can change my info and either:
            - Save, this will save changes and go back to my profile.
            - Cancel, this will ignore my changes and go back to my profile.
    7. As a user, I want to be able to change my password:
        - By using the navigation menu I can visit my Profile page by clicking on my name.
        - I can change my password by clicking on the Change password button to open a modal.
        - On the Change Password modal I can fill in my old and new password as well as a confirmation of the new password.
        - The contact form will let me know all fields are manditory.
        - I can save my change in the form by clicking the Save button.


- Admin
    1. As the admin, I want to be able to see and do all the user stories of a logged in user so I can perform regular actions:
        - See user stories user
    2. As the admin, I want to be able to have an overview of vacancies, applications and users in the environment:
        - By using the navigation menu I can visit the Vacancies page to see all the vacancies.
        - By using the navigation menu I can visit the Applications page to see all the applications.
        - By using the navigation menu I can visit the Users page to see all the users.
    3. As the admin, I want to be able to add, close, edit and delete vacancies so that I can controle the content available for website and candidate users:
        - By navigating to the Vacancies page I can use the 'Add Vacancy' button on top of the page.
            - On the Add Vacancy page I can fill in all fields for a new vacancy.
            - I also select a picture which will be the header of the vacancy card.
            - On the Add Vacancy page I can either:
                - Save, this will add the new vacancy and go back to the Vacancies page.
                - Cancel, this will ignore my input and go back to the Vacancies page.
        - By navigating to the Vacancies page I can use the 'Edit' button on a specific vacancy.
            - On the Edit Vacancy page I can change the vacancy info and either:
                - Save, this will save changes and go back to the Vacancies page.
                - Update, this will save changes and stay on this page.
                - Cancel, this will ignore my changes and go back to the Vacancies page.
        - By navigating to the Vacancies page I can use the 'Close' button on a specific vacancy.
            - I will see the vacancy moved to the Closed Vacancies section at the bottom of the page.
        - By navigating to the Vacancies page I can use the 'Delete' button on a specific vacancy.
            - I will see the vacancy removed from the page.
    4. As the admin, I want to be able to add, close, edit and delete applications for candidates and vacancies so that they are available for the candidate user:
        - I can create an application the same as a user can from a vacancy, only the button the vacancy has the name 'Application' (see user storie user)
        - By navigating to the Application page I can use the 'Add Application' button on top of the page.
            - On the Add Application page I can fill in all fields for a new application.
            - On the Add Application page I can either:
                - Save, this will add the new application and go back to the Applications page.
                - Cancel, this will ignore my input and go back to the Applications page.
        - By navigating to the Applications page I can use the 'Edit' button on a specific application.
            - On the Edit Application page I can change the application info and either:
                - Save, this will save changes and go back to the Applications page.
                - Cancel, this will ignore my changes and go back to the Applications page.
        - By navigating to the Applications page I can use the 'Close' button on a specific application.
            - I will see the application moved to the Closed Applications section at the bottom of the page.
        - By navigating to the Applications page I can use the 'Delete' button on a specific application.
            - I will see the application removed from the page.
    5. As the admin, I want to be able to add, deactivate, edit and delete users so that I can give candidates login credentials:
        - By navigating to the Users page I can use the 'Add User' button on the page.
            - On the Add User page I can fill in all fields for a new user.
            - On the Add User page I can either:
                - Save, this will add the new user and go back to the Users page.
                - Cancel, this will ignore my input and go back to the Users page.
        - By navigating to the Users page I can use the 'Edit' button on a specific user if the user is active.
            - On the Edit User page I can change the user info and either:
                - Save, this will save changes and go back to the Users page.
                - Cancel, this will ignore my changes and go back to the Users page.
        - By navigating to the Users page I can use the 'Deactivate' button on a specific user if the user is active.
            - I will see the user moved to the Inactive Users section at the bottom of the page.
        - By navigating to the Users page I can use the 'Delete' button on a specific user.
            - I will see the user removed from the page.
    6. As the admin, I want to be able to approve new registrations so no one can get access without permission/controle:
        - By navigating to the Users page I can use the 'Approve' button on a specific user in the Users asking for approval section.
            - I will see the user moved to the Active Users section.

    7. As the admin, I don't want other profiles to be able to use pages from where important changes to the database can be made:
        - As a user or visitor I can try to open the 

### Login-Register Validation
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
For the Unittests I focussed mostly on authorisation, page loads and the error pages. Besides this I also tested the login and logout functionality. Because of time I chose to do test the button, actions, queries and database modifiers in the user storie testing. This also applies for the JavaScript I used, the errors and success messages I tested on the website.

### Further testing
* Tested this website on laptop and mobile.
* Tested this website on Google Chrome, Firefox and Safari browsers.
* I've asked colleagues and friends to give feedback.
* I've asked for peer reviews on Slack.
* During testing I used "inspect" function on different OS, devices and browsers.


### Issues found (all solved)
* When implementing the sidebar nav form materialize I came accross the issue that the sidebar was greyed out. I found the solution [here](https://github.com/Dogfalo/materialize/issues/3844)
* Visitors and users can see urls from which they should have no access rights. I wouldn't want to solve this with several if-else statements in every route/view. So I asked arround and with a little help I created my own decorator for this. 