from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    # check if username already exists in database
    if username_exists(username):
        # display error message
        error = "Username already exists"
        return render_template('login.html', error=error)
    else:
        # check if password is correct
        # if correct, redirect to home page
        # if not correct, show error message
        return f"Username: {username}, Password: {password}"


def username_exists(username):
    # check if username exists in database
    # return True if it does, False otherwise
    pass


# @app.route('/signup', methods=['get'])
# def login():
#     return render_template('signup.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        password = request.form['password']

        # Check if username already exists in database
        # This is just an example, you will need to implement the check based on your database setup
        if username_exists_in_database(username):
            return 'Username already exists'
        else:
            # Add user to database
            # This is just an example, you will need to implement adding the user based on your database setup
            add_user_to_database(first_name, last_name, username, password)
            return redirect(url_for('login'))
    else:
        return render_template('signup.html')


def username_exists_in_database(username):
    # Check if username already exists in database
    # This is just an example, you will need to implement the check based on your database setup
    pass


def add_user_to_database(first_name, last_name, username, password):
    # Add user to database
    # This is just an example, you will need to implement adding the user based on your database setup
    pass


def url_for(string):
    if string == 'login':
        return '/'


if __name__ == '__main__':
    app.run()
