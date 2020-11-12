# General imports for this project
import os
import re
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
from functools import wraps
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


def login_required(f):
    """
    View decorator which indicates that for that view/page a user is
    required to be logged in. Otherwise a 404 page is being showed.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return abort(404)

        return f(*args, **kwargs)

    return decorated_function


def admin_required(f):
    """
    View decorator which indicates that for that view/page a admin is
    required to be logged in. Otherwise a 404 page is being showed.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is not None:
            if g.user['profile'] == 'admin':
                return f(*args, **kwargs)

            return abort(404)

        return abort(404)

    return decorated_function


class User:
    """
    Login configuration
    (https://www.youtube.com/watch?v=2Zz97NVbH0U)
    """
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'


@app.before_request
def before_request():
    """
    Set g.user at login to show the correct navbar and buttons
    Used tutorial: https://www.youtube.com/watch?v=2Zz97NVbH0U
    """
    g.user = None

    if 'user_id' in session:
        g.user = mongo.db.candidates.find_one({'user_id': session['user_id']})


@app.route('/')
@app.route('/index')
def index():
    """
    Index to welcome the user, static content
    """
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Registration view on a modal for vistors of the site to register
    Checks if :
    - username is minimal 8 characters long
    - if both passwords matches
    - if username allready exist
    - if registration was saved
    if incorrect; show messages above main hero image on index.html

    Also hashes the password to the database
    """
    # Check if user is not logged in already
    if g.user:
        return redirect(url_for('index'))

    # If the button is called for an action
    if request.method == 'POST':
        username1 = request.form['username1']
        email = request.form['emailAdress']
        user_password1 = request.form['user_password1']
        user_password2 = request.form['user_password2']

        # Check if the username is at least 8 characters
        if len(username1) < 8:
            flash("Username should be at least 8 characters", 'category2')

        else:
            # Check if the password and password actually match
            if user_password1 == user_password2:
                user = mongo.db.candidates.find_one({'user_name': username1})

                # Check if the user exist in the database
                if user:
                    flash(f"{username1} already exists! \
                        Please choose a different username.", 'category2')

                # If the user does not exist register new user
                else:
                    # Hash password
                    hash_pass = generate_password_hash(user_password1)

                    # Get the highest user_id from the database and add 1
                    max_user_id = mongo.db.candidates.find().sort(
                         [("user_id", -1)]).limit(1)[0]['user_id'] + 1

                    # Create new user with hashed password
                    mongo.db.candidates.insert_one(
                        {
                            'user_name': username1,
                            'email': email,
                            'password': hash_pass,
                            'approved': False,
                            'status': 'active',
                            'user_id': max_user_id,
                            'profile': 'user',
                            'first_name': request.form['firstName'],
                            'last_name': request.form['lastName']
                        }
                    )
                    # Check if user is actually saved
                    user_in_db = mongo.db.candidates.find_one(
                        {"user_name": username1})

                    # if saved message that the registration is being processed
                    if user_in_db:
                        flash("Your registration is saved, \
                            we will get in touch with you.", 'category4')

                    # if not saved refer to the contact page
                    else:
                        flash("There was a problem saving your registration. \
                            If this happens again, please use the contactform \
                                to contact the administrator of the website.",
                              'category2')

            # If the passwords don't match
            else:
                flash("Passwords are not identical. Please try again.",
                      'category2')

    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login view on a modal for candidates/user and admin to login
    I used a tutorial: https://www.youtube.com/watch?v=2Zz97NVbH0U
    for the login/session sections.
    Checks if :
    - username is minimal 8 characters long
    - if username exists
    - if password is correct
    - if user/candidate is active
    - if user is approved
    if incorrect; show messages above main hero image on index.html

    Used tutorial: https://www.youtube.com/watch?v=2Zz97NVbH0U

    Also unhashes the password from the database
    """
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

                # Check if the user is approved
                if users['approved'] is True:

                    # Check if the password is correct
                    if check_password_hash(users['password'], password):
                        session['user_id'] = users['user_id']

                    # Incorrect password
                    else:
                        flash('Your password is incorrect', 'category1')

                # User is not approved yet
                else:
                    flash('Your registration is not processed yet.',
                          'category1')

            # Inactive user
            else:
                flash('This user is inactive, \
                    please contact the administrator', 'category1')

        # Unknown user
        else:
            flash('The username provided is not known', 'category1')

    return redirect(url_for('index'))


