import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'gerke01'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'N04Oo7EOIbcFykIlssOkXWVaYeDeXYzH/2zewYT5mo0vYyssp/3BhgW3PmZ8FZ8K8iWz9TiYtjPYZw1m54tOCg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'gerke01.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'gerke01'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'gerke01'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Annkathrin002!'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###

    CLIENT_SECRET = "ao4RSUp23VSO~T8gQXJWT9j_~cZ-we~7Wb"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    # AUTHORITY = "https://login.microsoftonline.com/47e40f4b-24bc-4a7b-b6fb-972e0e9db20c"  # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/common"

    CLIENT_ID = "bf77329a-7ab4-4cbb-ae08-792dd093d919"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
