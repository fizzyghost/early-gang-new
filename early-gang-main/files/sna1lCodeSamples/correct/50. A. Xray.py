from urllib.parse import urlencode
from bots.econBot import *
import sqlite3
import configparser
import os
import threading
import requests
import time
import asyncio
from twitchio.ext import commands

config = configparser.ConfigParser()
config.read(os.path.abspath((os.path.join(directory, "config.ini"))))
spotifyClientID = config.get("spotify", "client id")
spotifyClientSecret = config.get("spotify", "client secret")
spotifyRefreshToken = config.get("spotify", "spotify refresh token")

if spotifyRefreshToken == "":
    print(f'authorize this script by going to:\n{"https://accounts.spotify.com/authorize" + "?" + urlencode({"client_id": spotifyClientID, "response_type": "code", "redirect_uri": "http://localhost:8888/callback", "scope": "user-read-currently-playing user-modify-playback-state"})}')
    authorizationCode = input("enter the authorization code found in the redirected url after \"code=\": ")
    response = requests.post("https://accounts.spotify.com/api/token", auth=(spotifyClientID, spotifyClientSecret), data={"grant_type": "authorization_code", "code": authorizationCode, "redirect_uri": "http://localhost:8888/callback"})
    if 'refresh_token' in response.json():
        with open(os.path.abspath((os.path.join(directory, "config.ini"))), 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if line.startswith("spotify refresh token ="):
                    lines[i] = "spotify refresh token = " + response.json()["refresh_token"] + "\n"
                    break
            with open(os.path.abspath((os.path.join(directory, "config.ini"))), "w") as file:
                file.writelines(lines)
    else:
        print("problem getting tokens " + response.json())

def startCommandBot():
    bot = Bot()
    botThread = threading.Thread(target=bot.run)
    botThread.start()
    return botThread

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=accessToken, prefix="!", initial_channels=[yourChannelName])

    async def event_message(self, message):
        if message.echo:
            return
        async with databaseLock:
            db = sqlite3.connect(os.path.abspath((os.path.join(directory, "chatData.db"))))
            cursor = db.cursor()
            cursor.execute("SELECT * FROM chatters WHERE id = ?", (getBroadcasterId(message.author.name),))
            result = cursor.fetchone()
            if not result:
                cursor.execute("INSERT INTO chatters (id) VALUES (?)", (getBroadcasterId(message.author.name),))
                db.commit()
                await self.connected_channels[0].send("[bot] welcome " + message.author.name + " to early_gang, where we play games and vibe while we wait for dougdoug to stream again. right now we are trying to beat a randomized pokemon white before dougdoug streams again. the controls are up, down, right, start, a, b, x, and y (more at !controls) and additionally the snack family may try to \"help\" you out. enjoy!")
            cursor.close()
            db.close()
        await self.handle_commands(message)

    @commands.command()
    async def controls(self, ctx: commands.Context):
        await ctx.send("[bot] (capitalization doesnt matter) up, down, left, right, hold up, hold down, hold left, hold right, a, hold a, mash a, b, hold b, mash b, x, y, l, r, start, select, stop, wander, up wander, down wander, left wander, right wander, north, south, east, west")

    @commands.command()
    async def what(self, ctx: commands.Context):
        await ctx.send("[bot] chat tries to beat randomised pokemon white before dougdoug streams again")

    @commands.command()
    async def dougdoug(self, ctx: commands.Context):
        await ctx.send("[bot] https://www.twitch.tv/dougdoug")

    @commands.command()
    async def RIGGED(self, ctx: commands.Context):
        await ctx.send("[bot] BUT FAIR")

    @commands.command()
    async def areYouAnImposter(self, ctx: commands.Context):
        await ctx.send("no, no I am not. I am the original early gang, beep bop boop.")

    @commands.command()
    async def bots(self, ctx: commands.Context):
        await ctx.send("[bot] input bot, aka chris snack, presses a random button every minute or so, idle bot steals your controller if you leave it alone for five minutes, and theres a 5% chance of your own input being completely random or the opposite")

    @commands.command()
    async def menu(self, ctx: commands.Context):
        await ctx.send("[bot] !what, !bots, !song, !controls, !vote, !poll, !discord, !watchtime, !bp, !donate, !playlist, !bpShop")

    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send("[bot] https://discord.gg/eYSUuqNUvb")

    @commands.command()
    async def donate(self, ctx: commands.Context):
        await ctx.send("[bot] https://tiltify.com/@early-gang/profile")

    @commands.command()
    async def playlist(self, ctx: commands.Context):
        await ctx.send("[bot] https://open.spotify.com/playlist/0GhV1AmrhugyYsCb8gEHsS?si=02930e0a7cd54a03")

    @commands.command()
    async def raid(self, ctx: commands.Context):
        if ctx.author.name == "sna1l_boy":
            ctx.message.content = ctx.message.content.replace("!raid ", "")
            raid(yourChannelName, ctx.message.content)
            openGame()

    @commands.command()
    async def mod(self, ctx: commands.Context):
        if ctx.author.name == "sna1l_boy":
            ctx.message.content = ctx.message.content.replace("!mod ", "")
            requests.post("https://api.twitch.tv/helix/moderation/moderators?broadcaster_id=" + getBroadcasterId(yourChannelName) + "&user_id=" + getBroadcasterId(ctx.message.content), headers={"Authorization": f"Bearer {accessToken}", "Client-Id": clientID})

    @commands.command()
    async def panicCode(self, ctx: commands.Context):
        connected = False
        while not connected:
            try:
                response = requests.get("https://api.twitch.tv/helix/users", headers={"Client-ID": clientID, "Authorization": f"Bearer {accessToken}"})
                rateLimit = response.headers.get("Ratelimit-Remaining")
                if rateLimit != "0":
                    response = requests.get("https://api.twitch.tv/helix/moderation/moderators?broadcaster_id=" + getBroadcasterId(yourChannelName), headers={"Authorization": f"Bearer {accessToken}", "Client-Id": clientID})
                    connected = True
                else:
                    time.sleep(5)
            except:
                time.sleep(5)
        modIds = []
        for mod in response.json().get("data"):
            modIds += [mod.get("user_id")]
        if getBroadcasterId(ctx.author.name) in modIds or ctx.author.name == yourChannelName:
            with open(os.path.abspath((os.path.join(directory, "config.ini"))), "r") as file:
                lines = file.readlines()
            for i, line in enumerate(lines):
                if line.startswith("ping kai ="):
                    lines[i] = "ping kai = True\n"
                    break
            with open(os.path.abspath((os.path.join(directory, "config.ini"))), "w") as file:
                file.writelines(lines)

    @commands.command()
    async def panicStream(self, ctx: commands.Context):
        connected = False
        while not connected:
            try:
                response = requests.get("https://api.twitch.tv/helix/users", headers={"Client-ID": clientID, "Authorization": f"Bearer {accessToken}"})
                rateLimit = response.headers.get("Ratelimit-Remaining")
                if rateLimit != "0":
                    response = requests.get("https://api.twitch.tv/helix/moderation/moderators?broadcaster_id=" + getBroadcasterId(yourChannelName), headers={"Authorization": f"Bearer {accessToken}", "Client-Id": clientID})
                    connected = True
                else:
                    time.sleep(5)
            except:
                time.sleep(5)
        modIds = []
        for mod in response.json().get("data"):
            modIds += [mod.get("user_id")]
        if getBroadcasterId(ctx.author.name) in modIds or ctx.author.name == yourChannelName:
            with open(os.path.abspath((os.path.join(directory, "config.ini"))), "r") as file:
                lines = file.readlines()
            for i, line in enumerate(lines):
                if line.startswith("ping fizz ="):
                    lines[i] = "ping fizz = True\n"
                    break
            with open(os.path.abspath((os.path.join(directory, "config.ini"))), "w") as file:
                file.writelines(lines)

    @commands.command()
    async def song(self, ctx: commands.Context):
        response = requests.post("https://accounts.spotify.com/api/token", auth=(spotifyClientID, spotifyClientSecret), data={"grant_type": "refresh_token", "refresh_token": spotifyRefreshToken})
        data = response.json()
        if "access_token" in data:
            accessToken = data["access_token"]
        else:
            print("error refreshing token: " + data)
            accessToken = None
        response = requests.get("https://api.spotify.com/v1/me/player/currently-playing", headers={"Authorization": f"Bearer {accessToken}"})
        if response.status_code == 200:
            data = response.json()
            if data['is_playing']:
                await ctx.send(f"[bot] {data['item']['name']} by {data['item']['artists'][0]['name']}")
            else:
                await ctx.send("[bot] no song playing")
        else:
            await ctx.send("[bot] can't get song")
