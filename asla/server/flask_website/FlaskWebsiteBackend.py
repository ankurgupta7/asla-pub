from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)


def create_app():
    """
    Returns the app's name to bootstrap
    :return: the name of the app
    """
    bootstrap_app = Flask(__name__)
    Bootstrap(bootstrap_app)
    return bootstrap_app


@app.route('/')
def welcome_to_asla():
    """
    Landing page
    :return:
    """
    return render_template('index.html'), 200


@app.route('/signup', methods=['GET'])
def signup():
    """
    Allows for signup
    :return:
    """
    return render_template('signup.html')


@app.route('/login', methods=['GET'])
def login():
    """
    Allows for login
    :return:
    """
    return render_template('login.html')


@app.route('/login_expert', methods=['GET'])
def login_expert():
    """
    Allows for login
    :return:
    """
    return render_template('login_expert.html')


@app.route('/update', methods=['POST'])
def update():
    """
    updates a user
    :return:
    """
    return "Update"


@app.route('/authenticate', methods=['POST'])
def authenticate():
    return "Authenticate"


if __name__ == '__main__':
    app.run()
