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

    # d = cards_generate(0)
    a = PokerCard().shuffle()
    c = list(a)
    b = c[0:3]
    print(sort_card(b))
    print(play_cards(b))


