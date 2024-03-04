# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: September 25, 2023

# Description:
# This program gives the user a menu to select what type of person
# they would like to enter (student, instructor, admin employee,
# professional employee, or none of the above). It then allows the
# user to enter all appropriate info for that type of person.
# The user can enter as many people as they would like, then the program
# displays all entries in an easily readable format.

# Logic:
# import person, student, instructor, employee, admin, professional, datetime
# main:
#   initialize list for each person type
#   while True:
#       display menu
#       get selection
#       case 0: break
#       case 1: create student, get person info, get student info, append
#       case 2: create instructor, get person info, get instructor info, append
#       case 3: create admin, get person info, get admin info, append
#       case 4: create professional, get person info, get professional info, append
#       case 5: create person, get person info, append
#   display results

# display menu:
#   print line of dashes + 'Entry Selection' + line of dashes
#   print numbers with corresponding person type

# get selection:
#   while loop for selection input validation:
#       try:
#           prompt for int input selection
#           if 0 <= selection <= 5: input good, break
#           else: display error, continue to try again
#       except: display error, continue to try again        
#   return selection

# get person info:
#   prompt for first name, middle initial, last name
#   call method to set attribute after each
#   while loop for dob input validation:
#       prompt for birth month/day/year
#       try:
#           set dob method
#           if dob > today:
#               display error, continue to try again
#           else: date is good, break
#       except: display error, continue to try again

# get student info:
#   prompt for major
#   call method to set attribute
#   while loop for gpa input validation:
#       try:
#           prompt for float input gpa
#       except: display error, continue
#   round(gpa, 2)
#   if 0 <= gpa <= 4: set method gpa, break
#   else: display error, continue
#   while loop for level input validation:
#       prompt for input
#       level.upper()
#       if FR, SO, JR, or SR: set method level, break
#       else: display error, continue

# get instructor info:
#   while loop for degree input validation:
#       prompt for input
#       degree.upper()
#       if degree == 'PHD': degree = 'PhD', set method degree, break
#       if degree == 'MS': set method degree, break
#       else: display error, continue
#   while loop for dept input validation:
#       prompt for input
#       dept.upper()
#       if CIS, CNG, CSC: set method dept, break
#       else: display error, continue
#   while loop for salary input validation:
#       try: prompt for int input salary
#       except: display error, continue
#       if salary < 0: display error continue
#       else: set method salary, break

# get employee info:
#   same dept validation loop above
#   if selection 'admin':
#       while loop for salary input validation:
#           try: prompt for float hourly rate
#           except: display error, continue
#           round(salary, 2)
#           if salary < 0: display error, continue
#           else: set method salary, break
#       prompt for sup, set method sup
#   if selection 'professional':
#       prompt for cred, set method cred
#       same salary validation loop as for instructor above

# display results:
#   if students:
#       print header
#       for item in students: print repr
#   if instructors:
#       print header
#       for item in instructors: print repr
#   if admins:
#       print header
#       for item in admins: print repr
#   if professionals:
#       print header
#       for item in professionals: print repr
#   if people:
#       print header
#       for item in people: print repr

      

# import files for Person and all subclasses, and datetime for working with DOB
import person, student, instructor, employee, admin, professional, datetime


# create main function to begin program execution
def main():
    # initialize entry list for each type of person for storing instances
    student_list = []
    instructor_list = []
    admin_list = []
    professional_list = []
    person_list = []

    # begin while loop to accept as many entries as user would like
    while True:
        # call function to display the entry selection menu
        display_menu()
        # call function to get and store user's selection
        selection = get_selection()

        # if EXIT was selected, user is done
        if selection == 0:
            # end loop to display result
            break

        # if user selected 'student'...
        elif selection == 1:
            # create student object
            entry = student.Student()
            # call function to get general person info
            get_person_info(entry)
            # call function to get student-specific info
            get_student_info(entry)
            # append instance to student list
            student_list.append(entry)

        # if user selected 'instructor'...
        elif selection == 2:
            # create instructor object
            entry = instructor.Instructor()
            # call function to get general person info
            get_person_info(entry)
            # call function to get instructor-specific info
            get_instructor_info(entry)
            # append instance to instructor list
            instructor_list.append(entry)

        # if user selected 'admin'...
        elif selection == 3:
            # create admin object
            entry = admin.Admin()
            # call function to get general person info
            get_person_info(entry)
            # call function to get employee-specific info
            # pass selection 3 as argument
            get_employee_info(entry, selection)
            # append instance to admin list
            admin_list.append(entry)

        # if user selected 'professional'...
        elif selection == 4:
            # create professional object
            entry = professional.Professional()
            # call function to get general person info
            get_person_info(entry)
            # call function to get employee-specific info
            # pass selection 4 as argument
            get_employee_info(entry, selection)
            # append instance to professional list
            professional_list.append(entry)

        # if user selected 'none of the above'...
        elif selection == 5:
            # create person object
            entry = person.Person()
            # call function to get general person info
            get_person_info(entry)
            # append instance to person list
            person_list.append(entry)

    # call function to display results, pass each object list
    display_results(student_list, instructor_list, admin_list, \
                    professional_list, person_list)


