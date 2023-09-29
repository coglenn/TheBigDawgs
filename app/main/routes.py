import os
from flask import Flask, render_template, request, flash, redirect, url_for, app, session
from app import db
import config
from app.main import bp
from app.main.models import *
import urllib.request
from werkzeug.utils import secure_filename


@bp.route('/')
def home():
    return render_template("index.html")

# New functions
@bp.route("/news/")
def news():
    news = NewsModel.query.order_by(NewsModel.week_number)
    week = NewsModel.query.with_entities(NewsModel.week_number).distinct()
    # top = league.top_scored_week()
    context = {
        'news': news,
        "week": week,
    }
    return render_template("news.html", **context )

@bp.route("/power/")
def power():
    # power = PowerModel.query.order_by(PowerModel.power_rank).group_by(PowerModel.week_number)
    power = PowerModel.query.order_by(PowerModel.power_rank)
    week = PowerModel.query.with_entities(PowerModel.week_number).distinct()
    context = {
        'power': power,
        "week": week,
    }
    return render_template("power.html", **context)

@bp.route("/forum/", methods=["GET", "POST"])
def forum():
    messages = PostModel.query.all()
    return render_template("forum.html", messages = messages)

@bp.route("/versus/")
def versus():
    match = MatchupModel.query.order_by(MatchupModel.game_of_week.desc()).all()
    week = MatchupModel.query.with_entities(MatchupModel.week_number).distinct()
    context = {
        'match': match,
        "week": week,
    }
    return render_template("versus.html", **context)

@bp.route('/create/', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not request.form['title'] or not request.form['content']:
            flash("Title and Message are required!")
        else:
            message = PostModel(title = title, 
                           content=content)
            db.session.add(message)
            db.session.commit()
            flash("Record successfully added")
            return redirect(url_for('main.forum'))
    return render_template('create.html')

@bp.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    post = PostModel.query.get_or_404(id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post.title = title
        post.content = content
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.forum'))
    return render_template('edit.html', post=post)

@bp.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    post = PostModel.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('The Post was successfully deleted!')
    # flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('main.forum'))

UPLOAD_FOLDER = 'static/uploads/'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

class MyView(BaseView):
    def __init__(self, *args, **kwargs):
        self._default_view = True
        super(MyView, self).__init__(*args, **kwargs)
        self.admin = Admin()

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@bp.route('/admin')
def upload_form():
	return render_template('admin/index.html')

@bp.route('/admin', methods=['POST'])
def upload_image():
    # print('test')
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # print(file)
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    else:
    # if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.abspath(f'app/static/uploads/{filename}'))
        # print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return MyView().render('admin/index.html', filename=filename)
    # else:
    #     flash('Allowed image types are -> png, jpg, jpeg, gif')
    #     return redirect(request.url)

@bp.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)
