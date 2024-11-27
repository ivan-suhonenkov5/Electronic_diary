from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from app.models.user import User


class RegistrationForm(FlaskForm):
    name = StringField("ФИО", validators=[DataRequired(), Length(min=2, max=100)])
    login = StringField("Логин", validators=[
        DataRequired(),
        Length(min=2, max=20)])
    password = PasswordField("Пароль", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Подтвердите пароль", validators=[DataRequired(), EqualTo("password")]
    )
    avatar = FileField(
        "Загрузите аватар", validators=[
            FileRequired(message="Файл обязательный для загрузки"),
            FileAllowed(["jpg", "jpeg", "png"], message="Допустимые форматы: jpg, jpeg, png")]
    )
    submit = SubmitField("Зарегистрироваться")

    def validate_login(self, login):
        if User.query.filter_by(login=login.data).first():
            raise ValidationError('Данное имя пользователя уже занято!')


class LoginForm(FlaskForm):
    """Form for login users"""
    login = StringField("Логин", validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField("<PASSWORD>", validators=[DataRequired()])
    remember = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")


class StudentForm(FlaskForm):
    student = SelectField("student", choices=[], render_kw={"class": "form-control"})

class TeacherForm(FlaskForm):
    teacher = SelectField("teacher", choices=[], render_kw={"class": "form-control"})