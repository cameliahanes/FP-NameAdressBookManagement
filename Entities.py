class Person(object):
    
    def __init__(self, entity_id, name, number, address):
        self.__entity_id = entity_id
        self.__name = name
        self.__number = number
        self.__address = address
        
    @property
    def entity_id(self):
        return self.__entity_id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def number(self):
        return self.__number
    
    @property
    def address(self):
        return self.__address
    
    @staticmethod
    def create_entity_csv(line):
        line = line.split(",")
        return Person(int(line[0]), line[1], int(line[2]), line[4])
    
    @staticmethod
    def format_csv(lst):
        return str(lst[1].entity_id + ","+lst[1].name+","+lst[1].number+","+lst[1].address)
    
    
class Activity(object):
    
    def __init__(self, entity_id, date, time, description):
        self.__entity_id = entity_id
        self.__date = date
        self.__time = time
        self.__description = description
        
    @property
    def entity_id(self):
        return self.__entity_id
    
    @property
    def date(self):
        return self.__date
    
    @property
    def time(self):
        return self.__time
    
    @property
    def description(self):
        return self.__description
    
    @staticmethod
    def format_csv(lst):
        return str(lst[1].entity_id +","+lst[1].date+","+lst[1].time+","+lst[1].description)
    
    @staticmethod
    def create_entity_csv(line):
        return Activity(int(line[0]), line[1], line[2], line[3])
    


class Attendance(object):
    
    def __init__(self, entity_id, person_id, activity_id):
        self.__entity_id = entity_id
        self.__person_id = person_id
        self.__activity_id = activity_id

    @property
    def entity_id(self):
        return self.__entity_id
    
    @property
    def person_id(self):
        return self.__person_id
    
    @property
    def activity_id(self):
        return self.__activity_id
    
    @staticmethod
    def format_csv(lst):
        return str(lst[1].__entity_id + ","+lst[1]._person_id + ","+lst[1].__activity_id)
    
    @staticmethod
    def create_entity_csv(line):
        line = line.split(",")
        return Attendance(int(line[0]), int(line[1]), int(line[2]))

import unittest
from unittest import TestCase
import datetime
class test_entities(unittest.TestCase):
    
    def setup(self):
        super.setUp()
        
    def testPerson(self):
        pers = Person(19, "Cami", 752831148, "Dunarii 19A")
        self.assertEqual(pers.entity_id, 19, "Id should be 19!")
        self.assertEqual(pers.name, "Cami", "Name should be Cami!")
        self.assertEqual(pers.number, 752831148, "Number should be 0752831148!")
        self.assertEqual(pers.address, "Dunarii 19A", "Address should be Dunarii 19A")
        
    def testActivity(self):
        act = Activity(2, "2016-10-19", "14:00", "activity")
        self.assertEqual(act.entity_id, 2, "-")
        self.assertEqual(act.date, "2016-10-19", 'no msg')

    def testAttendance(self):
        act = Activity(2, "2016-10-19", "14:00", "activity")
        pers = Person(19, "Cami", 752831148, "Dunarii 19A")
        att = Attendance(1, pers.entity_id, act.entity_id)
        self.assertEqual(att.entity_id, 1, "msg")
        self.assertEqual(att.person_id, pers.entity_id, "-")
        self.assertEqual(att.activity_id, act.entity_id, "assertion failed")

    def testAll(self):
        self.testActivity()
        self.testPerson()
        self.testAttendance()
        
import time
t = test_entities()
t.testAll()
print(datetime.time())
print(time.asctime())
print(time.strftime("%H:%M"))