@echo off

start /B py main.py
start /B py bots/twitch/econBot.py
start /B py bots/twitch/pollBot.py

pause
