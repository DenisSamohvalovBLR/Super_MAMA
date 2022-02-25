from flask import render_template, request, session, redirect, url_for, flash
from werkzeug.security import generate_password_hash

from app import app, db
from models.db_models import User, Profile

menu = [{"name": "Authorization", "url": "authorization"}]

        # {"name": "Authorization", "url": "authorization"},


blocks = [{"name": "Food", "url": "food"},
          {"name": "Sleep", "url": "sleep"},
          {"name": "Parse", "url": "parse"}]


# @app.route('/logout')

# def logout():
#     logout_user()
#     flash("Вы вышли из аккаунта", "success")
#     return redirect(url_for('login'))
#
#
# @app.route("/profile")

# def profile(username):
#     # if 'userLogged' not in session or session['userLogged'] != username:
#     #     abort(401)
#     #     return f"Профиль пользователя: {username}"
#     return f"""<p><a href="{url_for('logout')}">Выйти из профиля</a><p>user info: {current_user.get_id()}"""


@app.route("/registration", methods=["POST", "GET"])
def registration():
    if request.method == "POST":
        try:
            hash = generate_password_hash(request.form['password_hash'])
            u = User(email=request.form['email'], password_hash=hash)
            db.session.add(u)
            db.session.flush()

            p = Profile(name=request.form['username'], user_id=u.id)
            db.session.add(p)
            db.session.commit()
        except:
            db.session.rollback()
            print("Ошибка добавления в БД")

    if 'userLogged' in session:
        return redirect(url_for('blocks_menu', username=session['userLogged']))
    elif request.method == 'POST' \
            and request.form['username'] == "dsam" \
            and request.form['email'] == "denis.samohvalov.1987.blr@gmail.com" \
            and request.form['password_hash'] == "1805":
        session['userLogged'] = request.form['username']
        return redirect(url_for('blocks_menu', username=session['userLogged']))

    # if len(request.form['username']) > 2:
    #     flash("Message sent", category='success')
    # else:
    #     flash("Send error", category='error')
    #
    # if request.method == "POST":
    #     print(request.form)

    return render_template("registration.html", title="Registration", blocks=blocks)


# @app.route("/authentication", methods=["POST", "GET"])
# def authentication():
#     return render_template("authentication.html", title="Authentication", menu=menu)
#
#
@app.route("/authorization", methods=["POST", "GET"])
def authorization():
    # if request.method == "POST":
    #     user = dbase.getUserByEmail(request.form["email"])
    #     if user and check_password_hash(user["password_hash"], request.form["password_hash"]):
    #         userLogin = UserLogin().create(user)
    #         return redirect(url_for("registration"))
    #
    #     flash("Неверная пара логин/пароль", "error")

    return render_template("authorization.html", title="Authorization", menu=menu)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu), 404


@app.route("/")
def base():
    return render_template("base.html", title="Super MAMA", menu=menu)


@app.route("/blocks_menu")
def blocks_menu():
    return render_template("blocks_menu.html", title="Super MAMA", blocks=blocks)


@app.route("/food")
def food():
    return render_template("food.html")


@app.route("/sleep")
def sleep():
    return render_template("sleep.html")


@app.route("/parse")
def parse():
    return render_template("parse.html")


if __name__ == '__main__':
    app.run(debug=True)
