from string import printable

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from feixin.models import Friends, User

from flask_login import current_user


def is_latin(text):
    return not bool(set(text) - set(printable))


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("注册")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("该username已被占用。请选择另一个。")

        if not (is_latin(username.data)):
            raise ValidationError("只支持英文字母。")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("该email已被占用。请选择另一个。")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("登录")


class AddFriendForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    submit = SubmitField("Add")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not (user):
            raise ValidationError("没有找到username。")

        friendsa = Friends.query.filter_by(
            usernamea=current_user.username, usernameb=username.data
        ).all()
        friendsb = Friends.query.filter_by(
            usernamea=username.data, usernameb=current_user.username
        ).all()
        if friendsa or friendsb:
            raise ValidationError("已经是好友了。")


class CreateRoomForm(FlaskForm):
    roomname = StringField("Roomname", validators=[DataRequired()])
    username = StringField("Username to add", validators=[DataRequired()])
    submit = SubmitField("Add")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not (user):
            raise ValidationError("没有找到username。")

    def validate_roomname(self, roomname):
        if not (is_latin(roomname.data)):
            raise ValidationError("只支持英文字母。")
