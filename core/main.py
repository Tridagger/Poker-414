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

    path = f"../logs/game_record_{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))}.txt"
    for i in range(100):
        p1 = Player('玩家1', ai=True)
        p2 = Player('玩家2')
        p3 = Player('玩家3')
        p4 = Player('玩家4')

        game = GameRound(path=path)
        game.add_player(p1, p2, p3, p4)
        game.start_game(log=True)
        print(f"第i局结束")


