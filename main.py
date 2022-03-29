from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

class UserForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('log In')


app = Flask(__name__)
app.secret_key = 'LoveIsGoodFoeEveryThing'
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    user_form = UserForm()

    if user_form.validate_on_submit():
        if user_form.email.data == "admin@email.com" and user_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=user_form)


if __name__ == '__main__':
    app.run(debug=True)
