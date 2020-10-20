import os
import random
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv
from urllib import parse


# Implementation imports
from impl.help import get_help_command
from impl.character_info import get_character_info

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

COMMAND_PREFIX = "!"

bot = commands.Bot(command_prefix=COMMAND_PREFIX)
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(
    name="도움말", 
    brief="도움말을 출력합니다"
)
async def help_command(ctx, *args):
    text = get_help_command(ctx.bot, *args)
    await ctx.send(text)


@bot.command(
    name='주장봇',
    help='주장봇!',
    description='desc',
    brief="주장봇 관련 명령",
    usage='usage'
)
async def greetings(ctx, arg):
    if arg == '안녕' or arg == '하이':
        nick = ctx.author.nick
        if nick == None:
            nick = ctx.author.name
        msg = f'안녕! {nick}! :hearts:'
        await ctx.send(msg)
    else:
        await ctx.send("이해하지 못했어요 ㅠ")


@bot.command(
    name='정보',
    description="캐릭터 정보",
    brief="캐릭터 정보 확인",
    usage="[닉네임]"
)
async def character_info(ctx, name):
    img, embed = get_character_info(name)
    await ctx.send(file=img, embed=embed)


@bot.command(
    name='stop', 
    hidden=True, 
    aliases=["ㄴ새ㅔ"]
)
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

bot.run(TOKEN)
