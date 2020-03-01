# `BOGGLE GAME API`

## Notes

### Error Codes
```python
# Base Error Codes
ServerOk = 0
SERVER_ERROR = 1

# Error Codes
ResourceNotFound = 2
OperationNotSupported = 3
InvalidRequest = 4
DatabaseError = 5
```

### Response Fields

- `id`: a BSON `ObjectId` that uniquely identifies a game resource
- `result`: whether response data can be found in body
- `error_code`: extend status of response and indicate which error happened


## `GET /games/<:id>`

Retrieve the a particular game's status

- Response:
  + Success (status 200 OK)

```json
{
  "result": true,
  "error_code": 0,
  "id": "5e5a43f7adb9edc9f0b2a52e",
  "token": "9dda26ec7e476fb337cb158e7d31ac6c",
  "duration": 12345,
  "board": "A, C, E, D, L, U, G, *, E, *, H, T, G, A, F, K",
  "time_left": 10000,
  "points": 10
}
```

## `POST /games/`

Create new boggle game.


- Parameters:
  + `duration` (required): the time (in seconds) that specifies the duration of
    the game
  + `random` (required): if `true`, then the game will be generated with random
    board.  Otherwise, it will be generated based on input.
  + `board` (optional): if `random` is not true, this will be used as the board
    for new game. If this is not present, new game will get the default board
    from `test_board.txt`

- Request:
    + Success (status 201 OK)

```json
{
  "duration": 6000,
  "random": false,
  "board": "A, C, E, D, L, U, G, *, E, *, H, T, G, A, F, K",
}
```

Response

```json
{
  "id": "5e5a43f7adb9edc9f0b2a52e",
  "token": "9dda26ec7e476fb337cb158e7d31ac6c",
  "duration": 6000,
  "board": "A, C, E, D, L, U, G, *, E, *, H, T, G, A, F, K"
}
```

## `PUT /games/<:id>`

Update game by sending the guess word from user. If user's guess is correct, return status `200 OK`. Otherwise return status `400 BAD_REQUEST`

- Parameters:
  + `id` (required): The ID of the game
  + `token` (required): The token for authenticating the game
  + `word` (required): The word that can be used to play the game

- Request:
    + Success (status 200 OK)
    + Failure (status 400 BAD_REQUEST) for **wrong answer** or invalid request

```json
{
  "token": "9dda26ec7e476fb337cb158e7d31ac6c",
  "word": "HUG",
}
```