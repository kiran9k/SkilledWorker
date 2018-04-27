
from flask import Flask, send_from_directory, request, redirect, url_for, json, jsonify, \
    render_template, Response, session
from flask_login import current_user, login_required

from datetime import timedelta

from . import main as main

"""! \brief maincontroller Controller for main """

"""/////////////////////////
ROUTING FUNCTIONS for static files
Routing function for handling css, js, images & HTML
////////////////////////""" 


@main.route('/css/<path:path>')
def send_js(path):
    """! \brief  Routing function for static files
        Routing function for handling js files"""
    """Description : Sends the javascript file from static folders

    Route: /js/<path:path>
    """
    return send_from_directory('static/css', path)


@main.route('/js/<path:path>')
def send_css(path):
    """! \brief  Routing function for static files
        Routing function for handling CSS"""
    """Description : Sends the CSS file from static folders

    Route: /css/<path:path>
    """
    return send_from_directory('static/js', path)


@main.route('/image/<path:path>')
def send_image(path):
    """! \brief Routing function for static files
        Routing function for handling image Files"""
    """
    Description : Sends the Images file from static folders

    Route: /image/<path:path>"""
    return send_from_directory('static/images', path)


""" ROUTING FUNCTIONS for the content pages """


# Index Page Routing function
@main.route('/')
@main.route('/home')
def index():
    """! \brief  Routing function for Index Page
        Routing function for handling Main Index Page"""
    """Description : Sends the index.html file from static folders

    Route: /
    """
    return render_template('main/index.html',title='')



#  Routing function for Searching All Bookings by all users
@main.route('/showProfile', methods=["GET"])
@main.route('/search', methods=["GET"])
def search():
    return render_template("main/index.html",title="Skilled Worker")