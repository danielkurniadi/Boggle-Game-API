import bson
from app import flask_app, db


# -------------------
# GET
# -------------------

def test_get_valid_game(client, get):
    # On going valid game (game one)
    # The game id can be found in file: tests/schema/game.json 
    # TODO: do not hardcode id.
    data, resp = get(
        client,
        '/games/{id}'.format(id="abcdabcd1234abcdabcd1234")
    )

    assert "id" in data
    assert "token" in data
    assert "duration" in data
    assert "board" in data
    assert "time_left" in data
    assert "points" in data

    assert data["duration"] > 0
    assert 0 < data["time_left"] <= data["duration"]
    assert data["id"] == "abcdabcd1234abcdabcd1234"


def test_get_invalid_game_id(client, get):
    # TODO: do not hardcode id.
    data, resp = get(
        client,
        '/games/{id}'.format(id=-1)
    )

    assert resp._status_code == 404
