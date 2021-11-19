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


# 运行程序
def run(*args, debug=False, **kwargs):
    if debug:
        pass
    card = PokerCard()
    card.shuffle(5)
    card_ls = card[0:14]
    for index, item in enumerate(card_ls):
        print(index, item)
    while True:
        ls = input('请出牌:').split(',')  # 用,作分割符
        ls = [int(n) for n in ls]
        lst = []
        for i in ls:
            lst.append(card_ls[i])

        print(whats_hand(lst))
