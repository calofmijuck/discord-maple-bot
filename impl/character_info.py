from bs4 import BeautifulSoup
from time import sleep
import re
import requests
import discord

from .util import parse_int, get_character_image, encode
from .CharacterInfo import CharacterInfo
from .embeds import create_embed

MAPLE_GG = "https://maple.gg/u/"
NO_SUCH_CHARACTER = "캐릭터가 존재하지 않습니다."


def get_character_info(name):
    parser = fetch_info_page(name)

    if not character_exists(parser):
        return CharacterInfo(error=NO_SUCH_CHARACTER)

    if not character_updated(name, parser):
        return CharacterInfo(sync=True)

    return parse_character_info(name, parser)


def fetch_info_page(name):
    info_page = requests.get(MAPLE_GG + encode(name))
    parser = BeautifulSoup(info_page.content, 'html.parser')
    return parser

def character_exists(parser):
    no_data = parser.find(class_="container mt-5 text-center")
    if no_data != None:
        return False
    else:
        return True


def character_updated(name, parser):
    sync = parser.find(id="btn-sync").text.strip()
    if sync == "정보갱신":
        update_character_info(name)
        return False
    else:
        return True


def update_character_info(name):
    requests.get(MAPLE_GG + encode(name) + "/sync")


def parse_character_info(name, parser):
    world_icon_url = get_world_icon_url(parser)
    character_img_url = get_character_img_url(parser)

    user_summary = get_user_summary(parser)
    guild_name = get_guild_name(parser)
    rankings = get_user_ranking(parser)
    last_active = get_last_active(parser)

    mureung = get_mureung_info(parser)
    the_seed = get_seed_info(parser)
    maple_union = get_maple_union_info(parser)
    achievements = get_achievements(parser)

    embed = create_embed(
        name=name,
        thumbnail=world_icon_url,
        user_summary=user_summary,
        guild_name=guild_name,
        rankings=rankings,
        last_active=last_active,
        mureung=mureung,
        the_seed=the_seed,
        maple_union=maple_union,
        achievements=achievements
    )
    img = get_character_image(name, character_img_url)

    return CharacterInfo(embed=embed, img=img)


def get_world_icon_url(parser):
    h3 = parser.find('h3')
    url = h3.find('img')['src']
    return url


def get_character_img_url(parser):
    url = parser.find(class_="character-image")['src']
    return url


def get_user_summary(parser):
    summary_list = parser.find(class_="user-summary-list").find_all('li')
    level = int(summary_list[0].text.split('.')[1])
    job = summary_list[1].text
    popularity = summary_list[2].text.split('\n')[1]
    return [level, job, popularity]


def get_guild_name(parser):
    guild_info = parser.find(
        class_="col-lg-2 col-md-4 col-sm-4 col-12 mt-3").text
    guild_name = guild_info.split()[1]
    if guild_name == "(없음)":
        return "-"
    else:
        return guild_name


def get_user_ranking(parser):
    rankings = []
    ranking_info = parser.find_all(
        class_="col-lg-2 col-md-4 col-sm-4 col-6 mt-3")
    for info in ranking_info:
        rank_data = info.find('span').text
        rank_value = rank_data.split('위')[0].strip()
        rankings.append(rank_value)
    return rankings


def get_last_active(parser):
    last_active_data = parser.find(class_="font-size-12 text-white")
    if last_active_data == None:
        return ""
    else:
        last_active_data = last_active_data.text
    start_idx = last_active_data.find(':')
    end_idx = last_active_data.find('\n')
    last_active = last_active_data[start_idx + 2: end_idx]
    return last_active


def get_mureung_info(parser):
    mureung = parser.find_all(class_="col-lg-3 col-6 mt-3 px-1")[0]
    floor_data = mureung.find(class_="user-summary-floor font-weight-bold")
    if floor_data == None:
        return []
    else:
        floor = parse_int(floor_data.text.split()[0])
        duration = mureung.find(class_="user-summary-duration").text
        return [floor, duration]


def get_seed_info(parser):
    seed = parser.find_all(class_="col-lg-3 col-6 mt-3 px-1")[1]
    floor_data = seed.find(class_="user-summary-floor font-weight-bold")
    if floor_data == None:
        return []
    else:
        floor = parse_int(floor_data.text.split()[0])
        duration = seed.find(class_="user-summary-duration").text
        return [floor, duration]


def get_maple_union_info(parser):
    union_data = parser.find_all(class_="col-lg-3 col-6 mt-3 px-1")[2]
    tier_data = union_data.find(
        class_="user-summary-tier-string font-weight-bold")
    if tier_data == None:
        return []
    else:
        tier = tier_data.text.strip()
        level_data = union_data.find(class_="user-summary-level").text
        level = parse_int(level_data.split('.')[1])
        power_data = union_data.find(class_="d-block mb-1").text
        power = parse_int(power_data.split()[1])
        return [tier, level, power]


def get_achievements(parser):
    achievement_data = parser.find_all(class_="col-lg-3 col-6 mt-3 px-1")[3]
    tier_data = achievement_data.find(
        class_="user-summary-tier-string font-weight-bold")
    if tier_data == None:
        return []
    else:
        tier = tier_data.text.strip()
        score_data = achievement_data.find(class_="user-summary-level").text
        score = score_data.split()[1]
        return [tier, score]
