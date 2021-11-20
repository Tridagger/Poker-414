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

from core.utils import *
from tests.cards import cards_generate
from core.game import GameRound
from core.player import Player
import time


# 运行程序
def run(debug=False):
    if debug:
        pass

    p1 = Player('玩家1')
    p2 = Player('玩家2')
    p3 = Player('玩家3')
    p4 = Player('玩家4')
    game = GameRound()
    game.add_player(p1, p2, p3, p4)
    game.start_game()
