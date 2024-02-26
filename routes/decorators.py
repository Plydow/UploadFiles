from functools import wraps
from flask import redirect, url_for, session, request

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('views.account.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function