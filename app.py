# General imports for this project
import os
from flask import (
    flash,
    Flask,
    g,
    redirect,
    render_template,
    request,
    session, 
    url_for 
)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


# Import my env.py that's ignored by git
if os.path.exists("env.py"):
    import env


# App instance
app = Flask(__name__)
SECRET_KEY = os.environ.get("SECRET_KEY")
app.secret_key = SECRET_KEY


# MongoDB configuration
MONGO_URI = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = 'jobboard_milestone3'
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)


# Login config (https://www.youtube.com/watch?v=2Zz97NVbH0U)
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'


# Set g.user at login to show the correct navbar and buttons 
@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        g.user = mongo.db.candidates.find_one({'user_id': session['user_id']})


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Check if user is not logged in already
    if g.user:
        return redirect(url_for('index'))

    # If the button is called for an action
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        user_password1 = request.form['user_password1']
        user_password2 = request.form['user_password2']

        # Check if the password and password actually match
        if user_password1 == user_password2:
            user = mongo.db.candidates.find_one({'user_name': username})

            # Check if the user exist in the database
            if user:
                flash(f"{username} already exists! Please choose a different username.")
                return redirect(url_for('register'))

            # If the user does not exist register new user
            else:
                # Hash password
                hash_pass = generate_password_hash(user_password1)

                # Create new user with hashed password
                mongo.db.candidates.insert_one(
                    {
                        'user_name': username,
                        'email': email,
                        'password': hash_pass,
                        'approved':False
                    }
                )
                # Check if user is actually saved
                user_in_db = mongo.db.candidates.find_one({"user_name": username})

                # if saved message that the registration is being processed
                if user_in_db:
                    flash("Your registration is saved, we will get in touch with you.")
                    return redirect(url_for('register'))

                # if not saved refer to the contact page
                else:
                    flash("There was a problem saving your registration. If this happens again, please use the contactform to contact the administrator of the website.")
                    return redirect(url_for('contact'))
        
        # If the passwords don't match
        else:
            flash("Passwords are not identical. Please try again.")
            return redirect(url_for('register'))

    return render_template("register.html")


# Login page for candidates and admin to login
# I used a tutorial: https://www.youtube.com/watch?v=2Zz97NVbH0U for the login/session sections.
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check if user is not logged in already
    if g.user:
        return redirect(url_for('index'))
        
    # If the button is called for an action
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        users    = mongo.db.candidates.find_one({'user_name': username})

        # Check if the username exists in the database
        if bool(users):
            # Check if the password is correct
            if check_password_hash(users["password"], password ):
                session['user_id'] = users["user_id"] 
                return redirect(url_for('index'))

            else:
                flash('Your password is incorrect')
                return redirect(url_for('login'))

        else:
            flash('The username provided is not known')
            return redirect(url_for('login'))

    return render_template('login.html')


# User page for management of users
@app.route('/users')
def users():
    return render_template("users.html")


# Navbar link to clear session -> to logout
@app.route('/logout')
def logout():
    if not g.user:
        return redirect(url_for('index'))

    # Clear session
    session.pop('user_id', None)
    return redirect(url_for('index'))


# Contact page in case of any problems
@app.route("/contact")
def contact():
    return render_template("contact.html")


# Vacancies page for overview and management of vacancies
@app.route('/vacancies')
def vacancies():
    vacancies_open = mongo.db.vacancies.find({'vacancy_status': 'open'})

    return render_template("vacancies.html", 
        vacancies_open=vacancies_open )


# Applications page for overview and management of Applications
@app.route('/applications')
def applications():
    return render_template("applications.html", 
        applications_open=mongo.db.applications.find({'status': 'open' }),
        applications_closed=mongo.db.applications.find({'status': {'$ne': 'open'} }))


# To run the app
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)                     #debug uitzetten aan het eind