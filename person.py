# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: September 25, 2023

# Description:
# This file contains the Person class. Each object of this class will
# have data attributes consisting of first name, middle initial, last name,
# birth month/day/year, DOB, and full name.
# It contains methods for setting and getting each of these attributes.

# Logic:
# import datetime
# class Person
# init:
#   set first name, middle initial, last name, and dob to passed
#   arguments, or None if no argument passed
# sets for first name, middle initial, last name:
#   accept argument value, set attribute to argument value
# set dob (m, d, y):
#   call datetime.date(y, m, d)
# gets for first name, middle initial,last name, and dob:
#   return attribute
# get full name:
#   concatenate '{first name} {middle initial} {last name}'
#   return full name
# repr: return formatted string


# import the datetime class for assistance with setting DOB
import datetime

# declare Person class
class Person:
    # initializer method to initialize object's data attributes
    def __init__(self, first=None, middle=None, last=None, dob=None):
        # set each attribute to corresponding passed argument
        self.__first = first
        self.__middle = middle
        self.__last = last
        self.__dob = dob

    # set method to allow user to set first name
    def set_first(self, first):
        self.__first = first

    # set method to allow user to set middle initial
    def set_middle(self, middle):
        self.__middle = middle

    # set method to allow user to set last name
    def set_last(self, last):
        self.__last = last

    # set method to allow user to set date of birth
    # user inputs month, day, and year
    def set_dob(self, month, day, year):
        # use datetime date method to generate date
        self.__dob = datetime.date(year, month, day)

    # get method to return first name
    def get_first(self):
        return self.__first

    # get method to return middle initial
    def get_middle(self):
        return self.__middle

    # get method to return last name
    def get_last(self):
        return self.__last

    # get method to return date of birth
    def get_dob(self):
        return self.__dob

    # get method to return full name
    def get_full(self):
        # concatenate first name, middle initial, and last name
        full = f'{self.__first} {self.__middle} {self.__last}'
        # return concatenated string
        return full

    # repr method to return human readable representation of object
    def __repr__(self):
        return (f'Full Name: {self.get_full()}\nFirst Name: {self.__first}\n'
                f'Middle Initial: {self.__middle}\nLast Name: {self.__last}\n'
                f'DOB: {self.__dob}')