@app.route('/logout')
@login_required
def logout():
    """
    Navbar link to clear session -> to logout the user/admin
    """
    if not g.user:
        return redirect(url_for('index'))

    # Clear session
    session.pop('user_id', None)
    return redirect(url_for('index'))


@app.route('/profile/<userid>')
@login_required
def profile(userid):
    """
    Opens profile page of a user
    """
    return render_template(
        "profile.html",
        user=mongo.db.candidates.find_one(
            {"_id": ObjectId(userid)}))


@app.route('/update_password/<user_id>', methods=['POST'])
@login_required
def update_password(user_id):
    """
    This will update the password from a modal available at the profile
    page for the user. Some checks are being set. A user should always
    fill in his current password and twice the new one, so no typos
    can be made.
    """
    the_user = mongo.db.candidates.find_one({"_id": ObjectId(user_id)})

    if request.method == 'POST':
        users = mongo.db.candidates
        form = request.form.to_dict()
        hash_pass = generate_password_hash(form['password_new'])

        # Check if the new passwords actually match
        if form['password_new'] == form['password_new_confirm']:

            # Check if the old password is correct
            if check_password_hash(the_user['password'], form['password_old']):
                users.update(
                    {'_id': ObjectId(user_id)},
                    {'$set': {'password': hash_pass}})
                flash("Your password is changed", 'category4')

            # Old password is incorrect
            else:
                flash("Your current password is incorrect", 'category3')

        # Confirm and new password are not the same
        else:
            flash("The new passwords do not match", 'category3')

    return render_template(
        'profile.html',
        user=the_user)


@app.route('/users')
@admin_required
def users():
    """
    Overview of all the users divided in 3 groups:
    - Users which are registrated and need to be approved by an admin
    - Users which can login
    - Users which are inactive
    """
    users_active = mongo.db.candidates.find(
        {'approved': True, 'status': 'active'})
    users_to_approve = mongo.db.candidates.find(
        {'approved': False, 'status': 'active'})
    users_inactive = mongo.db.candidates.find(
        {'status': 'inactive'})
    nr_users_active = users_active.count()
    nr_users_to_approve = users_to_approve.count()
    nr_users_inactive = users_inactive.count()

    return render_template(
        "users.html",
        users=users_active,
        users_to_approve=users_to_approve,
        users_inactive=users_inactive,
        nr_users_active=nr_users_active,
        nr_users_to_approve=nr_users_to_approve,
        nr_users_inactive=nr_users_inactive
    )


@app.route('/add_user')
@admin_required
def add_user():
    """
    Add a user by using a form,
    profiles and statusses can be selected by dropdown
    user_id is counted upwards
    """
    user_status = mongo.db.statuses.find({'type': 'user'})
    user_profiles = mongo.db.profiles.find()
    max_user_id = mongo.db.candidates.find().sort(
        [("user_id", -1)]).limit(1)[0]['user_id'] + 1
    profile_pic = 'https://github.com/VolkovBos/milestone3_jobboard/\
blob/master/static/img/profile.png?raw=true'

    return render_template(
        'adduser.html',
        status=user_status,
        profiles=user_profiles,
        max_user_id=max_user_id,
        profile_pic=profile_pic
    )


