from random import choice
import string

def get_voucher():
    #Generating pin
    x = range(100000000)
    pin = choice(x)
    
    #Generating serial number
    characters = string.ascii_letters + string.digits  # Letters and numbers
    serial_number = ''.join(choice(characters) for _ in range(10))
    print(f'''
    \t\t-----VOUCHER DETAILS-----
    \t\tSERIAL NUMBER: {serial_number}
    \t\tPIN: {pin}

    # # # # # # # # # # # # # # # # # # # # #  #
    #                                          #
    #    Please note down your serial number   #
    #    and pin as you will use them for      #
    #    school selection                      #
    #                                          #
    # # # # # # # # # # # # # # # # # # # # #  #
    ''')
    return [serial_number,pin]

import csv
# Define a function to read the CSV file and filter schools
def filter_schools(csv_file, option, region=None, gender=None, category=None):
    filtered_schools, codes = [],[]

    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if option == 1:
                if row['Region'] == region:
                    filtered_schools.append(row['School Name'])
                    codes.append(row['Code'])
            elif option == 2:
                if row['Gender'] == gender:
                    filtered_schools.append(row['School Name'])
                    codes.append(row['Code'])
            elif option == 3:
                if row['Category'] == category:
                    filtered_schools.append(row['School Name'])
                    codes.append(row['Code'])
            elif option == 4:
                if row['Region'] == region and row['Gender'] == gender and row['Category'] == category:
                    filtered_schools.append(row['School Name'])
                    codes.append(row['Code'])
            filtered = [filtered_schools,codes]
    return filtered

def search_schools():
    while True:
        Schools = []
        print('''
        Search by:
        [1] Region
        [2] Gender
        [3] Category
        [4] All
        ''')
        choice = int(input())
        if choice == 1:
            region = input("Region: ").title()
            Schools = filter_schools("schools.csv", int(choice), region=region)
        elif choice == 2:
            gender = input("Gender: ").title()
            Schools = filter_schools("schools.csv", int(choice), gender=gender)
        elif choice == 3:
            category = input("Category: ").title()
            Schools = filter_schools("schools.csv", int(choice), category=category)
        elif choice == 4:
            region = input("Region: ").title()
            gender = input("Gender: ").title()
            category = input("Category: ").title()
            Schools = filter_schools("schools.csv", int(choice), region=region, gender=gender, category=category)
        print("\n")
        schools = Schools[0]
        codes = Schools[1]
        if len(schools) > 0:
            print("SCHOOL","SCHOOL CODE",sep = "\t\t\t\t\t\t\t")
            for i in range(len(schools)):
                print(f"{schools[i]:<60}",codes[i])
            break
        else:
            print('No school matching search')

# Get candidate information
def personal_info():
    name = input("Full name: ").title()
    school = input("School: ").title()
    year = int(input("Year of Exam: "))
    index = input('Index number: ')
    return [name,year,school,index]

# Take BECE results input
def BECE_results(name,year,school):
    
    # The subjects list contains two sub-lists, the first is for core subjects and the second is for electives
    subjects = [['ENGLISH LANGUAGE', 'SOCIAL STUDIES', 'INTEGRATED SCIENCE', 'MATHS'],['ICT', 'FRENCH', 'GA','TWI','PRE-TECH','HOME ECONS']]

    # Get details of candidate's electives
    def get_electives():
        electives = []
        n = 1
        print("ELECTIVES")
        for e in subjects[1]:
            print(f"{n}.",e, sep=" ")
            n += 1

        select = input("Select the electives you wrote (Example: 1,2,4,5) ")
        choice = [1,2,3,4,5,6]
        select = select.replace(',','') # Stripping off commas

        # Store selected electives in subject[1]
        indices = []
        for i in select:
            a = int(i)-1
            indices.append(a)
        for e in indices:
            electives.append(subjects[1][e])
        subjects[1] = electives
        
    # Get candidate's BECE results
    def results():
        grades = []
        print("\n\nSUBJECT\t\t\t       GRADE")
        for e in subjects[0]:
            print(f"{e:<20}", end = "\t\t")
            grades.append(int(input()))
        for e in subjects[1]:
            print(f"{e:<20}", end = "\t\t")
            grades.append(int(input()))
        return grades
    
    print(f'''
        Name: {name}
        Examination Year: {year}
        School: {school}
         ''')

    get_electives() # Calling the function to take details of electives
    grades = results() # Calling the function to take details of BECE results 
    return grades

