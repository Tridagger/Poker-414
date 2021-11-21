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
from core.poker import *
import time


# 运行程序
def run(debug=False):
    if debug:
        pass
    p1 = Player('玩家1')
    p2 = Player('玩家2')
    p3 = Player('玩家3')
    p4 = Player('玩家4')
    for i in range(1000000000):
        game = GameRound()
        game.add_player(p1, p2, p3, p4)
        game.start_game()
        print(f"第{i+1}局结束")
    print(p1.win_times, p2.win_times, p3.win_times, p4.win_times)
