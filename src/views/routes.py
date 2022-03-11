from flask import render_template, request, url_for, redirect, flash
from flask_login import logout_user, login_required, current_user, login_user
from werkzeug.security import check_password_hash

from app import app, login_manager
from controller.UserController import UserController
from models.db_models import User, UserLogin

menu = [{"name": "Authorization", "url": "authorization"}]
blocks = [{"name": "Food", "url": "food"},
          {"name": "Sleep", "url": "sleep"},
          {"name": "Parse", "url": "parse"}]


@login_manager.user_loader
def load_user(user_id):
    print('load_user')
    return User.query.filter_by(id=user_id).first()


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out', 'success')
    return redirect(url_for('authorization'))


@app.route('/profile')
@login_required
def profile():
    return f'''<p><a href='{url_for('logout')}'>Sign out</a><p>user info: {current_user.get_id()}'''


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        return UserController.add_user()
    return render_template('registration.html', title='Registration')


@app.route('/authorization', methods=['POST', 'GET'])
def authorization():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    if request.method == 'POST':
        user = UserController.get_user_by_email(request.form['email'])
        if user and check_password_hash(user.password_hash, request.form['password_hash']):
            user_login = UserLogin().create(user)
            rm = True if request.form.get('remain me') else False
            login_user(user_login, remember=rm)
            return redirect(request.args.get("next") or url_for("profile"))

        flash('Invalid username/password', 'error')

    return render_template('authorization.html', title='Authorization', menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Page not found', menu=menu), 404


@app.route("/")
def base():
    return render_template("base.html", title="Super MAMA", menu=menu)


@app.route("/blocks_menu")
@login_required
def blocks_menu():
    return render_template("blocks_menu.html", title="Super MAMA", blocks=blocks)


@app.route("/food")
@login_required
def food():
    return render_template("food.html")


@app.route("/sleep")
@login_required
def sleep():
    return render_template("sleep.html")


@app.route("/parse")
@login_required
def parse():
    return render_template("parse.html")


if __name__ == '__main__':
    app.run(debug=True)
