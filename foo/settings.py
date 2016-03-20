import logging
import os


# Values from environment variables + development defaults.
LISTEN_PORT = int(os.environ.get("FOO_LISTEN_PORT", "8000"))
DSN = os.environ.get("FOO_DSN", "dbname=aio-web-sandbox host=localhost user=aio-web-sandbox")
SQLALCHEMY_URL = os.environ.get(
    "FOO_SQLALCHEMY_URL",
    "postgresql+psycopg2://aio-web-sandbox@localhost/aio-web-sandbox")
DEBUG = bool(int(os.environ.get("FOO_DEBUG", "1")))
PUB_SUB_BROKER_URL = os.environ.get(
    "FOO_PUB_SUB_BROKER_URL",
    "amqp://localhost")
LOGGING_CONFIG = os.environ.get(
    "FOO_LOGGING_CONFIG",
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "logging.conf"))
LOG_DIR = os.environ.get("FOO_LOG_DIR", ".")
LOG_TO_STDOUT = bool(int(os.environ.get("FOO_LOG_TO_STDOUT", "1")))
LOG_TO_FILES = bool(int(os.environ.get("FOO_LOG_TO_FILES", "1")))


# Configure logging.
logging.basicConfig(level=logging.DEBUG)
