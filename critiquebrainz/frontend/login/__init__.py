"""
Package login provides authentication functionality for CritiqueBrainz.

It is based on OAuth2 protocol. MusicBrainz is the only supported provider.
"""
from flask import redirect, url_for
from flask_login import LoginManager, current_user
from flask_babel import gettext
from critiquebrainz.data.model.user import User
from functools import wraps

mb_auth = None

login_manager = LoginManager()
login_manager.login_view = 'login.index'
login_manager.login_message = gettext(u"Please sign in to access this page.")
login_manager.localize_callback = gettext


@login_manager.user_loader
def load_user(user_id):
    return User.get(id=user_id)


def login_forbidden(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if current_user.is_anonymous() is False:
            return redirect(url_for('frontend.index'))
        return f(*args, **kwargs)

    return decorated
