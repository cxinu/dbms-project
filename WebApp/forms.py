from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError
from WebApp.models import User


class RegistrationForm(FlaskForm):
    firstName = StringField(
        "Name",
        render_kw={"placeholder": "First Name"},
        validators=[DataRequired(), Length(min=1, max=16)],
    )
    username = StringField(
        "Username",
        render_kw={"placeholder": "username"},
        validators=[DataRequired(), Length(min=5, max=16)],
    )
    phone = StringField(
        "Phone Number",
        render_kw={"placeholder": "0123456789"},
        validators=[DataRequired(), Length(min=10, max=10)],
    )
    submit = SubmitField("Sign up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("This username Already occupied.")

    def validate_phone(self, phone):
        user = User.query.filter_by(phone=phone.data).first()
        if user:
            raise ValidationError("This Phone Number is Already Registered.")
        elif not (phone.data).isdigit():
            raise ValidationError("invaild Phone Number")


class LoginForm(FlaskForm):
    phone = StringField(
        "Phone Number",
        render_kw={"placeholder": "0123456789"},
        validators=[DataRequired(), Length(min=10, max=10)],
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")

    def validate_phone(self, phone):
        if not (phone.data).isdigit():
            raise ValidationError("invaild Phone Number")


class authForm(FlaskForm):
    code = StringField(
        "verification code",
        render_kw={"placeholder": "Enter code"},
        validators=[DataRequired(), Length(min=5, max=5)],
    )
    submit = SubmitField("Next")
