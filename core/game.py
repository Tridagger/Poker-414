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
from core.player import SPlayer


class GameRound:
    def __init__(self):
        self.round_cards = PokerCard().shuffle()
        self.players = []
        self.static_players = []

    def add_player(self, client_address):  # 向对局中添加玩家
        if client_address not in [p.addr for p in self.static_players]:
            player = SPlayer(str(len(self.players)+1), client_address)
            self.static_players.append(player)
            self.players.append(player)

    def addr_to_player(self, addr):
        for player in self.players:
            if player.addr == addr:
                return player

    def circle_del(self, player):
        ls = self.players
        assert player in ls
        i = ls.index(player)
        ls = ls[i:] + ls[:i]
        ls.remove(player)
        self.players = ls

    def circle(self, player):
        ls = self.players
        assert player in ls
        i = ls.index(player)
        ls = ls[i:] + ls[:i]
        self.players = ls

    def next(self, player):
        i = self.players.index(player)
        if i == len(self.players)-1:
            return self.players[0].addr
        else:
            return self.players[i+1].addr

    def reround(self):
        self.players = list(self.static_players)
        self.round_cards = PokerCard().shuffle()


