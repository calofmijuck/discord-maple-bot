import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='주사위', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    if number_of_sides <= 0:
        await ctx.send("주사위 면의 수는 0 보다 커야 합니다.")
        return
    if number_of_dice <= 0:
        await ctx.send("주사위 개수는 0 보다 커야 합니다.")
        return

    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

bot.run(TOKEN)