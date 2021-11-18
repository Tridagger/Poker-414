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
from core import poker


# 运行程序
def run(*args, debug=False, **kwargs):
    if debug:
        pass
    card = poker.PokerCard()
    card.shuffle(10)
    print(card[0])
