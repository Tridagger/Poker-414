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
import time

from core.poker import *
from core.utils import *
from tests.cards import cards_generate
import time


# 运行程序
def run(debug=False):
    if debug:
        pass
    c = 0
    t = time.time()
    while True:
        card1 = cards_generate(0)
        assert hand_type(card1)
        card2 = PokerCard().shuffle(2)[:14]
        card_hint(card1, card2)
        c += 1
        if c % 10000 == 0:
            print(c)
            print(time.time()-t)
