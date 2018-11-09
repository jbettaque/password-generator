import string
import random
import re


def request_len():

    """
    Prompts the user for the password length and returns the length as an int or -1 if input was invalid
    :rtype: int
    """

    length = input("Type in your desired password length:\n")

    # if the input cannot be converted to an integer, it therefore is not a number and invalid
    try:
        length = int(length)
        return length
    except:
        print("Invalid input for password length.")
        return -1


def request_methods():

    """
    Prompts the user for password strength and returns list containing the pool of chars to generate from
    (string list). Will repromt if input is invalid.
    :rtype: list
    """

    # initializing spaces (methods)
    chars = "abcdefghijklmnopqrstuvwxyzäöü"
    chars_upper = chars.upper()
    numbers = "1234567890"
    others = "!§$%&/()=?*'+#-.,;:[]{}_^"

    strength = str(input("Choose your desired password strength. \n"
                         "(1) lower case chars \n"
                         "(2) UPPER CASE CHARS \n"
                         "(3) numbers 1234567890 \n"
                         "(4) specials !§$%&/()=?*'+#-.,;:[]{}_^ \n"
                         "(5) ALL (overwrites)\n"
                         "(6) ALL without specials (overwrites)\n"
                         "Format: '1,2,3' for lower and upper case chars and numbers \n"))

    # if "," or "1" or "2" or "3" or "4" not in strength or strength[0] not in ["1", "2", "3", "4"]:
    #     print("Invalid input for strength.")
    #     quit()
    # Just for demonstration purposes, way worse that regex and also not complete

    # check if input is correct with regex
    # best site ever: https://regex101.com/
    if not re.match(r'([123456])|([123456],)+', strength):
        print("Invalid input for password strength.")
        request_methods()
    else:
        strength = strength.split(",")
        methods = []

        # replace input with actual methods
        for method_number in strength:
            if method_number == "1":
                methods.append(chars)
            if method_number == "2":
                methods.append(chars_upper)
            if method_number == "3":
                methods.append(numbers)
            if method_number == "4":
                methods.append(others)
            if method_number == "5":
                methods = [chars, chars_upper, numbers, others]
            if method_number == "6":
                methods = [chars, chars_upper, numbers]
        return methods


def main():
    """
    Main Function
    """
    print("-----------------------")
    print("PASSWORD GENERATOR v1.0")
    print("-----------------------")
    length = 0

    # request_len returns -1 if input was invalid. Requests Length until valid value was returned
    while(length <= 0):
        length = request_len()

    methods = request_methods()

    password = ""
    # for "length" chars
    # choose (pseudo) random method
    # generate char with chosen method and add it to password
    for i in range(length):
        method = random.choice(methods)
        random_char = random.choice(method)
        password = password + random_char

    print("Length: " + str(length))
    print("Your generated password:")
    print(password)


if __name__ == '__main__':
    main()