@app.route('/insert_user', methods=['POST'])
@admin_required
def insert_user():
    """
    Insert user to the database
    """
    users = mongo.db.candidates
    hash_pass = generate_password_hash(request.form.get('password'))
    user_id = int(request.form.get('user_id'),)

    users.insert_one(
        {
            'image_url': request.form.get('image_url'),
            'user_name': request.form.get('user_name'),
            'profile': request.form.get('profile'),
            'password': hash_pass,
            'status': request.form.get('status'),
            'user_id': user_id,
            'first_name': request.form.get('given-name'),
            'last_name': request.form.get('family-name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'street': request.form.get('street'),
            'house_nr': request.form.get('address-line2'),
            'zip_code': request.form.get('zip_code'),
            'city': request.form.get('city'),
            'approved': True
        })

    return redirect(url_for('users'))


@app.route('/edit_user/<userid>')
@login_required
def edit_user(userid):
    """
    Edit a user by using a form
    profiles and statuses can be selected by dropdown
    """
    user_status = mongo.db.statuses.find({'type': 'user'})
    user_profiles = mongo.db.profiles.find()
    the_user = mongo.db.candidates.find_one({"_id": ObjectId(userid)})

    return render_template(
        'edituser.html',
        user=the_user,
        status=user_status,
        profiles=user_profiles)


@app.route('/update_user/<userid>', methods=['POST'])
@login_required
def update_user(userid):
    """
    Updates user to the database
    """
    users = mongo.db.candidates
    user_id = int(request.form.get('user_id'),)

    users.update(
        {'_id': ObjectId(userid)},
        {'$set': {
            'image_url': request.form.get('image_url'),
            'user_name': request.form.get('user_name'),
            'profile': request.form.get('profile'),
            'status': request.form.get('status'),
            'user_id': user_id,
            'first_name': request.form.get('given-name'),
            'last_name': request.form.get('family-name'),
            'email': request.form.get('email_address'),
            'phone': request.form.get('phone'),
            'street': request.form.get('street'),
            'house_nr': request.form.get('address-line2'),
            'zip_code': request.form.get('zip_code'),
            'city': request.form.get('city'),
            'url_github': request.form.get('url_github'),
            'url_twitter': request.form.get('url_twitter'),
            'url_instagram': request.form.get('url_instagram'),
            'url_linkedin': request.form.get('url_linkedin'),
            'url_facebook': request.form.get('url_facebook'),
            'skill1': request.form.get('skill1'),
            'skillp1': request.form.get('skillp1'),
            'skill2': request.form.get('skill2'),
            'skillp2': request.form.get('skillp2'),
            'skill3': request.form.get('skill3'),
            'skillp3': request.form.get('skillp3'),
            'skill4': request.form.get('skill4'),
            'skillp4': request.form.get('skillp4'),
            'skill5': request.form.get('skill5'),
            'skillp5': request.form.get('skillp5')
        }}
    )

    # admin redirects back to users overview
    if g.user['profile'] == 'admin':
        return redirect(url_for('users'))

    # user redirects back to users overview
    if g.user['profile'] == 'user':
        return redirect(url_for('profile', userid=g.user['_id']))


@app.route('/approve_user/<userid>')
@admin_required
def approve_user(userid):
    """
    Updates user to approved in the database
    """
    users = mongo.db.candidates
    users.update(
        {'_id': ObjectId(userid)},
        {'$set': {
            'approved': True
        }})

    return redirect(url_for('users'))


@app.route('/deactivate_user/<userid>')
@admin_required
def deactivate_user(userid):
    """
    Updates user to inactive in the database
    """
    users = mongo.db.candidates
    users.update(
        {'_id': ObjectId(userid)},
        {'$set': {
            'status': 'inactive'
        }})

    return redirect(url_for('users'))


@app.route('/activate_user/<userid>')
@admin_required
def activate_user(userid):
    """
    Updates user to active in the database
    """
    users = mongo.db.candidates
    users.update(
        {'_id': ObjectId(userid)},
        {'$set': {
            'status': 'active'
        }})

    return redirect(url_for('users'))


@app.route('/delete_user/<userid>')
@admin_required
def delete_user(userid):
    """
    Deletes user from the database
    """
    mongo.db.candidates.delete_one({'_id': ObjectId(userid)})

    return redirect(url_for('users'))


@app.route('/setup')
@admin_required
def setup():
    """
    Overview of some fields which can be managed by the admin
    fields are status, images and profiles

    status has mandatory records which cannot be deleted because
    they are used in queries in this app

    images are used fo vacancies and application selection

    profiles are as of yet readonly
    """
    status = mongo.db.statuses.find().sort([("type", 1)])
    profiles = mongo.db.profiles.find().sort([("name", 1)])
    images = mongo.db.photos.find().sort([("name", 1)])
    return render_template(
        "setup.html",
        status=status,
        profiles=profiles,
        images=images
    )


@app.route('/insert_status', methods=['POST'])
@admin_required
def insert_status():
    """
    Insert status to the database
    """
    status = mongo.db.statuses
    status.insert_one(request.form.to_dict())

    return redirect(url_for('setup'))


@app.route('/uplete_status/<status_id>', methods=['POST'])
@admin_required
def uplete_status(status_id):
    """
    Updates or deletes a status to/of the database
    depending on the button used
    returns to the setup route
    """
    status = mongo.db.statuses

    if 'save' in request.form:
        status.update_one(
            {'_id': ObjectId(status_id)},
            {'$set': {
                'status_name': request.form.get('status_name'),
                'type': request.form.get('type')
            }})

    if 'delete' in request.form:
        status.delete_one({'_id': ObjectId(status_id)})

    return redirect(url_for('setup'))


@app.route('/insert_image', methods=['POST'])
@admin_required
def insert_image():
    """
    Insert image to the database
    used for vacancies and application overview pages
    """
    photos = mongo.db.photos
    photos.insert_one(request.form.to_dict())

    return redirect(url_for('setup'))


@app.route('/uplete_image/<image_id>', methods=['POST'])
@admin_required
def uplete_image(image_id):
    """
    Updates or deletes a image to/of the database
    depending on the button used
    returns to the setup route
    """
    photos = mongo.db.photos

    if 'save' in request.form:
        photos.update_one(
            {'_id': ObjectId(status_id)},
            {'$set': {
                'name': request.form.get('name'),
                'photo_url': request.form.get('photo_url')
            }})

    if 'delete' in request.form:
        photos.delete_one({'_id': ObjectId(image_id)})

    return redirect(url_for('setup'))


@app.route('/vacancies')
def vacancies():
    """
    Overview of all the vacancies divided in 2 user groups:
    - Visitors and users see the open vacancies
    - Admins will also see the closed vacancies
      they can CRUD all vacancies
    """
    vacancies_open = mongo.db.vacancies.find(
        {'status': {'$ne': 'closed'}})
    vacancies_closed = mongo.db.vacancies.find(
        {'status': 'closed'})

    return render_template(
        "vacancies.html",
        vacancies_open=vacancies_open,
        nr_vacancies_open=vacancies_open.count(),
        vacancies_closed=vacancies_closed,
        nr_vacancies_closed=vacancies_closed.count()
    )


@app.route('/search_vacancy')
def search_vacancy():
    """
    Option to search in the navbar for vacancies
    Got the solution here on slack:
    https://code-institute-room.slack.com/archives/C7JQY2RHC/p1597516473422900?thread_ts=1597493944.417900&cid=C7JQY2RHC
    """
    query = request.args.get("search")
    vacs = mongo.db.vacancies.find(
        {"$or": [{"job_title": {"$regex": re.compile(
                    query, re.IGNORECASE)}},
                 {"location": {"$regex": re.compile(
                    query, re.IGNORECASE)}},
                 {"text": {"$regex": re.compile(
                    query, re.IGNORECASE)}}]})

    return render_template(
        'vacancies.html',
        vacancies_open=vacs,
        nr_vacancies_open=vacs.count()
    )


@app.route('/add_vacancy')
@admin_required
def add_vacancy():
    """
    Add a vacancy by using a form,
    photos and statusses can be selected by dropdown
    """
    vacancy_status = mongo.db.statuses.find({'type': 'vacancy'})
    photos = mongo.db.photos.find()

    return render_template(
        'addvacancy.html',
        status=vacancy_status,
        photos=photos)


@app.route('/insert_vacancy', methods=['POST'])
@admin_required
def insert_vacancy():
    """
    Insert vacancy to the database
    """
    vacancies = mongo.db.vacancies
    vacancies.insert_one(
        {
            'job_title': request.form.get('job_title'),
            'status': request.form.get('status'),
            'location': request.form.get('location'),
            'hours': request.form.get('hours'),
            'salary': request.form.get('salary'),
            'start_date': request.form.get('start_date'),
            'end_date': request.form.get('end_date'),
            'photo_url': request.form.get('photo_url'),
            'text': request.form.get('text')
        })

    return redirect(url_for('vacancies'))


@app.route('/edit_vacancy/<vacancy_id>')
@admin_required
def edit_vacancy(vacancy_id):
    """
    Edit a vacancy by using a form
    photos and statusses can be selected by dropdown
    """
    the_vacancy = mongo.db.vacancies.find_one({"_id": ObjectId(vacancy_id)})
    photos = mongo.db.photos.find()
    vacancy_status = mongo.db.statuses.find({'type': 'vacancy'})

    return render_template(
        'editvacancy.html',
        vacancy=the_vacancy,
        status=vacancy_status,
        photos=photos)


@app.route('/update_vacancy/<vacancy_id>', methods=['POST'])
@admin_required
def update_vacancy(vacancy_id):
    """
    Updates vacancy to the database
    Checks build in to see which button is being used
    """
    vacancies = mongo.db.vacancies
    vacancies.update_one(
        {'_id': ObjectId(vacancy_id)},
        {'$set': {
            'job_title': request.form.get('job_title'),
            'status': request.form.get('status'),
            'location': request.form.get('location'),
            'hours': request.form.get('hours'),
            'salary': request.form.get('salary'),
            'start_date': request.form.get('start_date'),
            'end_date': request.form.get('end_date'),
            'photo_url': request.form.get('photo_url'),
            'text': request.form.get('text')
        }})

    # If update button is used
    if 'update' in request.form:
        return redirect(url_for('edit_vacancy', vacancy_id=vacancy_id))

    # If save button is used
    if 'save' in request.form:
        return redirect(url_for('vacancies'))


@app.route('/close_vacancy/<vacancy_id>')
@admin_required
def close_vacancy(vacancy_id):
    """
    Updates vacancy to the database
    Closes a vacancy, set status on closed
    """
    vacancies = mongo.db.vacancies
    vacancies.update_one(
        {'_id': ObjectId(vacancy_id)},
        {'$set': {
            'status': 'closed'
        }})

    return redirect(url_for('vacancies'))


@app.route('/delete_vacancy/<vacancy_id>')
@admin_required
def delete_vacancy(vacancy_id):
    """
    Deletes vacancy from the database
    """
    mongo.db.vacancies.delete_one({'_id': ObjectId(vacancy_id)})

    return redirect(url_for('vacancies'))


@app.route('/applications')
@admin_required
def applications():
    """
    Overview of all the applications
    for overview and management of applications
    Admins can CRUD all applications
    """

    applications_open = mongo.db.applications.find(
            {'status': {'$ne': 'closed'}})
    applications_closed = mongo.db.applications.find(
            {'status': 'closed'})

    return render_template(
        "applications.html",
        applications_open=applications_open,
        nr_applications_open=applications_open.count(),
        applications_closed=applications_closed,
        nr_applications_closed=applications_closed.count()
    )


@app.route('/myapplications')
@login_required
def myapplications():
    """
    Overview of all the applications for users
    for overview of applications
    users can only check their own applications
    """
    user_id = str(g.user['_id'])
    applications_open = mongo.db.applications.find(
        {
            'candidate_id': user_id,
            'status': {'$ne': 'closed'}
        }
    )
    applications_closed = mongo.db.applications.find(
        {
            'candidate_id': user_id,
            'status': 'closed'
        }
    )

    return render_template(
        "applications.html",
        applications_open=applications_open,
        nr_applications_open=applications_open.count(),
        applications_closed=applications_closed,
        nr_applications_closed=applications_closed.count()
    )


@app.route('/add_application/<vacancy_id>')
@login_required
def add_application(vacancy_id):
    """
    Add a application by using a form,
    statuses can be selected by dropdown
    Admin can also create a application from application page,
    here a open vacancy can be chosen in a dropdown as well
    as active candidates
    """
    photos = mongo.db.photos.find()
    active_candidates = mongo.db.candidates.find(
        {'status': 'active'})
    inactive_candidates = mongo.db.candidates.find(
        {'status': {'$ne': 'active'}})
    open_vacancies = mongo.db.vacancies.find(
        {'status': {'$ne': 'closed'}})
    closed_vacancies = mongo.db.vacancies.find(
        {'status': 'closed'})
    application_status = mongo.db.statuses.find({'type': 'application'})

    """
    The admin string is set if a application is created from the
    application page. Then there is no vacancy data available
    """
    # Check if the vacancy_id is a normal id
    if vacancy_id != 'admin':
        the_vacancy = mongo.db.vacancies.find_one(
            {"_id": ObjectId(vacancy_id)})

    # Set an empty string as the id, null will give an error
    elif g.user['profile'] == 'admin':
        the_vacancy = ''

    return render_template(
        'addapplication.html',
        vacancy=the_vacancy,
        active_candidates=active_candidates,
        inactive_candidates=inactive_candidates,
        open_vacancies=open_vacancies,
        closed_vacancies=closed_vacancies,
        status=application_status,
        photos=photos
    )


@app.route('/insert_application', methods=['POST'])
@login_required
def insert_application():
    """
    Insert application to the database
    Queries the linked vacancy and adds some of the data
    from vacancy to see in the myapplication overview
    """
    vacancy_id = request.form.get('vacancy_id')
    the_vacancy = mongo.db.vacancies.find_one(
            {"_id": ObjectId(vacancy_id)})

    candidate_id = request.form.get('candidate_id')
    the_candidate = mongo.db.candidates.find_one(
            {"_id": ObjectId(candidate_id)})

    applications = mongo.db.applications

    """
    When admin/user creates application its being updated with vacancy info
    An admin can overulle this, by filling the fields
    """
    vacancy_hours = (request.form.get('vacancy_hours')
                     if request.form.get('vacancy_hours') != ''
                     else the_vacancy.get('vacancy_hours'))
    vacancy_salary = (request.form.get('vacancy_salary')
                      if request.form.get('vacancy_salary') != ''
                      else the_vacancy.get('vacancy_salary'))
    vacancy_photo_url = (request.form.get('vacancy_photo_url')
                         if request.form.get('vacancy_photo_url') != ''
                         else the_vacancy.get('vacancy_photo_url'))
    vacancy_location = (request.form.get('vacancy_location')
                        if request.form.get('vacancy_location') != ''
                        else the_vacancy.get('vacancy_location'))
    vacancy_text = (request.form.get('vacancy_text')
                    if request.form.get('vacancy_text') != ''
                    else the_vacancy.get('vacancy_text'))

    applications.insert_one(
        {
            'status': request.form.get('status'),
            'availability_date': request.form.get('availability_date'),
            'comments': request.form.get('comments'),
            'candidate_id': candidate_id,
            'candidate_name': the_candidate.get('first_name') +
            ' ' + the_candidate.get('last_name'),
            'vacancy_id': vacancy_id,
            'vacancy_job_title': the_vacancy.get('job_title'),
            'vacancy_hours': vacancy_hours,
            'vacancy_salary': vacancy_salary,
            'vacancy_photo_url': vacancy_photo_url,
            'vacancy_location': vacancy_location,
            'vacancy_text': vacancy_text,
            'why_match': request.form.get('why_match'),
            'url_resume': request.form.get('url_resume')
        })

    # User is redirected to My Applications
    if g.user['profile'] != 'admin':
        return redirect(url_for('myapplications'))

    # Admin is redirected to all applications
    if g.user['profile'] == 'admin':
        return redirect(url_for('applications'))


@app.route('/edit_application/<application_id>')
@admin_required
def edit_application(application_id):
    """
    Route to go to the edit application page
    Vacancies and candidates are shown in dropdown selector
    closed/inactive record are shown in lower section of dropdown
    """
    photos = mongo.db.photos.find()
    the_application = mongo.db.applications.find_one(
        {"_id": ObjectId(application_id)})
    active_candidates = mongo.db.candidates.find(
        {'status': 'active'})
    inactive_candidates = mongo.db.candidates.find(
        {'status': {'$ne': 'active'}})
    open_vacancies = mongo.db.vacancies.find(
        {'status': {'$ne': 'closed'}})
    closed_vacancies = mongo.db.vacancies.find(
        {'status': 'closed'})
    application_status = mongo.db.statuses.find(
        {'type': 'application'})

    return render_template(
        'editapplication.html',
        application=the_application,
        active_candidates=active_candidates,
        inactive_candidates=inactive_candidates,
        open_vacancies=open_vacancies,
        closed_vacancies=closed_vacancies,
        status=application_status,
        photos=photos
    )


@app.route('/update_application/<application_id>', methods=['POST'])
@admin_required
def update_application(application_id):
    """
    Updates application to the database
    Queries the linked vacancy and adds some of the data
    from vacancy to see in the myapplication overview
    """
    vacancy_id = request.form.get('vacancy_id')
    the_vacancy = mongo.db.vacancies.find_one(
            {"_id": ObjectId(vacancy_id)})
    candidate_id = request.form.get('candidate_id')
    the_candidate = mongo.db.candidates.find_one(
            {"_id": ObjectId(candidate_id)})
    applications = mongo.db.applications
    # user_id = str(g.user['_id'])
    applications.update_one(
        {'_id': ObjectId(application_id)},
        {'$set': {
            'status': request.form.get('status'),
            'availability_date': request.form.get('availability_date'),
            'comments': request.form.get('comments'),
            'candidate_id': candidate_id,
            'candidate_name': the_candidate.get('first_name') +
            ' ' + the_candidate.get('last_name'),
            'why_match': request.form.get('why_match'),
            'url_resume': request.form.get('url_resume')
        }})

    the_application = mongo.db.applications.find_one(
        {"_id": ObjectId(application_id)})

    """
    Updates application with all vacancy data
    if vacancy is changed
    """
    if the_application['vacancy_id'] != vacancy_id:
        applications.update_one(
            {'_id': ObjectId(application_id)},
            {'$set': {
                'vacancy_id': vacancy_id,
                'vacancy_job_title': the_vacancy.get('job_title'),
                'vacancy_hours': the_vacancy.get('hours'),
                'vacancy_salary': the_vacancy.get('salary'),
                'vacancy_photo_url': the_vacancy.get('photo_url'),
                'vacancy_location': the_vacancy.get('location'),
                'vacancy_text': the_vacancy.get('text')
            }})
    else:
        applications.update_one(
            {'_id': ObjectId(application_id)},
            {'$set': {
                'vacancy_hours': request.form.get('vacancy_hours'),
                'vacancy_salary': request.form.get('vacancy_salary'),
                'vacancy_photo_url': request.form.get('vacancy_photo_url'),
                'vacancy_location': request.form.get('vacancy_location'),
                'vacancy_text': request.form.get('vacancy_text')
            }})

    return redirect(url_for('applications'))


@app.route('/close_application/<application_id>')
@admin_required
def close_application(application_id):
    """
    Updates application to the database
    Closes a application, set status on closed
    """
    applications = mongo.db.applications
    applications.update_one(
        {'_id': ObjectId(application_id)},
        {'$set': {
            'status': 'closed'
        }})

    return redirect(url_for('applications'))


@app.route('/delete_application/<application_id>')
@admin_required
def delete_application(application_id):
    """
    Deletes vacancy from the database
    """
    mongo.db.applications.delete_one({'_id': ObjectId(application_id)})

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
if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=False)