# function to display the entry selection menu      
def display_menu():
    # initialize variable with line of dashes
    header_line = '-' * 32
    # initialize variable with header text
    header = 'Entry Selection'
    # display formatted menu header
    print(f'{header_line}\n{header: ^32}\n{header_line}')
    # display menu options
    print(f'1. Student\n2. Instructor\n3. Employee (Admin)\n'
          f'4. Employee (Professional)\n5. None of the Above\n'
          f'0. Display and Exit\n{header_line}')


# function to accept user's menu selection
def get_selection():
    # begin while loop to validate input
    while True:
        # try block to attempt to accept input
        try:
            # prompt user for selection, read user input as integer
            selection = int(input(f'Select what you would like to enter: '))
            # check if user input is between 0 - 5 (inclusive)
            if 0 <= selection <= 5:
                # if it is, input is good, exit loop
                break
            # if input integer is not between 0 - 5...
            else:
                # it is no good, display error message
                print(f'Invalid selection. Please try again.')
                # begin next loop iteration to try again
                continue
        # if any errors, input is no good
        except:
            # display error message
            print(f'Invalid selection. Please try again.')
            # begin next loop iteration to try again
            continue

    # return the user's menu selection
    return selection

        
# function to get general person info from user and set attributes
def get_person_info(entry):
    # prompt user to enter first name
    first = str(input(f'Enter the first name: '))
    # call set method to set first name attribute to user input
    entry.set_first(first)

    # prompt user to enter middle initial
    middle = str(input(f'Enter the middle initial: '))
    # call set method to set middle initial attribute to user input
    entry.set_middle(middle)

    # prompt user to enter last name
    last = str(input(f'Enter the last name: '))
    # call set method to set last name attribute to user input
    entry.set_last(last)

    # start while loop to validate DOB input
    while True:
        # try to prompt user for DOB info and set DOB attribute
        try:
            # prompt user to enter birth month
            month = int(input(f'Enter the birth month (1 - 12): '))
            # prompt user to enter day of month
            day = int(input(f'Enter the day of the month: '))
            # prompt user to enter birth year
            year = int(input(f'Enter the birth year: '))
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


# function to get student-specific info from user and set attributes
def get_student_info(entry):
    # prompt user to enter major
    major = str(input(f'Enter the major: '))
    # call set method to set major attribute to user input
    entry.set_major(major)

    # start while loop to validate GPA input
    while True:
        # try to prompt user for GPA input and set gpa attribute
        try:
            # prompt user for GPA, read as float
            gpa = float(input(f'Enter the GPA: '))
        # if exception is raised...
        except:
            # display error message
            print(f'Invalid GPA entered. Please try again.')
            # continute to next iteration to try again
            continue

        # round GPA input to 2 decimal places
        gpa = round(gpa, 2)
        # if GPA is between 0 - 4 (inclusive)...
        if 0 <= gpa <= 4:
            # it is valid, call set method to set gpa attribute
            entry.set_gpa(gpa)
            # exit while loop
            break
        # if GPA input is not between 0 - 4, it is no good
        else:
            # display error message
            print(f'Invalid GPA entered. Please try again.')
            # continute to next iteration to try again
            continue

    # start while loop to validate grade level input
    while True:
        # prompt user for grade level
        level = str(input(f'Enter the grade level (FR, SO, JR, SR): '))
        # make input upper case for checking
        level = level.upper()

        # check if input is one of the valid options
        if level == 'FR' or level == 'SO' or level == 'JR' or level == 'SR':
            # if it is, call set method to set level attribute
            entry.set_level(level)
            # exit while loop
            break
        # if it is not one of the valid options, input is no good
        else:
            # display error message
            print(f'Invalid grade level entered. Please try again.')
            # continue to next iteration to try again
            continue


# function to get instructor-specific into and set data attributes
def get_instructor_info(entry):
    # start while loop to validate degree input
    while True:
        # prompt user to input degree
        degree = str(input(f'Enter the degree (PhD, MS): '))
        # make input upper case for checking
        degree = degree.upper()
        
        # if upper case input is 'PHD'...
        if degree == 'PHD':
            # modify to 'PhD'
            degree = 'PhD'
            # call method to set degree attribute
            entry.set_degree(degree)
            # exit while loop
            break

        # if upper case input is 'MS'...
        elif degree == 'MS':
            # call method to set degree attribute
            entry.set_degree(degree)
            # exit while loop
            break

        # if user input is anything else, it is no good
        else:
            # display error message
            print(f'Invalid degree entered. Please try again.')
            # continue to next iteration to try again
            continue

    # start while loop to validate department input
    while True:
        # prompt user for department
        dept = str(input(f'Enter the department (CIS, CNG, CSC): '))
        # make input upper case for checking
        dept = dept.upper()

        # check if input is one of the 3 options
        if dept == 'CIS' or dept == 'CNG' or dept == 'CSC':
            # if it is, call method to set dept attribute
            entry.set_dept(dept)
            # exit while loop
            break

        # if user input is anything else, it is no good
        else:
            # display error message
            print(f'Invalid department entered. Please try again.')
            # continue to next iteration to try again
            continue

    # start while loop to validate salary input
    while True:
        # try to prompt user for salary info 
        try:
            # prompt user for salary, read as integer
            salary = int(input(f'Enter the annual salary: '))
        # if error occurs, it is no good
        except:
            # display error message
            print(f'Invalid salary entered. Please try again.')
            # continue to next iteration to try again
            continue

        # check if salary is negative
        if salary < 0:
            # if it is, it is no good, display error message
            print(f'Invalid salary entered. Please try again.')
            # continue to next iteration to try again
            continue
        # if salary is not negative, it is good
        # $0 is okay, because there could be a volunteer situation
        else:
            # call method to set salary attribute
            entry.set_salary(salary)
            # exit while loop
            break


