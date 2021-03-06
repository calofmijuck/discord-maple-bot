import requests
import discord
from urllib import parse

def format_thousands(n):
    return '{:,}'.format(n)

def format_two_decimal(x):
    return "{:.2f}".format(x).rstrip('0').rstrip('.')

def parse_int(s):
    return int(s.replace(',', ''))

def get_character_image(name, url):
    img_data = requests.get(url).content
    path = 'char_img/' + name + '.png'
    with open(path, 'wb') as handler:
        handler.write(img_data)
    img = discord.File(path, filename="image.png")
    return img

def encode(name):
    return parse.quote(name)

def bold(s):
    return "**" + s + "**"

def italic(s):
    return "_" + s + "_"