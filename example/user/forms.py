from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(FlaskForm):
    first_name = StringField(
        label='First Name',
        validators=[DataRequired(), Length(min=3)],
        render_kw={'placeholder': 'First Name'}
    )
    email = StringField(
        label='Email',
        validators=[DataRequired(), Email()],
        render_kw={'placeholder': 'Email'}
    )
    password = PasswordField(
        label='Password',
        validators=[DataRequired(), Length(min=7)],
        render_kw={'placeholder': 'Password'}
    )

    submit = SubmitField(
        label='sign up'
    )


class LoginForm(FlaskForm):
    email = StringField(
        label='Email',
        validators=[DataRequired(), Email()],
        render_kw={'placeholder': 'Email'}
    )
    password = PasswordField(
        label='Password',
        validators=[DataRequired(), Length(min=7)],
        render_kw={'placeholder': 'Password'}
    )

    submit = SubmitField(
        label='sign in'
    )