def get_aggregate(grades):
    aggregate = 0
    for e in grades[:4]: # Iterating through grades for core subjects
        aggregate += e

    electives = grades[4:]
    
    # Arranging grades in ascending order
    i = 1
    while i < len(electives):
        if electives[i-1] > electives[i]:
            electives[i],electives[i-1] = electives[i-1], electives[i] # Swapping
        i += 1
    # print(electives)
    aggregate = aggregate + electives[0] + electives[1]
    return aggregate

def check_code(code,csv_file):
    count = 0
    cat = 'X' # This would be returned when the code matches no school
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Code'] == code:
                cat = row['Category']
                count += 1
    return [bool(count),cat]

# This function returns the names of the schools selected by using the code as key word for the search
def get_school(code):
    with open('schools.csv', newline = '') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Code'] == code:
                school = row['School Name']
    return school
    
def school_selection():
    def inputs():
        selected = []
        school = []
        School_names = []
        # Accepting inputs
        print("Enter school code, course(separated by commas)")
        print('\t CODE COURSE')
        for i in range(1,5):
            while True:
                print(f'Choice {i}: ', end = ' ')
                input_str = input()

                # Splitting the input string by commas and assigning it to a list variable
                school = input_str.split(',')
                residence = input("Residential status (Enter D or B): ")
                code_valid,cat = check_code(school[0],'schools.csv')
                if code_valid == False:
                    print('No school associated with this code')
                else:
                    school.append(cat)
                    School_names.append(get_school(school[0]))
                    break
            school.append(residence) # School = [Code, Course, Category, Residence]
            selected.append(school)
            print(' ')
        return selected
    selected = inputs()
    return selected

def school_placement(aggregate,selected):
    '''
    # 06 - 15 Cat A
    # 16 - 25 Cat B
    # 26 - 35 Cat C
    # 36+ No School
    '''

    Codes = []
    for i in selected: # Iterating through each sub list in selected
        if aggregate <36:
            if aggregate <= 15:
                for x in i: # Iterating through each element in each sub list
                    if x == 'A':
                        code = i[0]
                        Codes.append(code) # This ensures that all Cat A schools are stored
            elif aggregate <= 25:
                for x in i:
                    if x == 'B':
                        code = i[0]
                        Codes.append(code) # This ensures that all Cat B schools are stored
            elif aggregate <= 35:
                for x in i:
                    if x == 'C':
                        code = i[0]
                        Codes.append(code) # This ensures that all Cat C schools are stored
            school = get_school(Codes[0])
            return [True,school]
        else:
            return [False,'X']

# This function handles searching for schools and calls the school selection function
def menu():
        input('Press any key to proceed to school selection')
        print('SCHOOL SELECTION PORTAL')
        option = input('Press 1 to search school(s) or any other key to proceed with school selection')
        try:
            if int(option) == 1:
                while True:
                    print('''
                    What would you like to do?
                    [1] Perform another search
                    [2] Continue to school selection
                    ''')
                    option = int(input('>> '))
                    try:
                        if option == 1:
                            continue
                        elif option == 2:
                            break
                        else:
                            print('Enter 1 or 2')
                    except ValueError:
                        print('Enter 1 or 2')
                selected = school_selection()
            else:
                selected = school_selection()
        except ValueError:
            selected = school_selection()
        return selected
