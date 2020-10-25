import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from time import sleep


# Implementation imports
from impl.help import get_help_command
from impl.character_info import get_character_info
from impl.roll_dice import get_roll_result
from impl.experience_info import get_experience_info

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

COMMAND_PREFIX = "!"

bot = commands.Bot(command_prefix=COMMAND_PREFIX)
bot.remove_command('help')

SYNCING = "정보 갱신 중입니다 :hourglass_flowing_sand:"


@bot.event
async def on_ready():
    activity = discord.Activity(
        type=discord.ActivityType.listening, name="MapleStory 명령")
    await bot.change_presence(activity=activity)
    print(f'{bot.user} has connected to Discord!')


@bot.command(
    name="도움말",
    description="도움말과 명령어 목록을 출력합니다.",
)
async def help_command(ctx, *args):
    text = get_help_command(ctx.bot, *args)
    await ctx.send(text)


@bot.command(
    name='주장봇',
    description='주장봇 관련 명령입니다.',
    hidden=True
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
    description="캐릭터의 종합 정보를 확인합니다.",
    usage="[닉네임]"
)
async def character_info(ctx, name):
    info = get_character_info(name)
    if info.error != None:
        await ctx.send(info.error)
    elif info.sync:
        await ctx.send(SYNCING)
        sleep(5)
        await character_info(ctx, name)
    else:
        await ctx.send(file=info.img, embed=info.embed)


@bot.command(
    name='경험치',
    description="캐릭터의 경험치 정보를 확인합니다.",
    usage="[닉네임]"
)
async def experience_info(ctx, name):
    info = get_experience_info(name)
    if info.error != None:
        await ctx.send(info.error)
    else:
        await ctx.send(file=info.img, embed=info.embed)


@bot.command(
    name='주사위',
    description='주사위를 굴립니다. 1 부터 100 까지의 수가 나옵니다.',
    aliases=['데굴데굴']
)
async def roll_dice(ctx):
    text = get_roll_result()
    await ctx.send(text)


@bot.command(
    name='stop',
    hidden=True,
    aliases=["ㄴ새ㅔ"]
)
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

bot.run(TOKEN)