# function to get employee-specific info and set data attributes
def get_employee_info(entry, selection):
    # start while loop to validate department input
    while True:
        # prompt user for department
        dept = str(input(f'Enter the department (CIS, CNG, CSC): '))
        # make input upper case for checking
        dept = dept.upper()

        # check if user input is one of the 3 options
        if dept == 'CIS' or dept == 'CNG' or dept == 'CSC':
            # if it is, call method to set dept attribute
            entry.set_dept(dept)
            # exit while loop
            break

        # if it is not, input is no good
        else:
            # display error message
            print(f'Invalid department entered. Please try again.')
            # continue to next iteration to try again
            continue

    # if user's selection was 'admin'...
    if selection == 3:
        # begin while loop to validate salary input
        while True:
            # try to get salary
            try:
                # prompt user for hourly rate, read as float
                salary = float(input(f'Enter the hourly pay rate: '))
            # if error occurs, input is no good
            except:
                # display error message
                print(f'Invalid pay rate entered. Please try again: ')
                # continue to next iteration to try again
                continue

            # round hourly rate input to 2 decimal places
            salary = round(salary, 2)

            # check if hourly rate input is negative
            # $0 is okay, because there could be a volunteer situation
            if salary < 0:
                # if it is negative, input is not valid, display error message
                print(f'Invalid pay rate entered. Please try again.')
                # continue to next iteration to try again
                continue

            # if hourly rate is not negative, input is good
            else:
                # call method to set salary attribute
                entry.set_salary(salary)
                # exit while loop
                break

        # prompt user for direct supervisor
        sup = str(input(f'Enter the name of the direct supervisor: '))
        # call method to set sup attribute
        entry.set_sup(sup)

    # if user's selection was not 'admin', then it was 'professional'
    else:
        # prompt user for credential info
        cred = str(input(f'Enter the credentials: '))
        # call method to set cred attribute
        entry.set_cred(cred)

        # start while loop to validate salary input
        while True:
            # try to get salary info
            try:
                # prompt user for salary info, read as integer
                salary = int(input(f'Enter the annual salary: '))
            # if error occurs, input is no good
            except:
                # display error message
                print(f'Invalid salary entered. Please try again.')
                # continue to next iteration to try again
                continue

            # check if salary input is negative
            if salary < 0:
                # if it is negative, it is no good, display error message
                print(f'Invalid salary entered. Please try again.')
                # continue to next iteration to try again
                continue

            # if it is not negative, input is good
            else:
                # call method to set salary attribute
                entry.set_salary(salary)
                # exit while loop
                break


# function to display results of info gathered
# parameters include entry list of each type of person input
def display_results(students, instructors, admins, professionals, people):
    # initialize variable with line of dashes
    header_line = '-' * 32

    # check if student list contains any entries
    if students:
        # if it does, display formatted output header
        print(f'\n{header_line}\nStudents\n{header_line}')
        # start for loop to iterate through each entry in list
        for item in students:
            # call repr method to display entry
            print(f'{item.__repr__()}\n')

    # check if instructor list contains any entries
    if instructors:
        # if it does, display formatted output header
        print(f'\n{header_line}\nInstructors\n{header_line}')
        # start for loop to iterate through each entry in list
        for item in instructors:
            # call repr method to display entry
            print(f'{item.__repr__()}\n')

    # check if admin list contains any entries
    if admins:
        # if it does, display formatted output header
        print(f'\n{header_line}\nAdmins\n{header_line}')
        # start for loop to iterate through each entry in list
        for item in admins:
            # call repr method to display entry
            print(f'{item.__repr__()}\n')

    # check if professional list contains any entries
    if professionals:
        # if it does, display formatted output header
        print(f'\n{header_line}\nProfessionals\n{header_line}')
        # start for loop to iterate through each entry in list
        for item in professionals:
            # call repr method to display entry
            print(f'{item.__repr__()}\n')

    # check if people list contains any entries
    if people:
        # if it does, display formatted output header
        print(f'\n{header_line}\nPeople\n{header_line}')
        # start for loop to iterate through each entry in list
        for item in people:
            # call repr method to display entry
            print(f'{item.__repr__()}\n')
        

# call main to execute program      
if __name__ == '__main__':
    main()
