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
import socketserver
from core.game import GameRound
from core.player import Player
from core.poker import *
from core.server import game_server
from threading import Thread
from tests.cards import cards_generate
from core.tools import *


# 运行程序
def run(debug=False):
    if debug:
        pass

    p1 = Player('P1')
    d = cards_generate(0)
    a = PokerCard().shuffle()
    c = list(a)
    p1.cards = c[0:14]
    print(p1.cards)
    print(d)
    print(p1.over_cards(d))
    print(p1.cards)

