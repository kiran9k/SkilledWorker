
from flask import url_for, request, flash, session, redirect, jsonify
from flask import render_template
from flask_login import login_user, logout_user, current_user, login_required
from ..auth.models import Profile
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash   
from mongoengine.queryset.visitor import Q
from mongoengine import errors  as mgengErrors
import pymongo.errors as mongoErrs

import json
from . import api as api


@api.route('/saveProfile',methods=["POST","GET"])
@login_required
def saveProfile():
    if(request.method =="POST"):
        response_data = json.loads(request.data)
        profile = response_data['profile']
        userProfile = Profile.objects(userEmail = current_user.emailId).first()
        if(not userProfile):
            userProfile = Profile()
            userProfile.userEmail =  current_user.emailId
            if(profile['sex']=="Male"):
                userProfile.image = "defaultMale.png"
            else:
                userProfile.image = "defaultFemale.png"
        try:
            userProfile.name = profile['name']
            userProfile.price = float(profile['price'])
            userProfile.rating = float(profile['rating'])
            userProfile.skillSet = profile['skillSet']
            userProfile.location = profile['location']
            userProfile.age = profile['age']
            userProfile.jobType = profile['jobType']
            userProfile.sex = profile['sex']
        except KeyError:
            return jsonify({'status':0})
        

        try:
            userProfile.save()
        except  (mongoErrs.DuplicateKeyError, mgengErrors.NotUniqueError):
            #update existing object
            print("Error in updating profile")
        #Profile.Objects().first()
        return jsonify({'status':1})
    else:
        userProfile ={}
        try:
            userProfile = json.loads(Profile.objects(userEmail = current_user.emailId).first().to_json())
        
            if(userProfile):
                userProfile.pop("_id")
                userProfile.pop("userEmail")
        except Exception:
            pass
        return jsonify({'profile':userProfile})


@api.route("/getUsersProfile",methods=["POST"])
def getUsersProfile():
    response_data = json.loads(request.data)
    email = response_data['emailId']
    print(email)
    userProfile ={}
    try:
        userProfile = json.loads(Profile.objects(userEmail = email).first().to_json())
    
        if(userProfile):
            userProfile.pop("_id")
            userProfile.pop("userEmail")
    except Exception:
        pass
    return jsonify({'profile':userProfile})

@api.route("/listFilterJobs",methods=["GET"])
def listFilterJobs():
    searchResult = Profile.objects()
    location=[]
    for i in searchResult:
        location.append(str(i.location))
    location =list(set(location))

    return jsonify({"location":location})


@api.route("/fileredSearchJobs",methods=["POST"])
def filteredSearchJobs():

    response_data = json.loads(request.data)
    skill = str(response_data['skill'])
    location = str(response_data['location'])
    jobType = str(response_data['fulltime'])
    gender = str(response_data['gender'])
    age = str(response_data['age'])
    salary = str(response_data['salary'])
    age_lt=0
    age_gt=150
    salary_lt=0
    salary_gt =1000000
    
    if(len(age)>0):
        age_lt=age.split("-")[0]
        age_gt=age.split("-")[1]
    if(len(salary)>0):
        salary_lt=salary.split("-")[0]
        salary_gt=salary.split("-")[1]
    print(location,age_gt,age_lt,salary_gt,salary_lt)
    searchResult = Profile.objects(Q(skillSet__icontains= skill) & Q(sex__icontains= gender) & Q(jobType__icontains= jobType) & Q(location__icontains= location) & Q(age__lte= age_gt) & Q(age__gte= age_lt) & Q(price__lte= salary_gt) & Q(price__gte= salary_lt)).to_json()
    return jsonify(json.loads(searchResult))


@api.route("/searchJobs",methods=["POST"])
def searchJobs():
    response_data = json.loads(request.data)
    skill = response_data['skill']
    location = response_data['location']
    print(skill + " "+location)
    searchResult = Profile.objects(Q(skillSet__icontains= skill) & Q(location__icontains= location)).to_json()
    return jsonify(json.loads(searchResult))