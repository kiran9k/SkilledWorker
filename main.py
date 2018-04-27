#!usr/bin/python
""" Main Entry point for CIQ dashboard """

from app import app
import config


if(__name__=='__main__'):
    """ Main Entry point for the App """
    app.run(host=config.HOST, port=config.PORT_NO, debug=config.DEBUG)

