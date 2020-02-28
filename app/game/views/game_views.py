"""
This module is for boogle API related
"""

from flask import Blueprint, request, jsonify

from app.game.libs import game_manager
from app.game.views.game_validators import (
    validate_update_game_request,
    validate_create_game_request
)

mod_game = Blueprint('boogle', __name__)


@mod_game.route('/games/', methods=['POST'])
@validate_create_game_request
def api_post_game():
    payload = dict(request.json)
    error_code, boogle_game = game_manager.create_boogle_game(**payload)

    return jsonify({
        **error_code.to_dict(),
        **boogle_game
    }), error_code.http_code


@mod_game.route('/games/<game_id>', methods=['GET'])
def api_get_game(game_id):
    error_code, boogle_game = game_manager.get_boogle_game(game_id)

    return jsonify({
        **error_code.to_dict(),
        **boogle_game
    }), error_code.http_code


@mod_game.route('/games/<game_id>', methods=['PUT'])
@validate_update_game_request
def api_put_game(game_id):
    payload = dict(request.json)
    error_code, boogle_game = game_manager.update_boogle_game(game_id, **payload)

    return jsonify({
        **error_code.to_dict(),
        **boogle_game
    }), error_code.http_code
