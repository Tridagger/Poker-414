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
    def __init__(self):
        self.players = []
        self.all_cards = PokerCard().shuffle(2)
        self.current_cards = {'cards': [], 'player': None}

    def start_game(self):
        pass