#!/usr/bin/env python3

def isValidPassword(password):
    
    if len(password) <= 7:
        isLong = False
    else:
        isLong = True

    for i in password:
        if i.isnumeric():
            hasDigit = True
            break
        else:
            hasDigit = False

    for i in password:
        if i.islower():
            hasLower = True
            break
        else:
            hasLower = False

    for i in password:
        if i.isupper():
            hasUpper = True
            break
        else:
            hasUpper = False

    if hasDigit and hasUpper and hasLower and isLong:
        print('The password will work')
        return True
    elif isLong == False:
        print('The password needs to be at least 8 characters')
    else:
        print('The password did not have required properties')
        return False

def main():
#    password = 1
#    password2 = 1

#    while password != password2:
        password = input('Please enter password:')
        password = str(password)

        password2 = input('Please enter password again: ')
        password2 = str(password2)

        if password == password2:
            isValidPassword(password)
#            break
        else:
            print('The two passwords do not match, please try again')
            
    




if __name__ == '__main__':
    main()
