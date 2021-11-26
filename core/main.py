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
# import time
# import socketserver
from core.player import Player
# from core.poker import *
# from core.server import game_server
# from threading import Thread
# from tests.cards import cards_generate
# from core.tools import *
from core.game import GameRound


# 运行程序
def run(debug=False):
    if debug:
        pass
    for i in range(1):
        path = '../logs/log.txt'
        with open(path, 'w+', encoding='GBK') as f:
            f.write('')
        p1 = Player('玩家1')
        p2 = Player('玩家2')
        p3 = Player('玩家3')
        p4 = Player('玩家4')
        game = GameRound(path)
        game.add_player(p1, p2, p3, p4)
        game.start_game(log=True)
