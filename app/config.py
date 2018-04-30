""" @package : Config file for the CIQ App """
import os

# Statement for enabling the development environment
DEBUG = True

# Port Number
PORT_NO = 8080

# The Host IP
HOST = '0.0.0.0'

# Define the application directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Define the DB

# Define the DB (mongoLab)

MONGO_DATABASE_URI = 'mongodb://root:root@@ds147534.mlab.com:47534/'
MONGO_USERNAME = "root"
MONGO_USER_PASSWORD = "root"
MONGO_DB_NAME = "skilledworker"
MONGO_HOST = "ds147534.mlab.com"
MONGO_PORT = 47534
MONGO_DATABASE_DB = 'skilledworker'


#parent =  os.path.abspath(os.path.join())
UPLOAD_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)),'static','images')

# Secret key for signing cookies
SECRET_KEY = "MyCIQdAsHbOaRdsecretKey123"

