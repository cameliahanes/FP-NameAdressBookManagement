'''
Created on 16 dec. 2016

@author: Camelia
'''
class InexistentFileException(Exception):
    pass

import collections

class DuplicatedIDException(Exception):
    pass

class InexistentIDException(Exception):
    pass

class Repository(object):
    
    def __init__(self, filename, validator, entity_class):
        self.__filename = filename
        self.__validator = validator
        self.__entity_class = entity_class
        self.__entities = {}
        self.load_from_file()
        
    def load_from_file(self):
        try:
            with open(self.__filename, "r") as f:
                for line in f:
                    entity = self.__entity_class.create_entity_csv
                    self.__entities[entity.entity_id] = entity 
        except IOError:
            raise InexistentFileException("File {0} does not exist!".format)
        
    
    def get_all(self):
        return collections.OrderedDict(sorted(self.__entities.items()))
    
    def get_all_id(self):
        dict = collections.OrderedDict(sorted(self.__entities.items()))
        return list(dict.keys())
    
    def save(self, entity):
        self.__validator.validate(entity)
        if int(entity.entity_id) in self.__entities:
            raise DuplicatedIDException("Duplicated ID!")
        self.__entities[entity.entity_id] = entity
        try:
            with open(self.__filename, "w") as f:
                for e in self.__entities:
                    lst = [e, self.__entities[e]]
                    f.write(self.__entity_class.format_csv(lst))
        except IOError:
            raise InexistentFileException("Inexistent file!")
        
    def remove(self, entity_id):
        if int(entity_id) not in self.__entities:
            raise InexistentIDException("Inexistent ID!")
        self.__entities.pop(int(entity_id))
        try:
            with open(self.__filename, "w") as f:
                for e in self.__entities:
                    lst = [e, self.__entities[e]]
                    f.write(self.__entity_class.format_csv(lst))
        except IOError:
            raise InexistentFileException("Inexistent file!")
        
    def update(self, entity):
        self.__validator.validate(entity)
        if int(entity.entity_id) not in self.__entities:
            raise InexistentIDException("Inexistent ID!")
        self.__entities[entity.entity_id] = entity
        try:
            with open(self.__filename, "w") as f:
                for e in self.__entities:
                    lst = [e, self.__entities[e]]
                    f.write(self.__entity_class.format_csv(lst))
        except IOError:
            raise InexistentFileException("Inexistent file!")