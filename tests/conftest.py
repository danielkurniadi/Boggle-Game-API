import pytest
import os, json

from app import flask_app

from tests.utils.data_utils import (
    rand_string, create_solution,
    create_corpus_words, create_wrong_words,
)
from tests.utils.db_utils import setup_all_models


# ----------------------
# HOOKS
# ----------------------

def pytest_configure():
    setup_all_models()


def pytest_sessionfinish(session, exitstatus):
    from app import flask_app, db
    with flask_app.app_context():
        db_name = db.get_db().name
        db.connection.drop_database(db_name)
    print("\n\nTearing Down Test DataBase ...")


# -----------------------
#  FIXTURES
# -----------------------

@pytest.fixture
def client():
    from app import flask_app
    yield flask_app


def get_url(url, query):
    if isinstance(query, dict):
        return url + '?' + urlencode(query)
    return url


def test_client_call(method, app, url, query=None, payload=None):
    params = {'content_type': 'application/json'}
    headers = {}
    if payload:
        params.update(dict(data=json.dumps(payload)))
    final_url = get_url(url, query)
    resp = getattr(app.test_client(), method)(
        final_url, **params, headers=headers)
    data = json.loads(resp.get_data(as_text=True))
    return data, resp


@pytest.fixture
def get():
    def get_wrapper(app, url, query=None):
        return test_client_call(method='get', **locals())
    return get_wrapper


@pytest.fixture
def post():
    def post_wrapper(app, url, payload, query=None):
        return test_client_call(method='post', **locals())
    return post_wrapper


@pytest.fixture
def put():
    def put_wrapper(app, url, payload, query=None):
        return test_client_call(method='put', **locals())
    return put_wrapper


@pytest.fixture
def delete():
    def delete_wrapper(app, url, query=None):
        return test_client_call(method='delete', **locals())
    return delete_wrapper


# --------------------
# DATA FIXTURES
# --------------------

@pytest.fixture
def board_string():
    return 'ACEDLUG*E*HTGAFK'


@pytest.fixture
def solution():
    return create_solution()


@pytest.fixture
def corpus_words():
    return create_corpus_words()


@pytest.fixture
def wrong_words():
    return create_wrong_words()
