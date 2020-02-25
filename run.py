import os
from os.path import join, dirname

from dotenv import load_dotenv
from app import flask_app


if __name__ == '__main__':
    # Load environment variables from file
    dotenv_path = join(dirname(__file__), '_env')
    load_dotenv(dotenv_path)

    # Run WSGI application
    flask_app.run(
        host = os.environ['HOST'],
        port = os.environ['PORT'], 
        debug = os.environ.get('DEBUG', False)
    )
