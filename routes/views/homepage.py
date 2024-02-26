from flask import Blueprint, redirect, url_for

views = Blueprint('homepage', __name__)

@views.route('/')
def home():
    return redirect(url_for('views.account.login'))