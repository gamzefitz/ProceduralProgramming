import os, json, time
import payslip_calculations

BOLD      = '\033[1m'
UNDERLINE = '\033[4m'
RESET     = '\033[0m'

#get employee list from employees.json
employees = json.load(open('employees.json', 'r'))


#save the employee updates to employees.json
def save_employees():
    with open('employees.json', 'w') as f:
        return json.dump(employees, f)


#clear the terminal output
def clear_screen():
    if os.name == 'nt':
        return os.system('cls')
    else:
        return os.system('clear')


#generate id for a new employee
def generate_id():
    last_id = list(employees)[-1]
    digits = int(last_id[slice(2,len(last_id))])
    digits += 1
    new_id = 'ID' + str(digits)
    return new_id


#main menu
def display_main_menu():
    clear_screen()
    os.system('') # enables ANSI on Windows 10+
    print()
    print('*'*50)
    print(f'\n{'***Payroll System Main Menu***':^70}\n')
    print(f'{BOLD}(1){RESET} Display employee list')
    print(f'{BOLD}(2){RESET} Add a new employee')
    print(f'{BOLD}(3){RESET} Help')
    print(f'{BOLD}(4){RESET} Exit')
    print(f'\nSelect an option {BOLD}(1,2,3 or 4){RESET} to continue...\n')

    user_input = input()
    while user_input not in ['1','2','3','4']:
        print('Invalid input. Press 1, 2, 3 or 4...\n')
        user_input = input()

    if user_input == '1':
        display_employees()
    elif user_input == '2':
        add_new_employee()
    elif user_input == '3':
        payroll_help()
    elif user_input == '4':
        payroll_logout()


#display employee list
def display_employees():
    clear_screen()
    employee_list = list(employees)
    print()
    print('*'*50)
    print(f'\n{'***Payroll System Main Menu***':^70}\n')
    print('Retrieving employee list...')
    time.sleep(1)

    list_length = len(employee_list)
    start = 0
    page_size = 3
    employee_menu = False
    main_menu = False
    
    while True:
        clear_screen()
        os.system('') # enables ANSI on Windows 10+
        print()
        print('*'*50)
        print(f'\n{'***Employees List***':^70}\n')
        for employee in employee_list[start: start + page_size]:
            last_start = start - page_size
            print(f'ID: {employee:<5} Name: {employees[employee][0]}')
            index = employee_list.index(employee)
        if index == list_length - 1:
            start = last_start
        print(f'\nEnter {BOLD}(n){RESET} for Next page, {BOLD}(p){RESET} for Previous page.\nEnter {BOLD}employee ID{RESET} to display employee details.')
        print('Enter any other key for going back to main menu...\n')
        user_input = input()
        if user_input == 'n':
            start += page_size
        elif user_input == 'p':
            start -= page_size
            if start < 0:
                start = 0
        elif len(user_input) > 2 and user_input[slice(2)] == 'id':
            id = user_input.upper()
            employee_menu = True
            break
        elif user_input:
            print('Going back to main menu...')
            time.sleep(1)
            main_menu = True
            break

    if employee_menu == True:
        display_employee_menu(id)
    elif main_menu == True:
           display_main_menu()    


#display employee operations menu
def display_employee_menu(id):
    clear_screen()
    os.system('') # enables ANSI on Windows 10+
    print()
    print('*'*50)
    print(f'\n{'***Employee Menu***':^70}\n')
    print(f'\nShowing the details for {employees[id][0]}...\n')
    print(f'{'ID':<25}{'Name':<25}{'Department':<25}{'Role':<25}{'Salary':<25}{'PPSN':<25}')
    print('-' * 150)
    print(f'{id:<25}', end='')
    for data in employees[id]:
        print(f'{data:<25}', end='')
    print('\n')
    print(f'{BOLD}(1){RESET} Edit employee details')
    print(f'{BOLD}(2){RESET} Display payslip')
    print(f'{BOLD}(3){RESET} Remove from payroll')
    print(f'{BOLD}(4){RESET} Go back to previous menu')
    print(f'\nSelect an option {BOLD}(1,2,3 or 4){RESET} to continue...\n')

    user_input = input()
    
    while user_input not in ['1','2','3','4']:
        print('Invalid input. Press 1, 2, 3 or 4...')
        user_input = input()

    if user_input == '1':
        edit_employee_details(id)
    elif user_input == '2':
        display_payslip(id)
    elif user_input == '3':
        remove_employee(id)
    elif user_input == '4':
        display_employees()


#update employee details
def edit_employee_details(id):
    clear_screen()
    os.system('') # enables ANSI on Windows 10+
    print()
    print('*'*50)
    print(f'\n{'***Employee Menu***':^70}\n')
    print(f'Editing details for {BOLD}{employees[id][0]}{RESET}...\n')
    print('Only department, role or salary info can be changed.')
    print(f'Enter {BOLD}(d){RESET} for department, {BOLD}(s){RESET} for salary or {BOLD}(r){RESET} for role.\nPress any other key to go back to main menu...\n')

    user_input = input()

    if user_input == 'd':
        employees[id][1] = input('Enter new department name: ')
    elif user_input == 'r':
        employees[id][2] = input('Enter new role name: ')
    elif user_input == 's':
        employees[id][3] = input('Enter new salary amount: ')
    else:
        display_main_menu()
    
    save_employees()
    
    user_input = input('\nEmployee info updated. Press any key to go back to main menu...\n')
    if user_input :
        display_main_menu()


