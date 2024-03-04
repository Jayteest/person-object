# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: September 25, 2023

# Description:
# This file contains the Student class, a subclass of the Person class.
# This class extends the Person class to include data attributes for
# major, GPA, and grade level.
# It contains methods for setting and getting each of these attributes.

# Logic:
# import person
# init:
#   set first, middle, last, dob, major, gpa, level to passed arguments,
#   or None if no argument passed
#   call init from Person
#   set major, gpa, level
# sets for major, gpa, level:
#   accept argument value, set attribute to argument value
# gets for major, gpa, level:
#   return attribute
# repr: return formatted string


# import Person class to use as superclass
import person

# declare Student class
class Student(person.Person):
    # initializer method to initialize object's data attributes
    def __init__(self, first=None, middle=None, last=None, dob=None, major=None, gpa=None, level=None):
        # call constructor from Person class to inherit attributes
        person.Person.__init__(self, first, middle, last, dob)
        # set additional attributes to corresponding passed argument
        self.__major = major
        self.__gpa = gpa
        self.__level = level

    # set method to allow user to set major
    def set_major(self, major):
        self.__major = major

    # set method to allow user to set GPA
    def set_gpa(self, gpa):
        self.__gpa = gpa

    # set method to allow user to set grade level classification
    def set_level(self, level):
        self.__level = level

    # get method to return major
    def get_major(self):
        return self.__major

    # get method to return GPA
    def get_gpa(self):
        return self.__gpa

    # get method to return grade level
    def get_level(self):
        return self.__level


    # repr method to return human readable representation of object
    def __repr__(self):
        return (f'Full Name: {self.get_full()}\nFirst Name: {self.get_first()}\n'
                f'Middle Initial: {self.get_middle()}\nLast Name: {self.get_last()}\n'
                f'DOB: {self.get_dob()}\nMajor: {self.__major}\nGPA: {self.__gpa}\n'
                f'Grade Level: {self.__level}')
