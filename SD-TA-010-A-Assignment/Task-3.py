def isPPSN(str):
    for i in range(7):
        if str[i].isalpha():
            return False
    
    if len(str) == 8:
        if str[-1].isdigit():
            return False
    elif len(str) == 9:
        if str[-1].isdigit():
            return False
        elif str[-2].isdigit():
            return False
    else:
        return False
    
    return True

print(isPPSN('1234567E'))