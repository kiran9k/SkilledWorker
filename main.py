import config
import datetime
import json
from functools import wraps
import sys

import pymongo.errors as mongoErrs

from flask import Flask, send_from_directory, request, redirect, url_for, json, jsonify, render_template, Response, session, flash
from flask_login import login_user, logout_user, current_user, LoginManager, login_required, UserMixin

from werkzeug.security import generate_password_hash, check_password_hash
from mongoengine import connect
from mongoengine import *
from mongoengine import errors  as mgengErrors
from models import User, Room, Booking
from mongoengine.queryset.visitor import Q
from mongoengine.connection import MongoEngineConnectionError

try:
    conn = connect(config.MONGO_DATABASE_DB, host = config.MONGO_HOST, port = config.MONGO_PORT, username = config.MONGO_USERNAME, password =config.MONGO_USER_PASSWORD)
    #conn = connect(config.MONGO_DATABASE_DB, host ="localhost", port =27017)
except MongoEngineConnectionError as e:
    print("Connection to given mongodb Settings Failed. Please check for connection parameters")
    sys.exit(0)


app = Flask(__name__,static_url_path='')


app.config['SECRET_KEY'] = config.SECRET_KEY


login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "login"



#db = MongoEngine(app)

#Load user to load user from ID upon new request.. Commented out now for testing 
@login_manager.user_loader
def load_user(user_id):
    return User.objects(emailId = user_id).first()



#login_required() overriden inorder to accomodate next params
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if (not current_user.is_authenticated):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

#Routing Function 


# Index Page Routing function
@app.route('/')
def main():
    """! \brief  Routing function for Index Page
        Routing function for handling Main Index Page"""
    """Description : Sends the index.html file from static folders

    Route: /
    """
    return render_template('main/index.html')


#  Routing function for Logout
@app.route('/logout')
def logout():
    logout_user()
    flash('You were successfully logged out', 'success')
    return redirect(url_for('main'))


#  Routing function for Login
@app.route('/login',methods=["GET","POST"])
def login():
    """! \brief  Routing function for Login
    """
    """Description : 
        1. Gets user Credentials through Post request
        2. Checks if User is valid User
        3. Logs the user in  and redirects to index Page

    Route: /login
    """
    if request.method == 'POST':
        #get user name,email, id
        userid = request.form['username']
        password = request.form['password']
        newUser= User.objects(emailId = userid).first()
        if(newUser == None):
            flash("User is not registered. Please Click SignUp to register. ","danger")
            return render_template('auth/login.html')
        if(check_password_hash( password, newUser.password)):
            flash("UserId/Password combination incorrect","danger")
            return render_template('auth/login.html')
        login_user(newUser)
        flash('You were successfully logged in', 'success')
        return redirect(url_for('main'))
    return render_template('auth/login.html')


#  Routing function for Registering New User
@app.route('/register',methods=["GET","POST"])
def register():
    """! \brief  Routing function for Registering New User
    """
    """Description : 
        1. Gets user information through Post request
        2. Checks if User is already a User of System.
        3. Logs the user in  and redirects to index Page

    Route: /register
    """
    if request.method == 'POST':
        #get user name,email, id
        username = request.form['username']
        userid = request.form['userid']
        password = request.form['password']
        try:
            newUser = User()
            newUser.emailId = userid
            newUser.name = username
            newUser.password = generate_password_hash(password)
            newUser.save()
        except  (mongoErrs.DuplicateKeyError, mgengErrors.NotUniqueError):
            #user already exists
            flash("User with given UserId already exists","danger")
            return render_template('auth/register.html')
        newUser = User.objects(emailId = userid).first()
        login_user(newUser)
        return redirect(url_for('main'))
    return render_template('auth/register.html')



def generateHash(password):
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(password + salt).hexdigest()
    return hashed_password


