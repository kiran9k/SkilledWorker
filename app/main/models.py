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
    name = StringField()
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