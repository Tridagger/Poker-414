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


# 运行程序
def run(debug=False):
    if debug:
        pass
    while True:
        ls1 = []
        ls2 = []
        a = input('请输入牌值：').split(',')
        b = input('请输入牌值：').split(',')
        for i in a:
            ls1.append(Card(i, random.choice(PokerCard.suits)))
        for i in b:
            ls2.append(Card(i, random.choice(PokerCard.suits)))
        print(ls1, '\n', ls2)
        print(card_compare(ls1, ls2))
