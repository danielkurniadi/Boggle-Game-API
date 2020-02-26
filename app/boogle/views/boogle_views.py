"""
This module is for boogle API related
"""

from flask import Blueprint, request, jsonify

from app.boogle.service import boogle_service
from app.boogle.views.boogle_validators import (
    validate_update_game_request,
    validate_create_game_request
)

mod_boogle = Blueprint('boogle', __name__)


@mod_boogle.route('/games/', methods=['POST'])
@validate_create_game_request
def api_post_boogle():
    payload = dict(request.json)
    error_code, boogle_game = boogle_service.create_boogle_game(**payload)

    return jsonify({
        **error_code.to_dict(),
        **boogle_game
    }), error_code.http_code


@mod_boogle.route('/games/<game_id>', methods=['GET'])
def api_get_boogle(game_id):
    error_code, boogle_game = boogle_service.get_boogle_game(game_id)

    return jsonify({
        **error_code.to_dict(),
        **boogle_game
    }), error_code.http_code


@mod_boogle.route('/games/<game_id>', methods=['PUT'])
@validate_update_game_request
def api_put_boogle(game_id):
    payload = dict(request.json)
    error_code, boogle_game = boogle_service.update_boogle_game(game_id, **payload)

    return jsonify({
        **error_code.to_dict(),
        **boogle_game
    }), error_code.http_code
