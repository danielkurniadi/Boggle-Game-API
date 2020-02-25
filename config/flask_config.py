import os
from os.path import join, dirname, abspath

from dotenv import load_dotenv
import pytz

# Define the application directory
BASE_DIR = abspath(dirname(dirname(__file__)))

# Load environment variables from file
dotenv_path = join(BASE_DIR, '_env')
load_dotenv(dotenv_path)

# Statement for enabling the development environment
DEBUG = os.environ.get('DEBUG', False)
ENV = os.environ.get('ENV', 'test')  # Flask Environment mode: development, test, production

# Define the database - we are working with
# SQLite for this example
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@127.0.0.1:3306/boogle'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}
TRAP_HTTP_EXCEPTIONS = True

# Application threads. A utils general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = 'secret'

# Secret key for signing cookies
SECRET_KEY = os.environ.get('JWT_ENCRYPTION_KEY', 'secret')
