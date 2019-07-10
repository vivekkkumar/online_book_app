import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
# read more about bootstrap

#Login Manager can handle user login and logout sessions
from flask_login import LoginManager

# used to decrypt a password instead of storing it as plain text
from flask_bcrypt import Bcrypt



# Initialize the db ORM instance

db = SQLAlchemy()

bootstrap = Bootstrap()

# this method can be used an app factory by passing the config type on the fly by mentioning them in run.py

login_manager = LoginManager()

# maintain cokkies and session  for the logged in User
login_manager.login_view = 'authentication.do_the_login'

# will delete the cookies and other context for the usr when user logs out or session is closed.
login_manager.session_protection = 'strong'

bcrypt = Bcrypt()

def create_app(config_type):
    app = Flask(__name__)

    # Either dev.py or prod.py from config folder.
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')

    # since this is a python file
    app.config.from_pyfile(configuration)

    # passing the app so the connection is established between ORM and the app

    db.init_app(app)

    bootstrap.init_app(app)

    login_manager.init_app(app)
    bcrypt.init_app(app)

    # this is not app package, this is flask app instance.
    from app.catalog import main

    app.register_blueprint(main)

    from app.auth import authentication

    app.register_blueprint(authentication)

    return app



