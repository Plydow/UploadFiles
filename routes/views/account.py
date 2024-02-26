from flask import Blueprint, render_template, current_app, session, request, flash, redirect, url_for
from ..decorators import login_required
from ..forms import LoginForm

views = Blueprint('account', __name__)

@views.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if current_app.config['PASSWORD'] == form.password.data:
            session['logged_in'] = True
            next_page = request.args.get('next')
            return redirect(next_page or url_for('views.business.upload'))
        else:
            flash('Incorrect password', 'danger')
    return render_template('login.html', form=form)

@views.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('views.homepage.home'))