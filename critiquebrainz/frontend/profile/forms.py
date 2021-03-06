from flask_wtf import Form
from flask_babel import gettext
from wtforms import StringField, BooleanField, validators
from wtforms.fields.html5 import EmailField


class ProfileEditForm(Form):
    display_name = StringField(gettext("Display name"), [
        validators.DataRequired(message=gettext("Display name field is empty.")),
        validators.Length(min=3, message=gettext("Display name needs to be at least 3 characters long.")),
        validators.Length(max=64, message=gettext("Display name needs to be at most 64 characters long."))])
    email = EmailField(gettext("Email"), [
        validators.Optional(strip_whitespace=False),
        validators.Email(message=gettext("Email field is not a valid email address."))])
    show_gravatar = BooleanField(gettext("Show my Gravatar"))
