from random import randint
from .util import italic

def get_roll_result():
    idx = randint(0, 99)
    return italic(ROLL_RESULT[idx])


ROLL_RESULT = [
    '꽝이라고 해야겠군요. 주사위가 1 나왔습니다...',
    '완전 망이네요. 주사위가 2 나왔습니다...',
    '정말 망이네요. 주사위가 3 나왔습니다...',
    '심심하게 망이네요. 주사위가 4 나왔습니다...',
    '어쩔수없이 망이네요. 주사위가 5 나왔습니다...',
    '망이네요. 주사위가 6 나왔습니다...',
    '재미없이 망이네요. 주사위가 7 나왔습니다...',
    '스스럼없이 망이네요. 주사위가 8 나왔습니다...',
    '이런 망이네요. 주사위가 9 나왔습니다...',
    '거의 망이네요. 주사위가 10 나왔습니다...',
    '11 입니다. 어렵습니다. 너무 슬퍼마세요...',
    '12 입니다. 어렵겠어요. 너무 슬퍼마세요...',
    '13 입니다. 어려울것 같아요. 너무 슬퍼마세요...',
    '14 입니다. 어렵겠죠? 너무 슬퍼마세요...',
    '15 입니다. 어려울까요? 너무 슬퍼마세요...',
    '16 입니다. 어렵네요. 너무 슬퍼마세요...',
    '17 입니다. 어렵지만, 너무 슬퍼마세요...',
    '18 입니다. 어려워보여요. 너무 슬퍼마세요...',
    '19 입니다. 어려운 희망이에요. 너무 슬퍼마세요...',
    '20 입니다. 어렵겠어요. 그래도 너무 슬퍼마세요...',
    '주사위는 확실히 잘못이 없습니다. 유감스럽게도 21 입니다...',
    '주사위는 정말 잘못이 없습니다. 유감스럽게도 22 입니다...',
    '주사위는 완전 잘못이 없습니다. 유감스럽게도 23 입니다...',
    '주사위는 조금이라도 잘못이 없습니다. 유감스럽게도 24 입니다...',
    '주사위는 정말 잘못이 없습니다. 유감스럽게도 25 입니다...',
    '주사위는 스스럼없이 잘못이 없습니다. 유감스럽게도 26 입니다...',
    '주사위는 심심하게도 잘못이 없습니다. 유감스럽게도 27 입니다...',
    '주사위는 그래도 잘못이 없습니다. 유감스럽게도 28 입니다...',
    '주사위는 별로 잘못이 없습니다. 유감스럽게도 29 입니다...',
    '주사위는 잘못이 없습니다. 유감스럽게도 30 입니다...',
    '그닥 좋은 운은 아니네요. 주사위는 31 입니다...',
    '별로 좋은 운은 아니네요. 주사위는 32 입니다...',
    '오늘 좋은 운은 아니네요. 주사위는 33 입니다...',
    '살포시 좋은 운은 아니네요. 주사위는 34 입니다...',
    '그냥그렇게 좋은 운은 아니네요. 주사위는 35 입니다...',
    '그렇게 좋은 운은 아니네요. 주사위는 36 입니다...',
    '마음껏 좋은 운은 아니네요. 주사위는 37 입니다...',
    '이미 좋은 운은 아니네요. 주사위는 38 입니다...',
    '어제부터 좋은 운은 아니네요. 주사위는 39 입니다...',
    '쭈욱 좋은 운은 아니네요. 주사위는 40 입니다...',
    '온몸을 던져 주사위를 굴렸으나 41 나왔습니다...',
    '온마음을 던져 주사위를 굴렸으나 42 나왔습니다...',
    '모니터를 던져 주사위를 굴렸으나 43 나왔습니다...',
    '컴퓨터를 던져 주사위를 굴렸으나 44 나왔습니다...',
    '키보드를 던져 주사위를 굴렸으나 45 나왔습니다...',
    '서버를 던져 주사위를 굴렸으나 46 나왔습니다...',
    '집을 던져 주사위를 굴렸으나 47 나왔습니다...',
    '의자를 던져 주사위를 굴렸으나 48 나왔습니다...',
    '우유를 던져 주사위를 굴렸으나 49 나왔습니다...',
    '커피를 던져 주사위를 굴렸으나 50 나왔습니다...',
    '뼈에 사무치도록 주사위를 힘껏 던져 51 나왔습니다...',
    '뼈에 사무치도록 주사위를 열심히 던져 52 나왔습니다...',
    '뼈에 사무치도록 주사위를 마음껏 던져 53 나왔습니다...',
    '뼈에 사무치도록 주사위를 알차게 던져 54 나왔습니다...',
    '뼈에 사무치도록 주사위를 보람차게 던져 55 나왔습니다...',
    '뼈에 사무치도록 주사위를 조심히 던져 56 나왔습니다...',
    '뼈에 사무치도록 주사위를 우렁차게 던져 57 나왔습니다...',
    '뼈에 사무치도록 주사위를 저멀리 던져 58 나왔습니다...',
    '뼈에 사무치도록 주사위를 어쩔수없이 던져 59 나왔습니다...',
    '뼈에 사무치도록 주사위를 힘차게 던져 60 나왔습니다...',
    '별 감흥없이 주사위를 굴렸으나 61 나왔습니다...',
    '별 느낌없이 주사위를 굴렸으나 62 나왔습니다...',
    '별 의욕없이 주사위를 굴렸으나 63 나왔습니다...',
    '별 눈물없이 주사위를 굴렸으나 64 나왔습니다...',
    '별 감동없이 주사위를 굴렸으나 65 나왔습니다...',
    '별 기쁨없이 주사위를 굴렸으나 66 나왔습니다...',
    '별 설레임없이 주사위를 굴렸으나 67 나왔습니다...',
    '별 아무것도 없이 주사위를 굴렸으나 68 나왔습니다...',
    '별 감격없이 주사위를 굴렸으나 69 나왔습니다...',
    '별 의지없이 주사위를 굴렸으나 70 나왔습니다...',
    '대단합니다! 주사위는 71 입니다...',
    '정말 대단합니다! 주사위는 72 입니다...',
    '이런 대단합니다! 주사위는 73 입니다...',
    '대단합니다! 주사위는 74 입니다...',
    '오, 대단합니다! 주사위는 75 입니다...',
    '와, 대단합니다! 주사위는 76 입니다...',
    '완전, 대단합니다! 주사위는 77 입니다...',
    '진실로, 대단합니다! 주사위는 78 입니다...',
    '이얼~ 대단합니다! 주사위는 79 입니다...',
    '오호~ 대단합니다! 주사위는 80 입니다...',
    '축하드립니다! 확실한 결과입니다. 81 입니다!',
    '축하드립니다! 대단한 결과입니다. 82 입니다!',
    '축하드립니다! 기록적인 결과입니다. 83 입니다!',
    '축하드립니다! 의미있는 결과입니다. 84 입니다!',
    '축하드립니다! 확정적인 결과입니다. 85 입니다!',
    '축하드립니다! 우레같은 결과입니다. 86 입니다!',
    '축하드립니다! 폭풍같은 결과입니다. 87 입니다!',
    '축하드립니다! 태풍같은 결과입니다. 88 입니다!',
    '축하드립니다! 엄청난 결과입니다. 89 입니다!',
    '축하드립니다! 실로 엄청난 결과입니다. 90 입니다!',
    '메이플 봇이 보증합니다. 주사위가 91 나왔습니다!!',
    '메이플 봇이 인정해드립니다. 주사위가 92 나왔습니다!!',
    '메이플 봇이 살짝 보증합니다. 주사위가 93 나왔습니다!!',
    '메이플 봇이 확실하게 보증합니다. 주사위가 94 나왔습니다!!',
    '메이플 봇이 살포시 보증합니다. 주사위가 95 나왔습니다!!',
    '메이플 봇이 정말 보증합니다. 주사위가 96 나왔습니다!!',
    '메이플 봇이 주사위를 보증합니다. 주사위가 97 나왔습니다!!',
    '메이플 봇이 정확하게 보증합니다. 주사위가 98 나왔습니다!!',
    '메이플 봇이 확실히 보증합니다. 주사위가 99 나왔습니다!!',
    '메이플 봇이 무조건 확실히 정확하게 보증합니다. 주사위가 100 나왔습니다!!',
]
