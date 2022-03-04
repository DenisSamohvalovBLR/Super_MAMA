# if len(request.form['username']) > 4 and len(request.form['email']) > 4 and len(
#         request.form['password_hash']) > 4:
#     pass_hash = generate_password_hash(request.form['password_hash'])
#     res = db.add_user(request.form['username'], request.form['email'], pass_hash)
#     if res:
#         flash('You have successfully registered', 'success')
#         return redirect(url_for('authorization'))
#     else:
#         flash('Error adding to database', 'error')
# else:
#     flash('Invalid fields', 'error')


#profile = db.relationship('Profile', backref='user', lazy=True)
