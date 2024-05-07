'''
Divided into 3 sessions
[1] Personal information and BECE results input
At this part, candidates enter their name, index and school details
They also enter their BECE results and the aggregate is calculated

[2] Voucher generation and school selection
Get voucher before proceeding to school selection
At school selection, candidates should enter voucher details
Voucher details validation system [3 tries only]
When voucher is valid proceed to school selection [option to search for schools]
At school selection, students can select 4 schools, 4 courses and 4 statuses (B or D)


[3] School placement
Based on the aggregate, the student is placed. 
'''

from sp_functions import * 

def main():
    # 1. Getting Personal info and BECE results
    name,year,school,index = personal_info()
    grades = BECE_results(name,year,school)
    aggregate = get_aggregate(grades)

    # 2. Voucher generation, validation and school selection
    serial_number,pin = get_voucher()
    def menu():
        input('Press any key to proceed to school selection')
        print('SCHOOL SELECTION PORTAL')
        option = int(input('Press 1 to search school(s) or any other key to proceed with school selection'))
        try:
            if option == 1:
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
                selected = school_selection()
                    except ValueError:
                        print('Enter 1 or 2')
            else:
                selected = school_selection()    
        except ValueError:
            selected = school_selection()
        return selected
        
    # 3. School placement
