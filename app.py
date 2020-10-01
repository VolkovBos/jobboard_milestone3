import os
from flask import ( Flask, render_template )

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'           #in Heroku plaatsen


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)                     #debug uitzetten aan het eind