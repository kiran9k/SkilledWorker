"""! \brief Model for authentication"""
"""   
Description :
    Creating the Tables and Schemas for handling the User and User Role data 
    Creating Marhsmallow schemas for given tables"""
from mongoengine import *
import datetime



class User(Document):
    """! \brief  Class for  User Model 
    """
    """Contains : 
        1. User Name
        2. User Email Id ( Unique Key)
        3. Password (Stored as Hash)
    """
    emailId = StringField(required = True,unique = True)
    password = StringField()

    def __repr__(self):
        return '<User %r>' % self.emailId

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.emailId)

class Profile(Document):
    userEmail = StringField(required = True, unique = True)
    name = StringField()
    skillSet = StringField()
    location = StringField()
    rating = FloatField()
    price = FloatField()
    age = IntField()
    sex = StringField()
    jobType = StringField()
    image = StringField()