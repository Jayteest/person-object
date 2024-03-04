# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: September 25, 2023

# Description:
# This file contains the Employee class, a subclass of the Person class.
# This class extends the Person class to include data attributes for
# department and salary (annual).
# It contains methods for setting and getting each of these attributes.

# Logic:
# import person
# init:
#   set first, middle, last, dob, dept, salary to passed arguments,
#   or None if no argument passed
#   call init from Person
#   set dept and salary
# sets for dept and salary:
#   accept argument value, set attribute to argument value
# gets for dept and salary:
#   return attribute
# repr: return formatted string


# import Person class to use as superclass
import person

# declare Employee class
class Employee(person.Person):
    # initializer method to initialize object's data attributes
    def __init__(self, first=None, middle=None, last=None, dob=None, dept=None, salary=None):
        # call constructor from Person class to inherit attributes
        person.Person.__init__(self, first, middle, last, dob)
        # set additional attributes to corresponding passed arguments
        self.__dept = dept
        self.__salary = salary

    # set method to allow user to set dept
    def set_dept(self, dept):
        self.__dept = dept

    # set method to allow user to set salary
    def set_salary(self, salary):
        self.__salary = salary

    # get method to return dept
    def get_dept(self):
        return self.__dept

    # get method to return salary
    def get_salary(self):
        return self.__salary

    # repr method to return human readable representation of object
    def __repr__(self):
        return (f'Full Name: {self.get_full()}\nFirst Name: {self.get_first()}\n'
                f'Middle Initial: {self.get_middle()}\nLast Name: {self.get_last()}\n'
                f'DOB: {self.get_dob()}\nDepartment: {self.__dept}\nSalary: ${self.__salary}'
                f'/ year')
