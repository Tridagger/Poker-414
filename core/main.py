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

    card2 = PokerCard().shuffle(2)[:6]
    print(card2)
    card3 = random_play_card(card2)
    print(card3)