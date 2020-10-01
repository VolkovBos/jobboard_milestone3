import os
from flask, render_template import Flask

#in Heroku plaatsen
app = Flask(__name__)
app.secret_key = 'SECRET_KEY'


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

#debug uitzetten aan het eind
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True) 