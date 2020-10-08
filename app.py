# General imports for this project
import os
from flask import (
    abort,
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
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


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


# General index route
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
                flash(f"{username} already exists! \
                    Please choose a different username.")
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
                        'approved': False
                    }
                )
                # Check if user is actually saved
                user_in_db = mongo.db.candidates.find_one(
                    {"user_name": username})

                # if saved message that the registration is being processed
                if user_in_db:
                    flash("Your registration is saved, \
                        we will get in touch with you.")
                    return redirect(url_for('register'))

                # if not saved refer to the contact page
                else:
                    flash("There was a problem saving your registration. \
                        If this happens again, please use the contactform \
                            to contact the administrator of the website.")
                    return redirect(url_for('contact'))

        # If the passwords don't match
        else:
            flash("Passwords are not identical. Please try again.")
            return redirect(url_for('register'))

    return render_template("register.html")


# Login page for candidates and admin to login
# I used a tutorial: https://www.youtube.com/watch?v=2Zz97NVbH0U
# for the login/session sections.
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
        users = mongo.db.candidates.find_one({'user_name': username})

        # Check if the username exists in the database
        if bool(users):

            # Check if the user is active
            if users['status'] == 'active':

                # Check if the password is correct
                if check_password_hash(users['password'], password):
                    session['user_id'] = users['user_id']
                    return redirect(url_for('index'))

                # Incorrect password
                else:
                    flash('Your password is incorrect')
                    return redirect(url_for('login'))

            # Inactive user
            else:
                flash('This user is inactive, \
                    please contact the administrator')
                return redirect(url_for('login'))

        # Unknown user
        else:
            flash('The username provided is not known')
            return redirect(url_for('login'))

    return render_template('login.html')


# Navbar link to clear session -> to logout
@app.route('/logout')
def logout():
    if not g.user:
        return redirect(url_for('index'))

    # Clear session
    session.pop('user_id', None)
    return redirect(url_for('index'))


# Profile page for users
@app.route('/profile/<candidate_id>')
def profile(candidate_id):
    if not g.user:
        abort(404)

    else:
        return render_template(
            "profile.html",
            candidate=mongo.db.candidates.find_one(
                {"_id": ObjectId(candidate_id)}))


# Change password page for users
@app.route('/change_password/<user_id>')
def change_password(user_id):
    if not g.user:
        abort(404)

    else:
        the_user = mongo.db.candidates.find_one({"_id": ObjectId(user_id)})
        return render_template(
            'changepassword.html',
            user=the_user)


# Change the password in MongoDB
@app.route('/update_password/<user_id>', methods=['POST'])
def update_password(user_id):
    the_user = mongo.db.candidates.find_one({"_id": ObjectId(user_id)})

    if request.method == 'POST':
        users = mongo.db.candidates
        form = request.form.to_dict()
        hash_pass = generate_password_hash(form['password_new'])
        print(form)

        # Check if the password and password actually match
        if form['password_new'] == form['password_new_confirm']:

            if check_password_hash(the_user['password'], form['password_old']):
                users.update(
                    {'_id': ObjectId(user_id)},
                    {'$set': {'password': hash_pass}})

            else:
                flash("Your current password is incorrect")
                return render_template(
                    'changepassword.html',
                    user=the_user)

        else:
            flash("The new passwords do not match")
            return render_template(
                'changepassword.html',
                user=the_user)

    return render_template(
        'changepassword.html',
        user=the_user)


# User page for management of users
@app.route('/users')
def users():
    if g.user['profile'] == 'admin':
        return render_template(
            "users.html",
            users=mongo.db.candidates.find({'approved': True}),
            users_to_approve=mongo.db.candidates.find({'approved': False}))
    else:
        abort(403)


# Add user/candidate page
@app.route('/add_user')
def add_user():
    if g.user['profile'] == 'admin':
            user_status = mongo.db.status.find({'type': 'user'})
            user_profiles = mongo.db.profiles.find()
            return render_template(
                'adduser.html',
                status=user_status,
                profiles=user_profiles)
    else:
        abort(403)


