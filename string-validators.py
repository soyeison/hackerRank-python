def validateStringAlNum(string):
    validation = False
    for i in string:
        if i.isalnum():
            validation = True

    print(validation)

def validateAlpha(string):
    validation = False
    for i in string:
        if i.isalpha():
            validation = True

    print(validation)

def validateDigit(string):
    validation = False
    for i in string:
        if i.isdigit():
            validation = True

    print(validation)

def validateLower(string):
    validation = False
    for i in string:
        if i.islower():
            validation = True

    print(validation)

def validateUpper(string):
    validation = False
    for i in string:
        if i.isupper():
            validation = True

    print(validation)


def validateString(string):
    # Validate if string has any alphanumeric characters.
    validateStringAlNum(string)
    
    # Validate if string has any alphabetical characters
    validateAlpha(string)

    # Validate if string has any digits
    validateDigit(string)

    # Validate if string has any lowercase characters
    validateLower(string)

    # Validate if string has any lowercase characters
    validateUpper(string)

if __name__ == '__main__':
    s = input()

    validateString(s)