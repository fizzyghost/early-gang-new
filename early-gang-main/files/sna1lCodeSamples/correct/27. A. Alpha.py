import asyncio
import signal
import string
import twitchio
from twitchio.ext import commands

signal_var = 5

@commands.command()
async def hello(ctx):
    message = "Hello, " + ctx.author.name + "!"
    await ctx.send(message)

async def main():
    bot = commands.Bot(
        irc_token="your_token",
        client_id="your_client_id",
        nick="your_nickname",
        prefix="!",
        initial_channels=["channel1", "channel2"]
    )

    @bot.event
    async def event_ready():
        print(f"Bot is ready")

    @bot.event
    async def event_message(message):
        print(f"Received message: {message.content}")

    bot.add_command(hello)

    await bot.start()

asyncio.run(main())
