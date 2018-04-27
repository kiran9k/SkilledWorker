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

class Room(Document):
    """! \brief  Class for  Room Model 
    """
    """Contains : 
        1. Room ID (unique key)
        2. Floor Number
        3. Wing Name 
        4. Room Name
        5. Room Price ( Price of booking per day )
        6. Created On - Datetime Field which shows when booking was done
    """
    roomId = StringField(required = True,unique = True)
    floorNumber = IntField()
    wingName = StringField()
    roomName =  StringField()
    roomPrice = FloatField()
    createdOn = DateTimeField(default=datetime.datetime.utcnow)



class Booking(Document):
    """! \brief  Class for  Booking Model 
    """
    """Contains : 
        1. Booked by (refers to the User)
        2. Booking Id ( unique key)
        3. Booked Room (refers to the room Booked)
        4. Booking From DateTIme Feild
        5. Booking To DateTIme Feild
        6. Booking Price - Price of Booking
        7. Booking Status
        8. Updated On - Datetime Field which shows when booking was done
    """
    bookedBy = ReferenceField(User)
    bookingId = IntField(required = True,unique = True)
    bookedRoom =  ReferenceField(Room)
    bookingFromDate = DateTimeField()
    bookingToDate = DateTimeField()
    bookingPrice = FloatField()
    bookingStatus = BooleanField()
    updatedOn = DateTimeField(default=datetime.datetime.utcnow)