# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: game.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/27
-------------------------------------------------
"""

from core.poker import PokerCard


class GameRound:
    def __init__(self):
        self.round_cards = PokerCard().shuffle()
        self.players = []
        self.static_players = []

    def add_player(self, client_address):  # 向对局中添加玩家
        if client_address not in self.static_players:
            self.static_players.append(client_address)
            self.players.append(client_address)

