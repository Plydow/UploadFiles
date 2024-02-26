from flask import Blueprint
from .account import views as account_views
from .business import views as business_views
from .homepage import views as homepage_views

views = Blueprint('views', __name__)

views.register_blueprint(account_views)
views.register_blueprint(business_views)
views.register_blueprint(homepage_views)