# Insert a new user/candidate
@app.route('/insert_user', methods=['POST'])
def insert_user():
    users = mongo.db.candidates
    hash_pass = generate_password_hash(request.form.get('password'))

    users.insert_one(
        {
            'user_name': request.form.get('user_name'),
            'email': request.form.get('email'),
            'profile': request.form.get('profile'),
            'password': hash_pass,
            'status': request.form.get('status'),
            'user_id': request.form.get('user_id'),
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'street': request.form.get('street'),
            'house_nr': request.form.get('house_nr'),
            'zip_code': request.form.get('zip_code'),
            'city': request.form.get('city'),
            'approved': True
        })
    return redirect(url_for('users'))


# Edit user/candidate page
@app.route('/edit_user/<user_id>')
def edit_user(user_id):
    user_status = mongo.db.status.find({'type': 'user'})
    user_profiles = mongo.db.profiles.find()
    the_user = mongo.db.candidates.find_one({"_id": ObjectId(user_id)})
    return render_template(
        'edituser.html',
        user=the_user,
        status=user_status,
        profiles=user_profiles)


# Edit a user/candidate
@app.route('/update_user/<user_id>', methods=['POST'])
def update_user(user_id):
    users = mongo.db.candidates
    users.update(
        {'_id': ObjectId(user_id)},
        {'$set': {
            'user_name': request.form.get('user_name'),
            'email': request.form.get('email'),
            'profile': request.form.get('profile'),
            'status': request.form.get('status'),
            'user_id': request.form.get('user_id'),
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'street': request.form.get('street'),
            'house_nr': request.form.get('house_nr'),
            'zip_code': request.form.get('zip_code'),
            'city': request.form.get('city')
        }}
    )
    return redirect(url_for('users'))


# Approving a new registrated user
@app.route('/approve_user/<user_id>')
def approve_user(user_id):
    users = mongo.db.candidates
    users.update(
        {'_id': ObjectId(user_id)},
        {'$set': {
            'approved': True
        }})
    return redirect(url_for('users'))


# Delete a user
@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    mongo.db.candidates.remove({'_id': ObjectId(user_id)})
    return redirect(url_for('users'))


# Contact page in case of any problems
@app.route("/contact")
def contact():
    return render_template("contact.html")


# Vacancies page for overview and management of vacancies
@app.route('/vacancies')
def vacancies():
    vacancies_open = mongo.db.vacancies.find(
        {'vacancy_status': 'open'})
    vacancies_closed = mongo.db.vacancies.find(
        {'vacancy_status': {'$ne': 'open'}})
    return render_template(
        "vacancies.html",
        vacancies_open=vacancies_open,
        vacancies_closed=vacancies_closed
    )


# Route to go to the add vacancy page
@app.route('/add_vacancy')
def add_vacancy():
    vacancy_status = mongo.db.status.find({'type': 'vacancy'})
    return render_template(
        'addvacancy.html',
        status=vacancy_status)


# Insert a new vacancy
@app.route('/insert_vacancy', methods=['POST'])
def insert_vacancy():
    vacancies = mongo.db.vacancies
    vacancies.insert_one(request.form.to_dict())
    return redirect(url_for('vacancies'))


# Route to go to the edit vacancy page
@app.route('/edit_vacancy/<vacancy_id>')
def edit_vacancy(vacancy_id):
    the_vacancy = mongo.db.vacancies.find_one({"_id": ObjectId(vacancy_id)})
    vacancy_status = mongo.db.status.find({'type': 'vacancy'})
    return render_template(
        'editvacancy.html',
        vacancy=the_vacancy,
        status=vacancy_status)


# Edit a vacancy
@app.route('/update_vacancy/<vacancy_id>', methods=['POST'])
def update_vacancy(vacancy_id):
    vacancies = mongo.db.vacancies
    vacancies.update(
        {'_id': ObjectId(vacancy_id)},
        {
            'vacancy_name': request.form.get('vacancy_name'),
            'vacancy_status': request.form.get('vacancy_status'),
            'start_date': request.form.get('start_date'),
            'end_date': request.form.get('end_date'),
            'vacancy_text': request.form.get('vacancy_text')
        })
    return redirect(url_for('vacancies'))


