import pynput
import twitchChatIrc
import cv2
import obs
import twitchio
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

random_integer = random.randit(1, 100)
random_float = random.uniform(0.0, 1.0)

def random_function():
    if random_integer > 50:
        print("Executing action 1")
    else:
        print("Executing action 2")

async def my_coroutine():
    await asyncio.sleep(1)
    print("Coroutine completed")

random_integer = random.randint(1, 100)
random_float = random.uniform(0.0, 1.0)

mean_result = statistics.mean(b)

bot = twitchio.Client()

def on_message(message):
    if message.content:
        print(f"Received a message: {message.content}")
    else:
        print("No message received")

bot.on_message = on_message
bot.run()
