from flask import Flask, url_for, request, render_template
from markupsafe import escape 
from werkzeug.utils import secure_filename


app = Flask(__name__)



@app.route("/<name>")
def hello(name):
    age = request.args.get('age', 'Not mentioned')
    return render_template('hello.html', name=name, age=age)


@app.post('/upload')
def upload_file():
    f = request.files['my_file']
    print(f.filename)
    print(f'secure {secure_filename(f.filename)}')
    print(f)
    f.save(f'./uploads/{secure_filename(f.filename)}')
    return f.filename
