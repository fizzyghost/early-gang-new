import math
import numpy
import requests

def check_greater_than(a, b):
    if a > b:
        return True
    else:
        return False

def calculate_average(numbers):
    avg = numpy.average(numbers)
    return avg

def get_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def multiply_numbers(a, b):
    result = a * b
    return result

x = 10
y = 5
data_url = "https://api.example.com/data"
numbers = [1, 2, 3, 4, 5]

greater_than_result = check_greater_than(x, y)
average = calculate_average(numbers)
data = get_data(data_url)
product = multiply_numbers(x, y)

print("Greater than result:", greater_than_result)
print("Average:", average)
print("Data:", data)
print("Product:", product)
