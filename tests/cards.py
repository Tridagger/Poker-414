# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: cards.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/19
-------------------------------------------------
"""
import random

from core import poker


def cards_generate(types=0):
    """
    牌型生成器
    :param types: 0: 随机, 1: 单牌, 2: 对牌, 3: 顺子, 4: 连对, 5: 炸弹, 6: 导弹, 7: 火箭
    :return: list: 扑克列表
    """
    cards = list(poker.PokerCard())
    card_list = []
    card_dict = {
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': '10',
        '11': 'J',
        '12': 'Q',
        '13': 'K',
        '14': 'A',
    }
    match types:
        case 0:  # 随机牌型
            return cards_generate(random.randint(1, 7))

        case 1:  # 生成单牌
            card_list.append(random.choice(cards))
            return card_list

        case 2:  # 生成对牌
            card_list.append(random.choice(cards))
            card1 = card_list[0]
            if card1[0] == '王':
                card_list = [poker.Card('王', '小', 18), poker.Card('王', '大', 20)]
            else:
                suits = list(poker.PokerCard.suits)
                suits.pop(suits.index(card1[1]))
                card_list.append(poker.Card(card1[0], random.choice(suits), card1.level))
            return card_list

        case 3:  # 生成顺子
            start = random.randint(3, 12)
            number = random.randint(3, 15-start)
            suits = list(poker.PokerCard.suits)
            for i in range(number):
                card_list.append(poker.Card(card_dict[str(start+i)], random.choice(suits), start+i))
            return card_list

        case 4:  # 生成连对
            start = random.randint(3, 12)
            number = random.randint(3, 7 if 15-start > 7 else 15-start)
            for i in range(number):
                suits = list(poker.PokerCard.suits)
                card_list.append(poker.Card(card_dict[str(start + i)], random.choice(suits), start + i))
                suits.pop(suits.index(card_list[i*2][1]))
                card_list.append(poker.Card(card_dict[str(start + i)], random.choice(suits), start + i))
            return card_list

        case 5:  # 生成炸弹
            cards = cards[:-2]
            card_list.append(random.choice(cards))
            suits = list(poker.PokerCard.suits)
            for i in range(2):
                suits.pop(suits.index(card_list[i][1]))
                card_list.append(poker.Card(card_list[0][0], random.choice(suits), card_list[0].level))
            return card_list

        case 6:  # 生成导弹
            cards = cards[:-2]
            card_list.append(random.choice(cards))
            suits = list(poker.PokerCard.suits)
            for i in range(3):
                suits.pop(suits.index(card_list[i][1]))
                card_list.append(poker.Card(card_list[0][0], random.choice(suits), card_list[0].level))
            return card_list

        case 7:  # 生成火箭
            suits = list(poker.PokerCard.suits)
            card_list.append(poker.Card('A', random.choice(suits), 14))
            card_list.append(poker.Card('4', random.choice(suits), 4))
            suits.pop(suits.index(card_list[1][1]))
            card_list.append(poker.Card('4', random.choice(suits), 4))
            random.shuffle(card_list)
            return card_list

        case _:
            return None
