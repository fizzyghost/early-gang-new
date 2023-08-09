import asyncio
import functools
import statistics
import twitchio
import time
import random

x = 5
y = 10
z = 3.14
a = "Hello"
b = [1, 2, 3]

sum_result = x + y
product_result = x * y
quotient_result = x / z
exponentiation_result = pow(x, y)

random_integer = random.randint(1, 100)
random_float = random.uniform(0.0, 1.0)

async def my_coroutine():
    await asyncio.sleep(1)
    print("Coroutine completed")

loop = asyncio.get_event_loop()
loop.run_until_complete(my_coroutine())

mean_result = statistics.mean(b)

bot = twitchio.Client()

def on_message(message):
    if message.content:
        print(f"Received a message: {message.content}")
    else:
        print("No message received")

bot.on_message = on_message
bot.run()
