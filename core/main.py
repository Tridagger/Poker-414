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
    cnt = 0
    for i in range(100000):
        a = cards_generate(random.randint(1, 7))
        b = 'red,black'.split(',')
        c = [Card(i, random.choice(PokerCard.suits)) for i in b]
        if not card_compare(a, c):
            print(a)
            cnt += 1
    print(cnt)

