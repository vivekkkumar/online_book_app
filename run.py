#!/usr/bin/env python3
# This is from the flask app package __init__ and not from the application's app package

from app import create_app, db

if __name__ == '__main__':
    flask_app = create_app('dev')

    ''' this is in application context, since many application are created
    by giving different parameters, app keep tracks of the db context for that
    app'''

    with flask_app.app_context():
        db.create_all()
    flask_app.run()
