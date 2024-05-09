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
    print('''
            Press 1 to get a voucher
                        OR
            any other key to continue if you already have a voucher
         ''')
    option = input('>> ')
    if str(option) == '1':
        serial,pin = get_voucher()
        update_vouchers(serial,pin)

    print('VOUCHER VALIDATION')
    tries = 0
    while tries < 3:
        serial = input('Serial Number: ')
        pin = input('Pin: ')
        state = validate_voucher(pin,serial)
        if state == True:
            selected = menu()
            break
        else: 
            print('Invalid voucher')
            tries += 1

    if tries <3:        
        # 3. School placement
        placed,school = school_placement(aggregate,selected)
        if placed == True:
            print(f'Congrats {name}')
            print(f'You have been placed in {school}')
        else:
            print(f"It's quiet unfortunate, {name}")
            print('You were not placed in any school due to your aggregate.')

main()
input('Press any key to exit ......')
