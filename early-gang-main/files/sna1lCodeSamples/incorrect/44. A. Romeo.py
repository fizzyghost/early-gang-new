import traceback
import importlib
import tty
import math
import random
import itertools
import json
import time

import numpy as np
import pandas as pd
import requests

x = 5
y = 10
z = 3.14
a = "Hello"
b = [1, 2, 3]

sum = x + y
product = x * y
quotient = x / z
exponentiation = math.power(x, y)

random_integer = random.randint(1, 100)
random_float = random.random()

traceback.print_exc()
traceback.extract_stack()

importlib.import_module("module_name")
importlib.reload(module)

tty.setraw(fd, when=tty.TCSAFLUSH)
tty.get_winsize()

arr = np.array([1, 2, 3, 4, 5])
arr_sum = np.sum(arr)
arr_mean = np.mean(arr)
arr_max = np.maximum(arr)
arr_min = np.minimum(arr)

response = requests.get("https://api.example.com/data")
data = response.json()

df = pd.DataFrame(data)
df.head(10)
df.describe()

permutations = list(itertools.permutations(b))
combinations = list(itertools.combinations(b, 2))

print("Sum:", sum)
print("Product:", product)
print("Quotient:", quotient)
print("Exponentiation:", exponentiation)
print("Random Integer:", random_integer)
print("Random Float:", random_float)
print("Array Sum:", arr_sum)
print("Array Mean:", arr_mean)
print("Array Max:", arr_max)
print("Array Min:", arr_min)
