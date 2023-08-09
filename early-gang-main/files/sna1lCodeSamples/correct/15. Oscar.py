import math

def calculate_square_root(number):
    try:
        result = math.sqrt(number)
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Invalid value.")

class CustomException(Exception):
    pass

def raise_custom_exception():
    raise CustomException("Something went wrong!")

def handle_custom_exception():
    try:
        raise_custom_exception()
    except CustomException as e:
        print("Custom exception occurred:", str(e))

number = 25
calculate_square_root(number)
handle_custom_exception()
