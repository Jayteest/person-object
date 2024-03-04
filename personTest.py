# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: September 13, 2023

# Description:
# This program prompts the user to enter a person's information,
# including first name, middle initial, last name, and date of birth.
# It allows the user to enter information for as many people as they
# need. Once done, the program will display the full name and DOB for
# each person entered.

# Logic:
# import person
# main:
#   entry list = get entries function
#   display output header
#   call function to display entries

# get entries:
#   initialize entry list
#   create Person object
#   prompt for first name, middle initial, last name
#   call method to set attribute after each
#   while loop for input validation:
#       prompt for birth month/day/year
#       try:
#           set dob method
#           if dob > today:
#               display error, next iteration to try again
#           else: date is good, break from loop
#       except: display error, next iteration to try again
#   append Person object to entry list
#   ask user if they would like to enter another
#   if yes: reiterate function, if no: return entry list and end function

# display entries:
#   for item in entry list:
#       call get first name method and display
#       call get middle initial method and display
#       call get last name method and display
#       call get full name method and display
#       call get dob method and display       

# import person.py to use Person class, and datetime for working with DOB
import person
import datetime

# create main function to begin program execution
def main():
    # call function to get entries and assign list to variable
    entry_list = get_entries()
    
    # display results header
    print(f'\n_____Entries_____\n')
    
    # call function to display list of entries
    display_entries(entry_list)    

# function to prompt user to enter information for person
# and sets Person object to entered data attributes
# will allow multiple person entries until user specifies they are done
def get_entries():
    # initialize empty list for entries
    entries = []
    # initialize sentinel to control while loop
    keep_going = 'y'

    # start sentinel-controlled while loop to get entries until done
    while keep_going.lower() == 'y':
        # create a Person object
        entry = person.Person()

        # prompt user to enter first name
        first = str(input(f'Please enter the first name: '))
        # call set method to set first name attribute to user input
        entry.set_first(first)

        # prompt user to enter middle initial
        middle = str(input(f'Please enter the middle initial: '))
        # call set method to set middle initial attribute to user input
        entry.set_middle(middle)

        # prompt user to enter last name
        last = str(input(f'Please enter the last name: '))
        # call set method to set last name attribute to user input
        entry.set_last(last)

        # start while loop to validate DOB input
        while True:
            # try to prompt user for DOB info and create DOB attribute
            try:
                # prompt user to enter birth month
                month = int(input(f'Please enter the birth month (1 - 12): '))
                # prompt user to enter day of month
                day = int(input(f'Please enter the day of the month: '))
                # prompt user to enter birth year
                year = int(input(f'Please enter the birth year: '))
                # call set_dob method to set DOB data attribute
                entry.set_dob(month, day, year)

                # check whether entered DOB is in the future. If it is...
                if entry.get_dob() > datetime.date.today():\
                    # display error message
                    print(f'Date of birth cannot be in the future. Please try again.')
                    # continue to next loop iteration to try again
                    continue

                # if it is not in the future...
                else:
                    # data is valid, break from loop
                    break
            # if exception is raised...
            except:
                # display error message
                print(f'Invalid date entered. Please try again.')
                # continue to next loop iteration to try again
                continue

        # append Person object to entry list  
        entries.append(entry)

        # ask user if they would like to enter another person
        # if yes, next iteration begins for next Person object
        keep_going = input(f'Would you like to enter another? (y/n): ')

    # return entry list to be used by main function
    return entries

# function to display information for each person entered
def display_entries(entries):
    # start for loop to iterate through each Person object in entry list
    for item in entries:
        # call method to get first name and display
        print(f'First Name: {item.get_first()}')
        # call method to get middle initial and displaay
        print(f'Middle Initial: {item.get_middle()}')
        # call method to get last name and display
        print(f'Last Name: {item.get_last()}')
        # call method to get full name string and display
        print(f'Full Name: {item.get_full()}')
        # call method to get DOB and display
        print(f'DOB: {item.get_dob()}\n')

# call main to execute program      
if __name__ == '__main__':
    main()
