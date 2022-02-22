from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '1111'

menu = [{"name": "Registration", "url": "user"},
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
def profile(username, path):
    return f"Пользователь: {username}, {path}"


@app.route("/user", methods=["POST", "GET"])
def user():
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash("Message sent", category='success')
        else:
            flash("Send error", category='error')

    return render_template("user.html", title="Registration", menu=menu)


# with app.test_request_context():
#     print(url_for('base'))


if __name__ == '__main__':
    app.run(debug=True)