#  Routing function for Showing All Available Rooms Given Date
@app.route('/bookRoom',methods=["GET","POST"])
@login_required
def bookRoom():
    """! \brief  Routing function for Showing All available Rooms
    """
    """Description : 
        1. Gets from Date and TO Date for booking from POST request
        2. Checks for any available room during that tenure
        3. Returns the List of Avaliable rooms 
        4. Renders bookRoom.html for normal Get Request

    Route: /bookRoom
    """
    if request.method == 'POST':
        #get user name,email, id
        fromDate = request.form['fromDate']
        toDate = request.form['toDate']
        fromDate = datetime.datetime.strptime(fromDate,'%m/%d/%Y %I:%M %p')
        toDate = datetime.datetime.strptime(toDate,'%m/%d/%Y %I:%M %p')
        try:
            existingBooking = Booking.objects (( Q(bookingFromDate__gte= fromDate) & Q(bookingFromDate__lte= toDate)) | (Q(bookingToDate__gte= fromDate) & Q(bookingToDate__lte= toDate)))
            allRooms = json.loads(Room.objects().to_json())
            availableRooms = []
            #check for available Rooms for given date
            for room in allRooms:
                roomBooked = False
                for noRoom in existingBooking:
                    if(room['roomId'] == noRoom.bookedRoom.roomId):
                        roomBooked = True
                        break
                if(not roomBooked):
                    availableRooms.append(room)
            #room.save()
            return jsonify({'AvailableRooms':availableRooms})
        except Exception as e:
            print(e.message)
            print(e)
            #room already exists
            #flash("Given room with Room Id already Exists.","danger")
            #print("dupliacte key exists")
            print("Exception Occured")
    return render_template('main/bookRoom.html')


#  Routing function for Searching All Bookings by all users
@app.route('/search',methods=["GET","POST"])
def search():
    return render_template("main/search.html")

#  Routing function for Searching All Bookings by all users
@app.route('/searchBooking',methods=["GET","POST"])
@login_required
def searchBooking():
    """! \brief  Routing function for Showing All Bookings
    """
    """Description : 
        1. Gets from Date and TO Date for booking from POST request
        2. Returns the List of Booked rooms  and Booking details
        4. Renders searchBooking.html for normal Get Request

    Route: /searchBooking
    """
    if request.method == 'POST':
        #get user name,email, id
        fromDate = request.form['fromDate']
        toDate = request.form['toDate']
        fromDate = datetime.datetime.strptime(fromDate,'%m/%d/%Y %I:%M %p')
        toDate = datetime.datetime.strptime(toDate,'%m/%d/%Y %I:%M %p')
        try:
            existingBooking = Booking.objects (( Q(bookingFromDate__gte= fromDate) & Q(bookingFromDate__lte= toDate)) | (Q(bookingToDate__gte= fromDate) & Q(bookingToDate__lte= toDate)))
            returnData = []
            for booking in existingBooking:
                returnObject = {}
                returnObject['name'] = booking.bookedBy.name
                returnObject['bookingFromDate'] = str(booking.bookingFromDate)
                returnObject['bookingToDate'] = str(booking.bookingToDate)
                returnObject['bookingPrice'] = float(booking.bookingPrice)
                returnObject['bookingId'] = int(booking.bookingId)
                returnObject['floorNumber'] = str(booking.bookedRoom.floorNumber)
                returnObject['roomId'] = str(booking.bookedRoom.roomId)
                returnObject['updatedOn'] = str(booking.updatedOn)
                returnData.append(returnObject)
            return jsonify({'BookedRooms':returnData})
        except Exception as e:
            print(e.message)
            print(e)
            print("Exception Occured")
    return render_template('main/searchBooking.html')


#  Routing function for Listing  All Bookings for given Room
@app.route('/showBooking',methods=["GET"])
@login_required
def showBooking():
    """! \brief  Routing function for Showing All Bookings for selected Room
    """
    """Description : 
        1. Gets room ID from URL
        2. Returns the List of  Booking details for given selected Room
        4. Renders showBookings.html for normal Get Request

    Route: /showBookings
    """
    roomId = None
    roomId = request.args.get('room')
    if(roomId == None):
        return redirect(url_for('rooms'))
    userBookings = Booking.objects(bookedRoom = Room.objects(roomId = roomId).first())
    return render_template('main/showBookings.html',currentRoom = Room.objects(roomId = roomId).first(), userBookings = userBookings)


