#validate PPS number
def is_valid_ppsn(str, emp_dict):
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
    
    for data in list(emp_dict.values()):
        if str == data[-1]:
            print('This PPS number is already in the system.')
            return False
    
    return True

#validate ID format
def is_id(str):
    if len(str) > 2 and str[slice(2)].lower() == 'id':
        return True
    return False

#validate ID exists in the system
def is_id_present(str, emp_dict):
    if str.upper() in emp_dict.keys():
        return True
    return False

#validate salary input
def is_valid_salary(str):
    if str.isdigit() and len(str) > 4 and len(str) <= 6:
        return True
    return False

#validate user input for main menu, employee list menu and employee menu
def is_valid_option(str):
    if str in ['1','2','3','4']:
        return True
    return False

#validate user input for 'y' for confirm and 'n' for cancel
def is_valid_answer(str):
    if str.lower() in ['y', 'n']:
        return True
    return False

#validate input length in add new employe menu
def is_valid_length(str):
    if len(str) < 21:
        return True
    return False