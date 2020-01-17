from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '07d083450f3d26dad14427328952b167bab600c113e70b50'

posts = [
    {
        'author': 'Chad Tennent',
        'title': 'First Post',
        'content': 'some content here',
        'date_posted': '12/31/2019',
    },
    {
        'author': 'Jane Doe',
        'title': 'Second post',
        'content': 'second post content',
        'date posted' : '12/31/2019',
    }
]

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html' )

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('homepage'))
    return render_template('register.html', title = 'Register', form =form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form =form)

if __name__ == '__main__':
    app.run(debug =True)