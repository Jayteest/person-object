# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: September 25, 2023

# Description:
# This file contains the Professional class, a subclass of the Employee class.
# This class extends the Employee class to include a data attribute for
# credential info.
# It contains methods for setting and getting each of these attributes.

# Logic:
# import employee
# init:
#   set first, middle, last, dob, salary, dept, cred to passed arguments,
#   or None if no argument passed
#   call init from Employee
#   set cred
# set for cred:
#   accept argument value, set attribute to argument value
# get for cred:
#   return attribute
# repr: return formatted string


# import Employee class to use as superclass
import employee

# declare Professional class
class Professional(employee.Employee):
    # initializer method to initialize object's data attributes
    def __init__(self, first=None, middle=None, last=None, dob=None, salary=None, dept=None, cred=None):
        # call constructor from Employee class to inherit attributes
        employee.Employee.__init__(self, first, middle, last, dob, salary, dept)
        # set additional attribute to corresponding passed argument
        self.__cred = cred

    # set method to allow user to set credential
    def set_cred(self, cred):
        self.__cred = cred

    # get method to return credential
    def get_cred(self):
        return self.__cred

    # repr method to return human readable representation of object
    def __repr__(self):
        return (f'Full Name: {self.get_full()}\nFirst Name: {self.get_first()}\n'
                f'Middle Initial: {self.get_middle()}\nLast Name: {self.get_last()}\n'
                f'DOB: {self.get_dob()}\nDepartment: {self.get_dept()}\nCredentials: '
                f'{self.__cred}\nSalary: ${self.get_salary()} / year')
