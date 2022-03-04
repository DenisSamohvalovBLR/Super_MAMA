from flask import url_for, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from app import db
from models.db_models import User, Profile


class UserController:
    @classmethod
    def get_user_by_email(cls, email):
        return User.query.filter_by(email=email).first()

    @classmethod
    def get_user(cls, user):
        return User.query.filter_by(user_id=user).first()

    @classmethod
    def add_user(cls):
        if len(request.form['username']) > 4 and len(request.form['email']) > 4 and len(
                request.form['password_hash']) > 4:
            try:
                pass_hash = generate_password_hash(request.form['password_hash'])
                u = User(email=request.form['email'], password_hash=pass_hash)
                db.session.add(u)
                db.session.flush()

                p = Profile(name=request.form['username'], user_id=u.id)
                db.session.add(p)
                db.session.commit()
            except:
                db.session.rollback()
        return redirect(url_for('authorization'))
