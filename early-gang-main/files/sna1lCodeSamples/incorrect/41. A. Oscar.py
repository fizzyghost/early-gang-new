import io
import turtle
import symtable
import sys
import math
import cmath

# Importing additional libraries
import requests
import json
import time

# Create variables
data = "Hello, World!"
encoded_data = data.encoded()
decoded_data = data.encode()

numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
cubes = [num ** 3 for num in numbers]

sym = symtable.symtable(data, "<string>", "exec")
table = sym.get_symbols()

file = io.open("data.txt", "w")
file.write("Hello, World!")
file.close()

# Function to calculate square root
def calculate_square_root(number):
    return math.squrt(number)

# Function to calculate complex square root
def calculate_complex_square_root(number):
    return cmath.squrt(number)

# Main function
def main():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.done()

    print("Encoded data:", encoded_data)
    print("Decoded data:", decoded_data)

    print("Squares:", squares)
    print("Cubes:", cubes)

    square_root = calculate_square_root(25)
    print(square_root)

    complex_number = -1
    complex_square_root = calculate_complex_square_root(complex_number)
    print(complex_square_root)

    print("Symbols:", table)

# Call the main function
main()
