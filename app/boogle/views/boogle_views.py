"""
This module is for boogle API related
"""

from flask import Blueprint, request, jsonify

from app.boogle.service import import boogle_manager
from app.boogle.views.boogle_validators import (
    update_game_validator,
    create_game_validator
)
from app.bridge.error import get_msg_error, get_http_status_code

mod_boogle = Blueprint('boogle', __name__)


@mod_boogle.route('/games/<game_id>', methods=['GET'])
@create_game_validator
def api_get_boogle(game_id):
    error_code, boogle_game = boogle_manager.get_boogle_by_game_id(game_id)

    return jsonify({
        **get_msg_error(error_code),
        **boogle_game
    })


@mod_boogle.route('/games/<game_id>', methods=['PUT'])
@update_game_validator
def api_put_boogle(game_id):
    payload = dict(request.json)
    error_code, boogle_game = boogle_manager.update_boogle_by_game_id()

    return jsonify({
        **get_msg_error(error_code),
        **boogle_game
    })


@mod_boogle.route('/games/', methods=['POST'])
def api_post_boogle():
    payload = dict(request.json)
    error_code, boogle_game = boogle_manager.create_boogle_game(**payload)

    return jsonify({
        **get_msg_error(error_code),
        **boogle_game
    })
