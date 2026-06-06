import os, json, time
import payslip_calculations, input_validations

BOLD = '\033[1m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'

MAIN_MENU_HEADER = 'Payroll System Main Menu'
EMPLOYEES_HEADER = 'Employees List'
EMPLOYEE_MENU_HEADER = 'Employee Menu'
ADD_NEW_HEADER = 'Add New Employee to the Payroll System'
HELP_MENU_HEADER = 'Payroll System Help Menu'
EXIT_HEADER = 'Logged out'

#get employee list from employees.json
employees = json.load(open('employees.json', 'r'))


#save the employee updates to employees.json
def save_employees():
    with open('employees.json', 'w') as f:
        return json.dump(employees, f)


def screen_header(header):
    clear_screen()
    os.system('') # enables ANSI on Windows 10+
    print()
    print('*'*100)
    print(f'\n{'*** ' + header + ' ***':^100}\n')


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
    screen_header(MAIN_MENU_HEADER)
    
    print(f'{BOLD}(1){RESET} Display employee list')
    print(f'{BOLD}(2){RESET} Add a new employee')
    print(f'{BOLD}(3){RESET} Help')
    print(f'{BOLD}(4){RESET} Exit')
    
    user_input = input(f'\nSelect an option {BOLD}(1,2,3 or 4){RESET} to continue...\n')

    while input_validations.isValidOption(user_input) == False:
        print('Invalid input. Press 1, 2, 3 or 4...\n')
        user_input = input()

    if user_input == '1':
        display_employees()
    elif user_input == '2':
        add_new_employee()
    elif user_input == '3':
        display_help()
    elif user_input == '4':
        payroll_logout()


#display employee list
def display_employees():
    screen_header(MAIN_MENU_HEADER)
    print('Loading employees list...')
    time.sleep(1)
    
    employee_list = list(employees)
    list_length = len(employee_list)
    start = 0
    page_size = 3
    employee_menu = False
    main_menu = False
    
    while True:
        screen_header(EMPLOYEES_HEADER)
        
        for employee in employee_list[start: start + page_size]:
            last_start = start - page_size
            print(f'ID: {employee:<5} Name: {employees[employee][0]}')
            index = employee_list.index(employee)
        if index == list_length - 1:
            start = last_start
        
        print()
        print(f'{BOLD}(1){RESET} Next page')
        print(f'{BOLD}(2){RESET} Previous page')
        print(f'{BOLD}(3){RESET} View Employee Menu')
        print(f'{BOLD}(4){RESET} Back to Main Menu')
        
        user_input = input(f'\nSelect an option {BOLD}(1,2,3 or 4){RESET} to continue...\n')
        
        while input_validations.isValidOption(user_input) == False:
            user_input = input('Invalid input. Press 1, 2, 3 or 4...\n')
        
        if user_input == '1':
            start += page_size
        elif user_input == '2':
            start -= page_size
            if start < 0:
                start = 0
        elif user_input == '3':
            employee_menu = True
            break
        elif user_input == '4':
            main_menu = True
            break

    if employee_menu == True:
        display_employee_menu()
    elif main_menu == True:
        display_main_menu()    


#display employee operations menu
def display_employee_menu():
    screen_header(EMPLOYEE_MENU_HEADER)
    
    user_input = input(f'\nEnter employee ID (e.g. {BOLD}ID1{RESET}) to view a profile or press {BOLD}(c){RESET} to cancel\n')

    while input_validations.isID(user_input) == False and user_input.lower() != 'c':
        user_input = input(f'Not a valid ID. Try again or press {BOLD}(c){RESET} to cancel.\n')
    
    while input_validations.isIDpresent(user_input, employees) == False and user_input.lower() != 'c':
        user_input = input(f'This ID does not exist. Try again or press {BOLD}(c){RESET} to cancel.\n')

    if user_input.lower() == 'c':
        display_employees()
    else:
        id = user_input.upper()
        display_profile(id)
        

#display employee profile
def display_profile(id):
    print()
    print(f'{'ID':<6}{'Name':<21}{'Department':<21}{'Role':<21}{'Salary':<21}{'PPSN':<21}')
    print('-' * 100)
    print(f'{id:<6}', end='')
    for data in employees[id]:
        print(f'{data:<21}', end='')
    print('\n')
    print(f'{BOLD}(1){RESET} Edit payroll details')
    print(f'{BOLD}(2){RESET} Display Payslip')
    print(f'{BOLD}(3){RESET} Remove from payroll')
    print(f'{BOLD}(4){RESET} Back to Employee List')

    user_input = input((f'\nSelect an option {BOLD}(1,2,3 or 4){RESET} to continue...\n'))
        
    while input_validations.isValidOption(user_input) == False:
        user_input = input('Invalid input. Press 1, 2, 3 or 4...\n')

    if user_input == '1':
        edit_details(id)
    elif user_input == '2':
        display_payslip(id)
    elif user_input == '3':
        remove_employee(id)
    elif user_input == '4':
        display_employees()   

