#!/usr/bin/env python3

def isValidPassword(password):
    
    if len(password) <= 7:
        isLong = False
    else:
        #print('Password is not long enough')
        isLong = True

    for i in password:
        if i.isnumeric():
            hasDigit = True
            break
        else:
            #print('Password does not have a number')
            hasDigit = False

    for i in password:
        if i.islower():
            hasLower = True
            break
        else:
            #print('Password does not have a lower case')
            hasLower = False

    for i in password:
        if i.isupper():
            hasUpper = True
            break
        else:
            #print('Password does not have an upper case')
            hasUpper = False

    if hasDigit and hasUpper and hasLower and isLong:
        print('The password will work')
        return True

    else:
        print('The password did not have required properties')
        return False

def main():

    password = input('Please enter password:')

    password = str(password)

    password2 = input('Please enter password again: ')

    print(password2)
   
    print(password)

    if password == password2:
        isValidPassword(password)
    else:
        print('The two passwords do not match, please try again')
        return False
    




if __name__ == '__main__':
    main()
