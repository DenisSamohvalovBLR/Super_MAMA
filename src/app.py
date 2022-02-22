from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = '1111'

menu = [{"name": "Authorization", "url": "login"},
        {"name": "Food", "url": "food"},
        {"name": "Sleep", "url": "sleep"},
        {"name": "Parse", "url": "parse"}]


@app.route("/")
def base():
    print(url_for('base'))
    return render_template("base.html", title="Super MAMA", menu=menu)


@app.route("/food")
def food():
    return render_template("food.html")


@app.route("/sleep")
def sleep():
    return render_template("sleep.html")


@app.route("/parse")
def parse():
    return render_template("parse.html")


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)

    return f"Профиль пользователя: {username}"


@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "dsam" and request.form['psw'] == '111':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    if len(request.form['username']) > 2:
        flash("Message sent", category='success')
    else:
        flash("Send error", category='error')

    return render_template("login.html", title="Authorization", menu=menu)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu), 404


if __name__ == '__main__':
    app.run(debug=True)
