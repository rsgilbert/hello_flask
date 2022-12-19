from flask import Flask, url_for, request
from markupsafe import escape 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, there darling how are you?</h1>"


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}"

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    return f'Post {escape(post_id)}'

@app.route('/projects/')
def projects():
    return 'projects page'

@app.route('/about')
def about():
    return 'About page'
    
@app.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        return 'Get not allowed for logins!'

@app.post('/login')
def login_post():
    return 'I am logging you in...'


@app.get('/sample-pic')
def sample_pic():
    return url_for('static', filename="region-dim.PNG")


with app.test_request_context():
    print(url_for('about'))
    print(url_for('hello_world'))
    print(url_for('show_post', post_id=5))