#generate a payslip for an employee
def display_payslip(id):
    clear_screen()
    os.system('') # enables ANSI on Windows 10+
    
    #calculate the data to display
    company = 'Financial IT Solutions Ltd.'
    name = employees[id][0]
    number = id
    department = employees[id][1]
    frequency = 'M'
    period = payslip_calculations.calculate_pay_period()
    date = payslip_calculations.calculate_payment_date()
    ppsn = employees[id][4]
    gross_pay = payslip_calculations.calculate_monthly_gross(employees[id][3])
    deductions = payslip_calculations.calculate_monthly_deductions(employees[id][3])
    paye = payslip_calculations.calculate_monthly_paye(employees[id][3])
    prsi = payslip_calculations.calculate_monthly_prsi(employees[id][3])
    usc = payslip_calculations.calculate_monthly_usc(employees[id][3])
    net_pay = payslip_calculations.calculate_monthly_net_pay(employees[id][3])
    prsi_class = 'A1'
    tax_credit = payslip_calculations.PERSONAL_TAX_CREDIT


    #print the payslip
    print(f'Displaying payslip for {name}...\n')
    print('*' * 147)
    print(f'{'Employee Name:':<17}{name:<30}{'Company:':<14}{company:<30}{'Frequency:':<12}{frequency:<14}{'Pay Period:':<14}{period}')
    print(f'{'Employee Number:':<17}{number:<30}{'Department:':<14}{department:<30}{'PPS Number:':<12}{ppsn:<14}{'Payment Date:':<14}{date}')
    print('*' * 147)
    print(f'{BOLD}{'PAYMENT DETAILS':^50}{'DEDUCTION DETAILS':^62}{'SUMMARY OF PAY':^32}{RESET}')
    print('*' * 147)
    print(f'{'Salary:':<20}{'€' + str(gross_pay):<28}{'* '}{'PAYE:':<12}{'€' + str(paye):<48}{'* '}{'Gross Pay:':<18}')
    print(f'{'':48}{'* '}{'PRSI:':<12}{'€' + str(prsi):<48}{'* '}{'€' + str(gross_pay)}')
    print(f'{'':48}{'* '}{'USC:':<12}{'€' + str(usc):<48}{'* '}{'-' * 35}')
    print(f'{'':48}{'*'}{'':61}{'* '}{'Total Deductions:':<18}')
    print(f'{'':48}{'*'}{'':61}{'* '}{'€' + str(deductions)}')
    print(f'{'':48}{'*'}{'':61}{'* '}{'-' * 35}')
    print(f'{'':48}{'*'}{'':61}{'* '}{'Net Pay:':<18}')
    print(f'{BOLD}{'':48}{'* '}{'TAX/PRSI DETAILS':^62}{RESET}{'* '}{'€' + str(net_pay)}')
    print(f'{'':48}{'*' * 63}{'-' * 35}')
    print(f'{'':48}{'* '}{'PRSI Class:':<12}{prsi_class:<48}{'* '}{'Payment Method:':<18}')
    print(f'{'':48}{'* '}{'Tax Credit:':<12}{'€' + str(tax_credit):<48}{'* '}{'Bank transfer'}')
    print('*' * 147)

    user_input = input('\nPress any key to go back to main menu...\n')
    if user_input:
        display_main_menu()


#remove employee from employee list
def remove_employee(id):
    print('Removing employee from the system...')
    time.sleep(1)
    employees.pop(id)
    save_employees()
    
    clear_screen()
    print()
    print('*'*50)
    print(f'\n{'***Employee Menu***':^70}\n')

    user_input = input('Employee removed. Press any key to go back to main menu...\n')
    if user_input:
        display_main_menu()


#add new employee to the employee list
def add_new_employee():
    while True:
        name = input('Enter full name: ')
        department = input('Enter department: ')
        role = input('Enter role: ')
        salary = input('Enter salary: ')
        ppsn = input('Enter PPSN: ').upper()
        while isValidPPSN(ppsn) == False:
            ppsn = input('Enter a valid PPSN: ').upper()

        employees[generate_id()] = [name, department, role, salary, ppsn]
        save_employees()
        user_input = input('Employee added to the payroll system.\nPress (y) for adding another employee. Press any other key to go back to main menu\n')
        if user_input == 'y':
            continue
        elif user_input:
            break
        
    display_main_menu()
      

#help menu for the payroll system
def payroll_help():
    clear_screen()
    print('help menu')

    user_input = input('Press any key to go back to main menu...\n')
    if user_input:
        display_main_menu()


#close the program
def payroll_logout():
    print('Program closed')


#validate PPS number
def isValidPPSN(str):
    if len(str) < 8 or len(str) > 9:
        return False
    elif len(str) == 8:
        for i in range(7):
            if str[i].isalpha():
                return False
        if str[-1].isdigit():
            return False
    elif len(str) == 9:
        for i in range(7):
            if str[i].isalpha():
                return False
        if str[-1].isdigit():
            return False
        elif str[-2].isdigit():
            return False
    
    for data in list(employees.values()):
        if str in data[-1]:
            print('This PPSN is already in the system.')
            return False
    
    return True


#program starts
display_main_menu()










