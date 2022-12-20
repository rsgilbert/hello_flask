from flask import Flask, flash, session, redirect, abort, url_for, request, make_response, render_template
from markupsafe import escape 
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = b'Annia'


@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.post("/login")
def login():
    session["username"] = request.form["username"]
    return redirect(url_for("index"))


@app.get("/login")
def login_get():
    return render_template("login.html")


@app.get('/hello')
def hello():
    return 'Hello!'

@app.route("/sample-abort")
def sample_abortion():
    abort(401)

@app.route("/sample-redirect")
def sample_redirection():
    print('I am going to redirect you!')
    return redirect(url_for('hello'))

@app.errorhandler(401)
def unauthorized(error):
    flash('Login first please')
    app.logger.warn('An attempt to access the page when unauthorized')
    resp = make_response(render_template('unauthorized.html'), 401)
    resp.headers['X-App'] = 'Flask'
    return resp


@app.post('/upload')
def upload_file():
    f = request.files['my_file']
    print(f.filename)
    print(f'secure {secure_filename(f.filename)}')
    print(f)
    f.save(f'./uploads/{secure_filename(f.filename)}')
    return f.filename


@app.route('/me')
def me():
    return {
        "username": "Gilbert",
        "title": "Software Engineer"
    }

@app.route("/todos")
def todos():
    return ["Write app", "market", "ship"]
