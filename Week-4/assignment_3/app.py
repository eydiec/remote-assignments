from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql.cursors
from werkzeug.security import check_password_hash, generate_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key='your-secret-key'
app.config['WTF_CSRF_ENABLED'] = False

#MySQL Configuration
# app.config['MYSQL_HOST']='localhost'
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']='a12345678'
# app.config['MYSQL_DB']='assignment'
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'a12345678',
    'database': 'assignment',
    'cursorclass': pymysql.cursors.DictCursor
}

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

@app.route('/')
def home():

    return render_template('home.html')


@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        username = form.username.data
        email = form.email.data
        password = form.password.data
        hashed_password = generate_password_hash(password)
        if not form.validate_on_submit():
            if form.email.errors:
                flash('Wrong email format!')
                return redirect(url_for('home'))
        connection = pymysql.connect(**db_config)



        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM user WHERE email = %s", [email])

            if cursor.fetchone():
                flash('Email already exists.')
                return redirect(url_for('home'))

            else:
                cursor.execute("INSERT INTO user (username, email, password) VALUES (%s, %s, %s)", (username, email, hashed_password))
                connection.commit()
                session['username'] = username #set to session
                session['email'] = email
                return redirect(url_for('signup_success'))
        connection.close()

    return render_template('home.html', form=form)

@app.route('/signin', methods=['POST'])
def signin():
    if request.method == 'POST':
        # username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        connection = pymysql.connect(**db_config)

        with connection.cursor() as cursor:
            cursor.execute("select username, email, password from user where email = %s", [email])
            user = cursor.fetchone()
            if user and check_password_hash(user['password'], password):
                session['username'] = user['username']
                session['email'] = user['email']
                return redirect(url_for('signin_success'))
            else:
                flash('Email or Password is incorrect.')
        connection.close()
    return redirect(url_for('home'))

@app.route('/signup_success')
def signup_success():
    if 'username' in session:
        return render_template('signup.html', username = session['username'])


@app.route('/signin_success')
def signin_success():
    if 'username' in session:
        return render_template('signin.html', username = session['username'])
    

if __name__=='__main__':
    app.run(debug=True)
