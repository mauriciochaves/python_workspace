# -- FILE: features/environment.py
import os
import tempfile
from behave import fixture, use_fixture
# flaskr is the sample application we want to test
from flaskr import app, init_db


def before_feature(context, feature):
    context.base_url = context.config.userdata['URL']
    context.db, app.config['DATABASE'] = tempfile.mkstemp()
    app.testing = True
    context.client = app.test_client()
    with app.app_context():
        init_db()


def before_scenario(context, scenario):
    os.close(context.db)
    os.unlink(app.config['DATABASE'])