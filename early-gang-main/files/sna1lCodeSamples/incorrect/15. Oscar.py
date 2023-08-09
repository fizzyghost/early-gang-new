import exceptionss as exceptions
import mathh as math

def calculate_square_root(number):
    try:
        result = math.squrt(number)
        return result
    except exceptions.ZerroDivisionError:
        print("Cannot divide by zero.")
    except exceptions.ValuError:
        print("Invalid value.")

def raise_custom_exception():
    raise exceptions.CustomeException("Something went wrong!")

def handle_custom_exception():
    try:
        raise_custom_exception()
    except exceptions.CustomeException as e:
        print("Custom exception occurred:", str(e))

number = 25
calculate_square_root(number)
handle_custom_exception()
