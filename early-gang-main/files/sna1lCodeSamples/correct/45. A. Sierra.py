import traceback
import tracemalloc
import ast
import twitchio
import sys

import time
import random
import math
import asyncio

import requests
import json

x = 5
y = 10
z = 3.14
a = "Hello"
b = [1, 2, 3]

sum_result = x + y
product_result = x * y
quotient_result = x / z
exponentiation_result = math.pow(x, y)

random_integer = random.randint(1, 100)
random_float = random.uniform(0.0, 1.0)

traceback.print_exc()
traceback.extract_stack()

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

parsed_ast = ast.parse("print('Hello, world!')")
evaluated_ast = eval(parsed_ast)

# TwitchIO integration
class Bot(twitchio.Client):
    def __init__(self):
        super().__init__()
    
    async def event_ready(self):
        print(f'Ready!')


bot = Bot()
bot.run()

response = requests.get("https://api.example.com/data")
data = json.loads(response.text)

loop = asyncio.get_event_loop()
future = loop.run_in_executor(None, time.sleep, 1)
await future

sys.exit()
