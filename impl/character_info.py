from bs4 import BeautifulSoup
from urllib import parse
import re
import requests
import discord

def parse_info(html, name):
    world_ranking_text = html.find(class_="\'ranking_other\'")
    world_ranking = int(world_ranking_text.text.strip())

    try:
        span = html.find(class_='char_img')
        character_image_url = span.find('img')['src']
    except:
        # TODO
        pass

    job_group, job = html.find('dd').text.split(' / ')

    td = html.find_all('td')[-4:]
    level_text = td[0].text
    experience_text = td[1].text
    popularity_text = td[2].text
    guild_name = td[3].text

    if len(guild_name) == 0:
        guild_name = "-"

    info = [name, world_ranking, character_image_url, job_group, job, level_text, experience_text, popularity_text, guild_name]

    return info

def get_info(name):
    name_enc = parse.quote(name)
    
    req_url = "https://maplestory.nexon.com/Ranking/World/Total?c="

    search_result = requests.get(req_url + name_enc)

    soup = BeautifulSoup(search_result.content, 'html.parser')

    character_info_html = soup.find(class_="search_com_chk")

    if character_info_html == None:
        raise Exception("No such character")

    character_info = parse_info(character_info_html, name)
    return character_info

def get_character_info(name):
    info = get_info(name)

    name = info[0]
    name_enc = parse.quote(name)
    world_ranking = '{:,}'.format(int(info[1]))
    character_img_url = info[2]
    job_group = info[3]
    job = info[4]
    level_text = info[5]
    experience_text = info[6]
    popularity_text = info[7]
    guild_name = info[8]

    img = get_character_img(name, character_img_url)

    title_url = "https://maple.gg/u/" + name_enc
    description = job + " / " + level_text
    embed = discord.Embed(title=name, url=title_url,
                          description=description, color=0x008000)
    embed.set_image(url="attachment://image.png")
    embed.add_field(name="종합랭킹", value=str(world_ranking) + "위", inline=False)
    embed.add_field(name="EXP", value=experience_text, inline=False)
    embed.add_field(name="인기도", value=popularity_text, inline=False)
    embed.add_field(name="길드", value=guild_name, inline=False)
    return img, embed

def get_character_img(name, url):
    img_data = requests.get(url).content
    path = 'char_img/' + name + '.png'
    with open(path, 'wb') as handler:
        handler.write(img_data)
    img = discord.File(path, filename="image.png")
    return img
