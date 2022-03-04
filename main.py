import requests
import random
import string
import threading
from itertools import cycle
from colorama import Fore
import os
from discord.ext import commands 
import discord, requests, random, threading, asyncio
from webserver import keep_alive
os.system('color')

my_secret = os.environ['token']
token = os.environ['token']

with open('proxies.txt', 'r+', encoding='utf-8') as f:
    proxy = cycle(f.read().splitlines())
with open('cookies.txt', 'r+', encoding='utf-8') as f:
    cookie = cycle(f.read().splitlines())

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('Bot is online!')

def follow():
        try:
            proxies = {
                'https': 'https://' + next(proxy)
            }
            cookies = {
                'sessionid': next(cookie)
            }
            sendfollow = requests.post(f'https://www.instagram.com/web/friendships/{clientid}/follow/', cookies=cookies, headers=headers, proxies=proxies)
    except:
        pass


@bot.command()
async def ig(ctx, userId):
    await ctx.send(f'<@{ctx.author.id}>, **sending instagram followers made by Bling#9999**')
            
keep_alive()
bot.run(token)
