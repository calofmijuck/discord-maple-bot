from discord import Embed
from .util import encode, format_thousands

MAPLE_GG = "https://maple.gg/u/"
ZWS = '\u200B'


def create_embed(
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
        achievement_text = achievements[0] + "(" + achievements[1] + ")"

    embed.add_field(name="업적", value=achievement_text, inline=False)
    embed.add_field(name="마지막 활동일", value=last_active + "일 전", inline=False)

    return embed


def add_empty_field(embed):
    embed.add_field(name=ZWS, value=ZWS)