#update payroll details
def edit_details(id):
    screen_header(EMPLOYEE_MENU_HEADER)
    
    print(f'Editing details for {BOLD}{employees[id][0]}{RESET}...\n')
    print('Only salary details can be updated. Contact HR department to update other details.')
    user_input = input(f'Enter a new salary amount below or press {BOLD}(c){RESET} to cancel...\n')

    while user_input.lower() != 'c' and input_validations.isValidSalary(user_input) == False:
        user_input = input(f'Invalid input. Press {BOLD}(c){RESET} to cancel or enter a valid salary amount. Salary can only be numeric and 5 or 6 digits\n')
   
    if user_input.lower() == 'c':
        print('\nProcess cancelled...\n')
        time.sleep(1)
        display_profile(id)
    else:
        employees[id][3] = user_input
        save_employees()
        print('\nEmployee info updated...\n')
        time.sleep(1)
        display_profile(id)


#generate a payslip for an employee
def display_payslip(id):
    screen_header(EMPLOYEE_MENU_HEADER)
    
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
    print('*' * 100)
    print(f'{BOLD}{'Financial IT Solutions Ltd. Payslip':^100}{RESET}')
    print('*' * 100)
    print(f'{'Employee Name:':<17}{name:<31}{'Frequency:':<14}{frequency}')
    print(f'{'Employee Number:':<17}{number:<31}{'Pay Period:':<14}{period}')
    print(f'{'PPS Number:':<17}{ppsn:<31}{'Payment Date:':<14}{date}')
    print('*' * 100)
    print(f'{BOLD}{'PAYMENT DETAILS':^50}{'DEDUCTION DETAILS':^50}{RESET}')
    print('*' * 100)
    print(f'{'Salary:':<12}{'€' + str(gross_pay):<36}{'PAYE:':<12}{'€' + str(paye):<48}')
    print(f'{'':48}{'PRSI:':<12}{'€' + str(prsi)}')
    print(f'{'':48}{'USC:':<12}{'€' + str(usc)}')
    print('*' * 100)
    print(f'{BOLD}{'TAX/PRSI DETAILS':^50}{'SUMMARY OF PAY':^50}{RESET}')
    print('*' * 100)
    print(f'{'PRSI Class:':<12}{prsi_class:<36}{'Gross Pay:':<18}{'€' + str(gross_pay)}')
    print(f'{'Tax Credit:':<12}{'€' + str(tax_credit):<36}{'Total Deductions:':<18}{'€' + str(deductions)}')
    print(f'{'':48}{'Net Pay:':<18}{'€' + str(net_pay)}')
    print(f'{'':48}{'Payment Method:':<18}{'Bank transfer'}')
    print('*' * 100)

    user_input = input('\nPress any key to go back...\n')
    if user_input:
        screen_header(EMPLOYEE_MENU_HEADER)
        display_profile(id)


#remove employee from employee list
def remove_employee(id):
    screen_header(EMPLOYEE_MENU_HEADER)
    user_input = input('\nAre you sure you want to remove this employee from the system? (y/n).\nThis change cannot be undone. All details will be deleted.\n')
    
    while input_validations.isValidAnswer(user_input) == False:
        user_input = input(f'\nInvalid input. Please only press {BOLD}(y){RESET} for "Yes" and {BOLD}(n){RESET} for "No".\n')

    if user_input.lower() == 'y':
        print('\nProcessing...')
        time.sleep(1)
        employees.pop(id)
        save_employees()
        screen_header(EMPLOYEE_MENU_HEADER)
        print('\nEmployee removed from the system...')
        time.sleep(1)
        display_employees()
    elif user_input.lower() == 'n':
        screen_header(EMPLOYEE_MENU_HEADER)
        print('\nProcess cancelled...')
        time.sleep(1)
        display_profile(id)


#add new employee to the employee list
def add_new_employee():
    while True:
        screen_header(ADD_NEW_HEADER)
        name = input('Enter full name: ')
        while input_validations.isValidLength(name) == False:
            name = input('Name is too long. Enter 20 characters or less: ')
        department = input('Enter department: ')
        while input_validations.isValidLength(department) == False:
            department = input('Department is too long. Enter 20 characters or less: ')
        role = input('Enter role: ')
        while input_validations.isValidLength(role) == False:
            role = input('Role is too long. Enter 20 characters or less: ')
        salary = input('Enter salary: ')
        while input_validations.isValidLength(salary) == False:
            salary = input('Role is too long. Enter 20 characters or less: ')
        ppsn = input('Enter PPSN: ').upper()
        while input_validations.isValidPPSN(ppsn, employees) == False:
            ppsn = input('Enter a valid PPSN: ').upper()

        employees[generate_id()] = [name, department, role, salary, ppsn]
        print('\nProcessing...')
        time.sleep(1)
        save_employees()
        user_input = input('\nEmployee added to the payroll system.\nDo you want to add another employee to the system? (y/n)\n')
        while input_validations.isValidAnswer(user_input) == False:
            user_input(f'\nInvalid input. Please only press {BOLD}(y){RESET} for "Yes" and {BOLD}(n){RESET} for "No".\n')
        
        if user_input.lower() == 'y':
            continue
        elif user_input.lower() == 'n':
            break
        
    time.sleep(1)
    display_main_menu()
      

#help menu for the payroll system
def display_help():
    screen_header(HELP_MENU_HEADER)
    print('help menu')

    user_input = input('Press any key to go back...\n')
    if user_input:
        display_main_menu()


#close the program
def payroll_logout():
    screen_header(EXIT_HEADER)



#program starts
display_main_menu()
