import uuid
from io import BytesIO

from flask import Blueprint, request, render_template, url_for, redirect, session, jsonify, make_response

from werkzeug.utils import secure_filename
import time
import os
import base64

from App.models.uploadpictures import Indexpic
from App.models import db

blue = Blueprint('first', __name__)
basedir = os.path.abspath(os.path.dirname(__file__))

@blue.route('/')
def hello_world():
    return 'Hello World!'

@blue.route('/index/')
def index():
    piclist = Indexpic.query.all()
    return render_template("index.html",piclist=piclist)

@blue.route('/base/')
def base():
    return render_template("basea.html")

@blue.route('/pricing/')
def pricing():
    return render_template("pricing.html")

@blue.route('/products/')
def products():
    return render_template("products.html")

@blue.route('/contact/')
def contact():
    return render_template("contact.html")

@blue.route('/technology/')
def technology():
    return render_template("technology.html")

@blue.route('/login/')
def login():
    return render_template("login.html")

@blue.route('/regist/',methods=['POST','GET'])
def regist():
    if request.method == 'GET':
        return render_template("regist.html")
    else:
        return 'jojo的奇幻冒险'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@blue.route('/up_photo/', methods=['POST'])
def up_photo():
    file_dir = os.path.join(basedir, 'static/img123/')
    name = request.form.get('name')
    print(name)
    f = request.files['photo']
    if f and allowed_file(f.filename):
        fname = secure_filename(f.filename)
        print(fname)
        ext = fname.rsplit('.', 1)[1]
        uuid_text = str(uuid.uuid4())
        new_filename = uuid_text + '.' + ext
        print(new_filename)
        new_filepath = os.path.join(file_dir, new_filename)
        f.save(new_filepath)
        src = os.path.join( '/static/img123/',new_filename)
        pic = Indexpic(name=name,src=src)
        data = pic.save()
        return jsonify(data)

@blue.route('/to_up_photo/', methods=['GET'])
def to_up_photo():
    return render_template("uploadpic.html")

@blue.route('/downloadpic/', methods=['GET'])
def downloadpic():
    piclist = Indexpic.query.all()

    return render_template("downloadpic.html",piclist=piclist)


