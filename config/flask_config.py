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
# MongoDB for example:
# mongodb://localhost:27017/dbname
MONGODB_SETTINGS = {
    'host': os.environ['DATABASE_URI']
}
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

# Corpus (or language dictionary) text file
CORPUS_DIR = join(BASE_DIR, 'corpus/')

# Default Corpus to use
DEFAULT_CORPUS_PATH = os.environ.get('CORPUS_PATH', join(CORPUS_DIR, 'dictionary.txt'))
DEFAULT_CORPUS_NAME = 'default'

# Default board to use
DEFAULT_BOARD_STRING = 'TAP*EAKSOBRSS*XD'