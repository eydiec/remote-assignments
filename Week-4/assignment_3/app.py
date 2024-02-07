from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
app.secret_key='your-secret-key'

#MySQL Configuration
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='a12345678'
app.config['MYSQL_DB']='assignment'


mysql = MySQL(app)

@app.route('/')
def home():

    return render_template('home.html')



@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user WHERE email = %s", [email])

        if cur.fetchone():
            flash('Email already exists.')
            return redirect(url_for('home'))
        else:
            cur.execute("INSERT INTO user (username, email, password) VALUES (%s, %s, %s)", (username, email, hashed_password))
            mysql.connection.commit()
            session['username'] = username #set to session
            session['email'] = email
            return redirect(url_for('signup_success'))
        cur.close()
    return redirect(url_for('home'))

@app.route('/signin', methods=['POST'])
def signin():
    if request.method == 'POST':
        # username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("select username, email, password from user where email = %s", [email])
        user = cur.fetchone()
        if user and check_password_hash(user[2], password):
            session['username'] = user[0]
            session['email'] = user[1]
            return redirect(url_for('signin_success'))
        else:
            flash('Email or Password is incorrect.')
        cur.close()
    return redirect(url_for('home'))

@app.route('/signup_success')
def signup_success():
    if 'username' in session:
        return render_template('signup.html', username = session['username'])
    else:
        flash('Please sign up or sign in to access the member page.')
        return redirect(url_for('home'))

@app.route('/signin_success')
def signin_success():
    if 'username' in session:
        return render_template('signin.html', username = session['username'])
    else:
        flash('Please sign up or sign in to access the member page.')
        return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)