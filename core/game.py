# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: game.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/20
-------------------------------------------------
"""

from core.poker import PokerCard, Card
from core.utils import *


class GameRound:
    def __init__(self, first=True):
        self.players = []
        self.all_cards = PokerCard().shuffle(2)  # 生成一副新的扑克牌, 洗两次牌
        self.first = first  # 是否是第一局游戏
        self.current_cards = []

    def start_game(self, first=None):
        assert len(self.players) == 4  # 保证四个玩家
        if self.first:
            if not first:
                random.choice(self.players).king = True  # 随机一个人先抓牌
            else:
                first.king = True

        self.__distribute_cards()  # 发牌
        self.__play_game()

    def add_player(self, *args):
        """
        向游戏中添加玩家
        :param args: Player 玩家对象
        :return:
        """
        self.players = list(args)

    def __remove_king(self):
        for p in self.players:
            p.king = False

    def __set_king(self):
        for p in self.players:
            p.king = True

    def __distribute_cards(self):
        while self.all_cards:
            for p in self.players:
                if self.all_cards and p.king:
                    self.__set_king()
                    assert self.all_cards
                    p.cards.append(self.all_cards.pop(0))

    def __who_has_heart_3(self):
        for player in self.players:
            if Card('3', '红桃') in player.cards:
                return player

    def __play_game(self):
        h3 = self.__who_has_heart_3()  # 判断红桃3在谁的手里
        self.__play_cards(h3)

    def __play_cards(self, player):
        """
        随机出牌 玩家的手牌减少，出的牌更新到 self.current_cards 中
        :param player: 玩家对象
        :return: None
        """
        played_cards = random_play_card(player.cards)
        for card in played_cards:
            for index, item in enumerate(player.cards):
                if card == item[0]:
                    self.current_cards.append(player.cards.pop(index))
                    break
        p_index = self.players.index(player)
        if p_index == len(self.players) - 1:
            self.players[0].turn = True
        else:
            self.players[p_index + 1] = True
