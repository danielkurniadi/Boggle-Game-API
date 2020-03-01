import bson
from app import flask_app, db


# -------------------
# POST
# -------------------

def test_create_random_board_game(client, post):
    payload = {
        "random": True,
        "duration": 1000
    }

    data, resp = post(
        client,
        '/games/',
        payload
    )

    assert resp._status_code == 201

    assert "id" in data
    assert "token" in data
    assert "duration" in data
    assert "board" in data

    assert len(data["id"]) == 24
    assert bson.ObjectId.is_valid(data["id"])

    board_string = data["board"].replace(' ', '').split(',')
    assert len(board_string) == 16

    assert data["duration"] > 0


def test_create_specified_board_game(client, post):
    expected_board_string = "A, C, E, D, L, U, G, *, E, *, H, T, G, A, F, K"
    payload = {
        "random": False,
        "duration": 1000,
        "board": expected_board_string
    }

    data, resp = post(
        client,
        '/games/',
        payload
    )

    assert resp._status_code == 201

    assert "id" in data
    assert "token" in data
    assert "duration" in data
    assert "board" in data

    assert len(data["id"]) == 24
    assert bson.ObjectId.is_valid(data["id"])

    assert data["board"] == expected_board_string
    assert data["duration"] > 0


def test_create_default_board_game(client, post):
    default_board_string = ', '.join(flask_app.config['DEFAULT_BOARD_STRING'])
    payload = {
        "random": False,
        "duration": 1000
    }

    data, resp = post(
        client,
        '/games/',
        payload
    )

    assert resp._status_code == 201

    assert "id" in data
    assert "token" in data
    assert "duration" in data
    assert "board" in data

    assert len(data["id"]) == 24
    assert bson.ObjectId.is_valid(data["id"])

    assert data["board"] == default_board_string
    assert data["duration"] > 0


def test_cannot_create_missing_field(client, post):
    payload = {
        # missing:
        #  "random": True,
        "duration": 1000
    }

    data, resp = post(
        client,
        '/games/',
        payload
    )

    assert resp._status_code == 400
    assert data['error_code'] == 4


def test_cannot_create_invalid_duration(client, post):
    payload = {
        "random": False,
        "duration": 0
    }

    data, resp = post(
        client,
        '/games/',
        payload
    )

    assert resp._status_code == 400
    assert data['error_code'] == 4
