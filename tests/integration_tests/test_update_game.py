import bson
from app import flask_app, db


# -------------------
# PUT
# -------------------

def test_update_valid_game_correct_word(client, put):
    # On going valid game (first game)
    # The first game token can be found in file: tests/schema/game.json 
    # TODO: do not hardcode token.
    
    expected_token = "tokenonetokenonetokenonetokenone"
    word = "gauge"
    payload = {
        "token": expected_token,
        "word": word
    }

    # The first game id can be found in file: tests/schema/game.json 
    # TODO: do not hardcode id.
    expected_id = "abcdabcd1234abcdabcd1234"
    data, resp = put(
        client,
        '/games/{id}'.format(id=expected_id),
        payload
    )

    assert resp._status_code == 200
    assert "id" in data
    assert "token" in data
    assert "time_left" in data
    assert "duration" in data
    assert "board" in data
    assert "points" in data
    assert "error_code" in data

    assert data['error_code'] == 0
    assert data["token"] == expected_token
    assert data["id"] == expected_id

    assert data["points"] == len(word)


def test_update_valid_game_incorrect_word(client, put, get):
    # On going valid game (2nd game)
    # The second game's token can be found in file: tests/schema/game.json 
    # TODO: do not hardcode token.
    
    expected_token = "tokentwotokentwotokentwotokentwo"
    word = "bogo"
    payload = {
        "token": expected_token,
        "word": word
    }

    # The second game's id can be found in file: tests/schema/game.json 
    # TODO: do not hardcode id.
    expected_id = "abcdabcd1234abcdabcd5678"
    data, resp = put(
        client,
        '/games/{id}'.format(id=expected_id),
        payload
    )

    assert resp._status_code == 400
    assert "error_code" in data
    assert data['error_code'] == 3

    # check the points does not increment
    data, resp = get(
        client,
        '/games/{id}'.format(id=expected_id),
    )

    assert "points" in data
    assert data["points"] == 0


def test_update_valid_game_repeat_word(client, put, get):
    # On going valid game (3rd game)
    # The third game's token can be found in file: tests/schema/game.json 
    # TODO: do not hardcode token.
    
    expected_token = "tokentritokentritokentritokentri"
    word = "gauge"
    payload = {
        "token": expected_token,
        "word": word
    }

    # Step 1. Give correct answer to a new game
    # The third game's id can be found in file: tests/schema/game.json 
    # TODO: do not hardcode id.
    expected_id = "abcdabcd1234abcdabcd9012"
    data, resp = put(
        client,
        '/games/{id}'.format(id=expected_id),
        payload
    )

    assert resp._status_code == 200
    assert "id" in data
    assert "token" in data
    assert "time_left" in data
    assert "duration" in data
    assert "board" in data
    assert "points" in data
    assert "error_code" in data

    assert data['error_code'] == 0
    assert data["token"] == expected_token
    assert data["id"] == expected_id

    assert "points" in data
    assert data["points"] == len(word)

    # Step 2. Repeat answer and verify points not increasing

    # The third game's id can be found in file: tests/schema/game.json 
    # TODO: do not hardcode id.
    expected_id = "abcdabcd1234abcdabcd9012"
    data, resp = put(
        client,
        '/games/{id}'.format(id=expected_id),
        payload
    )

    assert "points" in data
    assert data["points"] == len(word)


def test_update_invalid_game(client, put):
    # Outdated game (4th game)
    # The fourth game's token can be found in file: tests/schema/game.json 
    # TODO: do not hardcode token.
    
    expected_token = "tokenfourtokenfourtokenfourtoken"
    word = "gauge"
    payload = {
        "token": expected_token,
        "word": word
    }

    # Step 1. Give correct answer to a new game
    # The fourth game's id can be found in file: tests/schema/game.json 
    # TODO: do not hardcode id.
    expected_id = "5e5a47997ba7cb8c171ad416"
    data, resp = put(
        client,
        '/games/{id}'.format(id=expected_id),
        payload
    )

    assert resp._status_code == 404
