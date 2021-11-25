# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: game2.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/25
-------------------------------------------------
"""
from core.poker import PokerCard


class GameRound:
    def __init__(self, path):
        self.players = []
        self.all_cards = PokerCard().shuffle(2)
        self.current_cards = {'cards': [], 'player': None}
        self.path = path
        self.log = False

    def start_game(self, log=False):
        assert len(self.players) == 4  # 保证四个玩家
        if log:
            self.log = True
            with open(self.path, 'a+', encoding='utf-8') as f:
                f.write("-"*200+"\n")
                f.write("4名玩家已就位，准备开始游戏！\n")



    def add_player(self, *args):
        self.players = list(args)
