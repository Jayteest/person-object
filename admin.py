# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: September 25, 2023

# Description:
# This file contains the Admin class, a subclass of the Employee class.
# This class extends the Employee class to include a data attribute for
# direct supervisor. It also overrides the Employee class' salary attribute
# for an hourly rate, instead of annual salary.
# It contains methods for setting and getting each of these attributes.

# Logic:
# import employee
# init:
#   set first, middle, last, dob, dept, sup, salary to passed arguments,
#   or None if no argument passed
#   call init from Employee
#   set sup
# set for sup:
#   accept argument value, set attribute to argument value
# get for sup:
#   return attribute
# repr: return formatted string


# import Employee class to use as superclass
import employee

# declare Admin class
class Admin(employee.Employee):
    # initializer method to initialize object's data attributes
    def __init__(self, first=None, middle=None, last=None, dob=None, dept=None, sup=None, salary=None):
        # call constructor from Employee class to inherit attributes
        employee.Employee.__init__(self, first, middle, last, dob, dept, salary)
        # set additional attribute to corresponding passed argument
        self.__sup = sup

    # set method to allow user to set supervisor
    def set_sup(self, sup):
        self.__sup = sup

    # get method to return supervisor
    def get_sup(self):
        return self.__sup

    # repr method to return human readable representation of object
    def __repr__(self):
        return (f'Full Name: {self.get_full()}\nFirst Name: {self.get_first()}\n'
                f'Middle Initial: {self.get_middle()}\nLast Name: {self.get_last()}\n'
                f'DOB: {self.get_dob()}\nDepartment: {self.get_dept()}\nSupervisor: '
                f'{self.__sup}\nSalary: ${self.get_salary()} / hour')
                
    