# Close a vacancy, set status on done
@app.route('/close_vacancy/<vacancy_id>')
def close_vacancy(vacancy_id):
    vacancies = mongo.db.vacancies
    vacancies.update(
        {'_id': ObjectId(vacancy_id)},
        {'$set': {
            'vacancy_status': 'closed'
        }})
    return redirect(url_for('vacancies'))


# Delete a vacancy
@app.route('/delete_vacancy/<vacancy_id>')
def delete_vacancy(vacancy_id):
    mongo.db.vacancies.remove({'_id': ObjectId(vacancy_id)})
    return redirect(url_for('vacancies'))


# Applications page for overview and management of Applications
@app.route('/applications')
def applications():
    return render_template(
        "applications.html",
        applications_open=mongo.db.applications.find(
            {'status': 'open'}),
        applications_closed=mongo.db.applications.find(
            {'status': {'$ne': 'open'}})
    )


# Applications page for overview of applications for a user
@app.route('/myapplications')
def myapplications():
    return render_template(
        "applications.html",
        applications_open=mongo.db.applications.find(
            {'candidate_name': g.user['user_name'], 'status': 'open'}),
        applications_closed=mongo.db.applications.find(
            {
                'candidate_name': g.user['user_name'],
                'status': {'$ne': 'open'}
            }
        )
    )


# Route to go to the add application page
@app.route('/add_application/<vacancy_id>')
def add_application(vacancy_id):
    all_candidates = mongo.db.candidates.find()
    open_vacancies = mongo.db.vacancies.find({'vacancy_status': 'open'})
    application_status = mongo.db.status.find({'type': 'application'})

    if vacancy_id != 'admin':
        the_vacancy = mongo.db.vacancies.find_one(
            {"_id": ObjectId(vacancy_id)})
    else:
        the_vacancy = ''
    return render_template(
        'addapplication.html',
        vacancy=the_vacancy,
        candidates=all_candidates,
        vacancies=open_vacancies,
        status=application_status)


# Insert a new application, from application page or from a vacancy
@app.route('/insert_application', methods=['POST'])
def insert_application():
    applications = mongo.db.applications
    applications.insert_one(request.form.to_dict())

    if g.user['profile'] == 'admin':
        return redirect(url_for('applications'))
    else:
        return redirect(url_for('myapplications'))


# Route to go to the edit application page
@app.route('/edit_application/<application_id>')
def edit_application(application_id):
    the_application = mongo.db.applications.find_one(
        {"_id": ObjectId(application_id)})
    all_candidates = mongo.db.candidates.find()
    open_vacancies = mongo.db.vacancies.find(
        {'vacancy_status': 'open'})
    closed_vacancies = mongo.db.vacancies.find(
        {'vacancy_status': {'$ne': 'open'}})
    application_status = mongo.db.status.find(
        {'type': 'application'})

    return render_template(
        'editapplication.html',
        application=the_application,
        candidates=all_candidates,
        open_vacancies=open_vacancies,
        closed_vacancies=closed_vacancies,
        status=application_status)


# Update an application
@app.route('/update_application/<application_id>', methods=['POST'])
def update_application(application_id):
    applications = mongo.db.applications
    applications.update(
        {'_id': ObjectId(application_id)},
        {
            'vacancy_name': request.form.get('vacancy_name'),
            'status': request.form.get('status'),
            'candidate_name': request.form.get('candidate_name'),
            'start_date': request.form.get('start_date'),
            'comments': request.form.get('comments'),
            'vacancy_text': request.form.get('vacancy_text')
        })
    return redirect(url_for('applications'))


# Close an application
@app.route('/close_application/<application_id>')
def close_application(application_id):
    applications = mongo.db.applications
    applications.update(
        {'_id': ObjectId(application_id)},
        {'$set': {
            'status': 'closed'
        }})
    return redirect(url_for('applications'))


# Delete an application
@app.route('/delete_application/<application_id>')
def delete_application(application_id):
    mongo.db.applications.remove({'_id': ObjectId(application_id)})
    return redirect(url_for('applications'))


# Error 403 handler route
@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403


# Error 404 handler route
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Error 500 handler route
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


# To run the app
# debug uitzetten aan het eind
if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
