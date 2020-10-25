import requests
from bs4 import BeautifulSoup

from .embeds import create_exp_embed
from .exp_const import REQUIRED_EXP, CUMULATIVE_EXP, EXP_AT_250, EXP_AT_275
from .CharacterInfo import CharacterInfo
from .util import encode, parse_int, get_character_image

MAPLE_RANKING = "https://maplestory.nexon.com/Ranking/World/Total?c="
NO_SUCH_CHARACTER = "캐릭터가 존재하지 않습니다."


def get_experience_info(name):
    parser = fetch_ranking_page(name)

    if parser == None:
        return CharacterInfo(error=NO_SUCH_CHARACTER)

    return parse_experience_info(name, parser)


def fetch_ranking_page(name):
    ranking_page = requests.get(MAPLE_RANKING + encode(name))
    soup = BeautifulSoup(ranking_page.content, 'html.parser')
    parser = soup.find(class_="search_com_chk")
    return parser


def parse_experience_info(name, parser):
    info = parser.find_all('td')

    world_icon_url = get_world_icon_url(info)
    character_img_url = get_character_image_url(info)
    job = get_job_name(info)
    level = get_level(info)
    experience = get_experience(info)

    curr_percent = get_current_percentage(level, experience)
    total_exp = get_total_exp(level, experience)
    to_250 = get_achieved_info(EXP_AT_250, total_exp)
    to_275 = get_achieved_info(EXP_AT_275, total_exp)

    embed = create_exp_embed(
        name=name,
        thumbnail=world_icon_url,
        job=job,
        level=level,
        experience=experience,
        curr_percent=curr_percent,
        total_exp=total_exp,
        to_250=to_250,
        to_275=to_275
    )

    img = get_character_image(name, character_img_url)

    return CharacterInfo(embed=embed, img=img)


def get_world_icon_url(info):
    world_icon_url = info[1].find('dt').find('img')['src']
    return world_icon_url


def get_character_image_url(info):
    img_tag = info[1].find('span').find_all('img')[0]
    img_url = img_tag['src']
    return img_url


def get_job_name(info):
    job_info = info[1].find('dd')
    job = job_info.text.split(' / ')[1]
    return job


def get_level(info):
    level = parse_int(info[2].text.split('.')[1])
    return level


def get_experience(info):
    experience = parse_int(info[3].text)
    return experience


def get_current_percentage(level, experience):
    required = REQUIRED_EXP[level - 1]
    percent = experience / required * 100
    return percent


def get_total_exp(level, experience):
    cumulated = CUMULATIVE_EXP[level - 1]
    total_exp = cumulated + experience
    return total_exp


def get_achieved_info(target_exp, total_exp):
    required = max(0, target_exp - total_exp)
    achieved_rate = (target_exp - required) / target_exp * 100
    return [required, achieved_rate]


get_experience_info("모이스쳐그린")
