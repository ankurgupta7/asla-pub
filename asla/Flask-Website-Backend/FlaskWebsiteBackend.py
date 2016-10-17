from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome_to_asla():
    """
    Landing page
    :return:
    """
    return 'Welcome to Asla'


@app.route('/signup', methods=['POST'])
def signup():
    """
    Allows for signup
    :return:
    """
    return "Signup"


@app.route('login/', methods=['POST'])
def login():
    """
    Allows for login
    :return:
    """
    return "Login"


@app.route('/update', methods=['POST'])
def update():
    """
    updates a user
    :return:
    """
    return "Update"


@app.route('/authenticate', method=['POST'])
def authenticate():
    return "Authenticate"


if __name__ == '__main__':
    app.run()
