from discord import Embed
from decimal import *

from .util import encode, format_thousands


MAPLE_GG = "https://maple.gg/u/"
ZWS = '\u200B'

DECIMAL_CTX = getcontext().prec = 2

def create_info_embed(
    name=None,
    thumbnail=None,
    user_summary=None,
    guild_name=None,
    rankings=None,
    last_active=None,
    mureung=None,
    the_seed=None,
    maple_union=None,
    achievements=None,
):
    title_url = MAPLE_GG + encode(name)
    level = user_summary[0]
    job = user_summary[1]
    popularity = user_summary[2]
    description = job + " / " + "Lv." + str(level)

    embed = Embed(title=name, url=title_url,
                  description=description, color=0x008000)

    embed.set_thumbnail(url=thumbnail)
    embed.set_image(url="attachment://image.png")

    total_ranking = rankings[0]
    world_ranking = rankings[1]
    embed.add_field(name="종합랭킹", value=total_ranking + "위", inline=True)
    embed.add_field(name="월드랭킹", value=world_ranking + "위", inline=True)
    add_empty_field(embed)

    job_ranking = rankings[2]
    job_ranking_total = rankings[3]
    embed.add_field(name="직업랭킹(월드)", value=job_ranking + "위", inline=True)
    embed.add_field(name="직업랭킹(전체)",
                    value=job_ranking_total + "위", inline=True)
    add_empty_field(embed)

    embed.add_field(name="길드", value=guild_name)
    embed.add_field(name="인기도", value=popularity)
    add_empty_field(embed)

    mureung_text = "-"
    if mureung:
        mureung_text = str(mureung[0]) + "층 (" + mureung[1] + ")"

    seed_text = "-"
    if the_seed:
        seed_text = str(the_seed[0]) + "층 (" + the_seed[1] + ")"

    embed.add_field(name="무릉도장", value=mureung_text, inline=True)
    embed.add_field(name="더 시드", value=seed_text, inline=True)
    add_empty_field(embed)

    union_text = "-"
    union_power = "-"
    if maple_union:
        union_text = maple_union[0] + \
            " (Lv." + format_thousands(maple_union[1]) + ")"
        union_power = format_thousands(maple_union[2])

    embed.add_field(name="메이플 유니온", value=union_text, inline=True)
    embed.add_field(name="유니온 전투력", value=union_power, inline=True)
    add_empty_field(embed)

    achievement_text = "-"
    if achievements:
        achievement_text = achievements[0] + " (" + achievements[1] + ")"

    embed.add_field(name="업적", value=achievement_text, inline=False)

    last_active_text = "-"
    if last_active:
        last_active_text = last_active + "일 전"
    embed.add_field(name="마지막 활동일", value=last_active_text, inline=False)

    return embed


def add_empty_field(embed):
    embed.add_field(name=ZWS, value=ZWS)


def create_exp_embed(
    name=None,
    thumbnail=None,
    job=None,
    level=None,
    experience=None,
    curr_percent=None,
    total_exp=None,
    to_250=None,
    to_275=None,
):
    title_url = MAPLE_GG + encode(name)
    description = job + " / Lv." + str(level)
    embed = Embed(title=name, url=title_url,
                  description=description, color=0x00080)

    embed.set_thumbnail(url=thumbnail)
    embed.set_image(url="attachment://image.png")

    experience_text = format_thousands(experience) + " ({}%)".format(Decimal(curr_percent))
    embed.add_field(name="EXP", value=experience_text, inline=False)

    embed.add_field(name="누적 경험치", value=format_thousands(total_exp), inline=False)

    to_250_text = format_thousands(to_250[0]) + " ({}% 달성)".format(Decimal(to_250[1]))
    embed.add_field(name="Lv.250 까지", value=to_250_text, inline=False)

    to_275_text = format_thousands(to_275[0]) + " ({}% 달성)".format(Decimal(to_275[1]))
    embed.add_field(name="Lv.250 까지", value=to_275_text, inline=False)
    
    return embed