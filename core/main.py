# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: main.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/18
-------------------------------------------------
"""

from core.poker import *
from core.utils import *
from tests.cards import cards_generate


# 运行程序
def run(debug=False):
    if debug:
        pass
    c = 0
    while True:
        cards = list(PokerCard().shuffle(2))[:13]
        if have_pair(cards, 3)[0]:
            print(sorted([calc_card_level(card) for card in cards]))
            print(have_pair(cards, 3))
            break

