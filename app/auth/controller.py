
from flask import url_for, request, flash, session, redirect
from flask import render_template
from flask_login import login_user, logout_user, current_user, login_required
from .models import User, Profile
from datetime import timedelta
from werkzeug import secure_filename
from datetime import timedelta, datetime
from werkzeug.security import generate_password_hash, check_password_hash   
import os
from mongoengine import errors  as mgengErrors
import pymongo.errors as mongoErrs

from app import config
from . import auth as auth

"""! \brief Controller Class for Auth """


# #session management
# @auth.before_request
# def session_management():
#     # make the session last indefinitely until it is cleared
#     session.permanent = True
#     auth.permanent_session_lifetime = timedelta(minutes=5)
@auth.route('/login',methods=["GET","POST"])
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
        return redirect(url_for('main.index'))
    return render_template('auth/login.html',title="Skilled Worker")



#  Routing function for Registering New User
@auth.route('/register',methods=["GET","POST"])
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
        userid = request.form['userid']
        password = request.form['password']
        try:
            newUser = User()
            newUser.emailId = userid
            newUser.password = generate_password_hash(password)
            newUser.save()
        except  (mongoErrs.DuplicateKeyError, mgengErrors.NotUniqueError):
            #user already exists
            flash("User with given UserId already exists","danger")
            return render_template('auth/register.html',title="Skilled Worker")
        newUser = User.objects(emailId = userid).first()
        login_user(newUser)
        return redirect(url_for('main.index'))
    return render_template('auth/register.html',title="Skilled Worker")


@auth.route('/profile',methods=["GET","POST"])
@login_required
def profile():
    if(request.method =="POST"):
        if 'file' not in request.files:
            print('[error] No file part')
        else:
            file = request.files['file']

            if file.filename == '':
                #No FIle has been uploaded. 
                print('[error] No selected file')

            if file:
                #Save the file into the designated folder
                print("[info] trying to save file")
                #rename the file name before saving. Suffix DateTime.
                
                #UPLOAD_FOLDER = os.path.join('static','images')
                filename = secure_filename(file.filename)
                filename='.'.join(filename.split(".")[:-1])+"_"+str(current_user.emailId.split("@")[0]).replace("\.","")+"_"+datetime.now().strftime("%m%d%y%I%M%S")+"."+filename.split(".")[-1]
                #fileCaption+=filename
                file.save(os.path.join(config.UPLOAD_PATH, filename))
                
                userProfile = Profile.objects(userEmail = current_user.emailId).first()
                if(not userProfile):
                    userProfile = Profile()
                    userProfile.userEmail =  current_user.emailId
                userProfile.image = filename
                try:
                    userProfile.save()
                except  Exception:
                    #update existing object
                    print("Error in updating profile")
                #Profile.Objects().first()
        

        return render_template('main/profile.html',title="Skilled Worker")
    else:
        return render_template('main/profile.html',title="Skilled Worker")

def generateHash(password):
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(password + salt).hexdigest()
    return hashed_password



#  Routing function for Logout
@auth.route('/logout')
def logout():
    logout_user()
    flash('You were successfully logged out', 'success')
    return redirect(url_for('main.index'))