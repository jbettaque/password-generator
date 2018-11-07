import string
import random
import re


def request_len():
    length = input("Type in your desired password length:\n")

    try:
        length = int(length)
        return length
    except Exception as e:
        print("Invalid input for password length.")
        return -1



def request_methods():
    chars = "abcdefghijklmnopqrstuvwxyzäöü"
    chars_upper = chars.upper()
    numbers = "1234567890"
    others = "!§$%&/()=?*'+#-.,;:[]{}_^"

    strength = str(input("Choose your desired password strength. \n"
                         "(1) lower case chars \n"
                         "(2) UPPER CASE CHARS \n"
                         "(3) numbers 1234567890 \n"
                         "(4) specials !§$%&/()=?*'+#-.,;:[]{}_^ \n"
                         "Format: '1,2,3' for lower and upper case chars and numbers \n"))

    # if "," or "1" or "2" or "3" or "4" not in strength or strength[0] not in ["1", "2", "3", "4"]:
    #     print("Invalid input for strength.")
    #     quit()

    if not re.match(r'([1234])|([1234],)+', strength):  # best site ever: https://regex101.com/
        print("Invalid input for password strength.")
        request_methods()
    else:
        strength = strength.split(",")
        methods = []
        for method_number in strength:
            if method_number == "1":
                methods.append(chars)
            if method_number == "2":
                methods.append(chars_upper)
            if method_number == "3":
                methods.append(numbers)
            if method_number == "4":
                methods.append(others)
        return methods


def main():
    print("-----------------------")
    print("PASSWORD GENERATOR v1.0")
    print("-----------------------")
    length = 0
    while(length <= 0):
        length = request_len()

    methods = request_methods()
    password = ""
    for i in range(length):

        method = random.choice(methods)
        random_char = random.choice(method)
        password = password + random_char

    print("Length: " + str(length))
    print("Your generated password:")
    print(password)


if __name__ == '__main__':
    main()
