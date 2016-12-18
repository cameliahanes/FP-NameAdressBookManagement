'''
Created on 16 dec. 2016

@author: Camelia
'''

class PersonException(Exception):
    pass

class PersonValidator(object):
    @staticmethod
    def validate(person):
        err = ""
        if len(str(person.entity_id)) == 0:
            err += "Person must have an ID!"
        if len(str(person.name)) == 0 :
            err += "Person must have a name!"
        if len(str(person.number)) == 0:
            err += "Person must have a number!"
        if len(str(person.address)) == 0:
            err += "Person must have an address!"
        if len(err) > 0:
            raise PersonException(err)
        
        
class ActivityException(Exception):
    pass 
    
    
class ActivityValidator(object):
    @staticmethod
    def validate(activity):
        err = ""
        if len(str(activity.entity_id)) == 0:
            err += "Activity must have an id!"
        if len(str(activity.date)) == 0:
            err += "Activity should have a date!"
        if len(str(activity.time)) == 0:
            err += "Activity should have a time!"
        if len(str(activity.description)) == 0:
            err += "Activity should have a descrption!"
        if len(err) > 0:
            raise ActivityException(err)
        
class AttendanceException(Exception):
    pass

        
class AttendanceValidator(object):
    @staticmethod
    def validate(att):
        err = ""
        if len(str(att.entity_id)) == 0:
            err += "Attendance should have an id!"
        if len(str(att.person_id)) == 0:
            err += "Attendance should have a person's id!"
        if len(str(att.activity_id)) == 0:
            err += "Attendance should have an activity id!"
        if len(err) > 0:
            raise AttendanceException(err)