#  Routing function for Listing  All Rooms
@app.route('/Rooms',methods=["GET","POST"])
@login_required
def rooms():
    """! \brief  Routing function for Showing All Room Information  and adding new Room
    """
    """Description : 
        1. For adding  new Room, ROOM details are obtained through POST request
        2. Checks if Room with given ROOM ID alerady Exists.
        3. If not, new room is added with provided room details
        2. Returns the List of  all  Room details
        3. Renders addRoom.html 

    Route: /Rooms
    """
    if request.method == 'POST':
        roomId = request.form['roomId']
        floorNumber = request.form['floorNumber']
        wingName = request.form['wingName']
        roomName = request.form['roomName']
        price = float(request.form['price'])

        try:
            room = Room()
            room.floorNumber = floorNumber
            room.roomId =  roomId 
            room.wingName = wingName
            room.roomPrice= price
            room.roomName = roomName
            room.save()
        except (mongoErrs.DuplicateKeyError, mgengErrors.NotUniqueError):
            flash("Given room with Room Id already Exists.","danger")
            print("dupliacte key exists")
    #get list of all rooms    
    return render_template('main/addRoom.html', AllRooms = Room.objects)


#  Routing function for Booking current Available  Room
@app.route("/api/bookAvailableRoom",methods=["POST"])
@login_required
def listAvailableRooms():
    """! \brief  Routing function for Booking given Rooms
    """
    """Description : 
        1. FromDate, ToDate, RoomId are obtained through POST request
        2. COmputes room fare for given days
        3. Creates a new Booking with given Room details and for current user
        4. Returns Status of adding new Booking

    Route: /api/bookAvailableRoom
    """
    fromDate = request.form['fromDate']
    toDate = request.form['toDate']
    fromDate = datetime.datetime.strptime(fromDate,'%m/%d/%Y %I:%M %p')
    toDate = datetime.datetime.strptime(toDate,'%m/%d/%Y %I:%M %p')
    roomId = request.form['roomId']
    room = Room.objects(roomId = roomId).first()
    booking = Booking()
    booking.bookedBy = User.objects(emailId = current_user.emailId).first()
    booking.bookedRoom = room
    booking.bookingFromDate = fromDate
    booking.bookingToDate = toDate
    booking.bookingPrice = int((toDate-fromDate).days)*room.roomPrice
    booking.bookingStatus = True
    booking.bookingId = Booking.objects.count() + 1
    status = 1
    try:
        booking.save()
    except Exception as e:
        status = 0
        print(e)
        print("error occured while saving a new booking")
    return jsonify({'status':1})

#  Routing function for Showing all Bookings under current Room
@login_required
@app.route('/api/showRoomBookings',methods=["POST"])
def showRoomBookings():
    """! \brief  Routing function for Showing all bookings under given Rooms
    """
    """Description : 
        1. RoomId are obtained through POST request
        2. Fetches all booking under given Room
        3. Returns list of  Bookings

    Route: /api/bookAvailableRoom
    """
    roomId = None
    roomId = request.form['room']
    if(roomId == None):
        return redirect(url_for('rooms'))
    userBookings = Booking.objects(bookedRoom = Room.objects(roomId = roomId).first())
    bookedRooms = []
    for booking in userBookings:
        returnObject = {}
        returnObject['name'] = booking.bookedBy.name
        returnObject['bookingFromDate'] = str(booking.bookingFromDate)
        returnObject['bookingToDate'] = str(booking.bookingToDate)
        returnObject['bookingPrice'] = float(booking.bookingPrice)
        returnObject['bookingId'] = int(booking.bookingId)
        returnObject['updatedOn'] = str(booking.updatedOn)
        bookedRooms.append(returnObject)
    return jsonify({'roomBookings':bookedRooms})

@app.route('/api/deleteBooking',methods=["POST"])
def deleteBooking():
    """! \brief  Routing function for deleting bookings 
    """
    """Description : 
        1. BookingID is obtained through POST request
        2. Fetches booking info under given BookingId
        3. Deletes the booking.
        4. Returns Status of booking deletion.

    Route: /api/deleteBooking
    """
    bookingId = int(request.form['bookingId'])
    booking = Booking.objects(bookingId = bookingId)
    booking.delete()
    return jsonify({'status':1})

@app.errorhandler(500)
def server_error(e):
    """! \brief  Routing function for handling Errors 
    """
    """Description : 
        1. Routing function for handling Errors
        2. Renders 500 internal Error page

    """
    # Log the error and stacktrace.
    return 'An internal error occurred.', 500

if(__name__ =='__main__'):
    """! \brief  Main Entry Point
    """
    """Description : 
        1. Runs a Flask App

    """
    app.run(host=config.HOST, port=config.PORT_NO, debug= config.DEBUG)