import os

DEBUG = True

# Port Number
PORT_NO = 8080

# The Host IP
HOST = '0.0.0.0'

# Define the application directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Define the DB (mongoLab)
MONGO_DATABASE_URI = 'mongodb://root:root@ds137054.mlab.com:37054/'
MONGO_USERNAME = "root"
MONGO_USER_PASSWORD = "root"
MONGO_DB_NAME = "room-scheduler"
MONGO_HOST = "ds137054.mlab.com"
MONGO_PORT = 37054

MONGO_DATABASE_DB = 'room-scheduler'

# Secret key for signing cookies
SECRET_KEY = "MyRooMS#cH3dUleRsecretKey123"