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
import random

from core.poker import *


# 运行程序
def run(*args, debug=False, **kwargs):
    if debug:
        pass
    while True:
        ls = []
        a = input('请输入牌值：').split(',')
        for i in a:
            ls.append(Card(i, random.choice(PokerCard.suits)))
        print(ls)
        print(whats_hand(ls))
