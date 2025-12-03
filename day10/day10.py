# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return # Returns 'None'
#     formated_f = f_name.title()
#     formated_l = l_name.title()
#     return f"{formated_f} {formated_l}"

# def fn1(text):
#     return text + text
# def fn2(text):
#     return text.title()
# print(fn2(fn1('hello')))

# def is_leap_year(year):
#     check = False
#     if year % 4 == 0:
#         if year % 100 != 0:
#             check = True
#         elif year % 400 == 0:
#             check = True
#     return check

# def format_name(f_name, l_name):
#     """
#     Take the first and the last name and format it
#     to return the title case version of the full name
#     """ # Doc strings for notes of functions - Will show when cursor is held above the function when calling it.
#     if f_name == "" or l_name == "":
#         return "Error - no value given"
#     formated_f = f_name.title()
#     formated_l = l_name.title()
#     return f"{formated_f} {formated_l}"

# print(format_name(input("What is your first name?\n"), input("What is your last name?\n")))



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}


def calculator():
    should_accumulate = True
    num1 = int(input("Enter your first number: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        op = input("Enter an operation: ")

        num2 = int(input("Enter your second number: "))

        result = operations[op](num1, num2)

        print(f"Your result is: {result}")

        check = input(f"Enter 'y' if you want to continue with your previous result ({result}) or 'n' if you want to start a new calculation:\n").lower()
        if check == 'y':
            num1 = result
        elif check == 'n':
            should_accumulate = False
            print("\n"*20)
            calculator()

calculator()