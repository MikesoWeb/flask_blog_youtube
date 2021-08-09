import os
import shutil
from flask import Blueprint, render_template, flash, url_for
from werkzeug.utils import redirect

from blog import bcrypt, db
from blog.models import User
from blog.user.forms import RegistrationForm, LoginForm

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        full_path = os.path.join(os.getcwd(), 'blog/static', 'profile_pics', user.username)
        if not os.path.exists(full_path):
            os.mkdir(full_path)
        shutil.copy(f'{os.getcwd()}/blog/static/profile_pics/default.jpg', full_path)
        flash('Ваш аккаунт был создан. Вы можете войти на блог', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form, title='Регистрация', legend='Регистрация')


@users.route('/login', methods=['GET', 'POST'])
def login():
    return 'hello'
