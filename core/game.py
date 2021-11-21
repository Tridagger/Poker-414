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
import random
import time
from core.poker import PokerCard, Card
from core.utils import *


class GameRound:
    def __init__(self):
        self.static_players = []
        self.players = []
        self.all_cards = PokerCard().shuffle(2)  # 生成一副新的扑克牌, 洗两次牌
        self.current_cards = {'cards': [], 'player': None}

    def start_game(self):
        assert len(self.players) == 4  # 保证四个玩家
        have_king = False
        for player in self.players:
            if player.king:
                have_king = True
        if not have_king:
            random.choice(self.players).king = True  # 随机一个人先抓牌

        for player in self.players:
            player.clean_up()  # 清空手里的牌
            player.turn = False
        self.__distribute_cards()  # 发牌
        self.__play_game()

    def add_player(self, *args):
        """
        向游戏中添加玩家
        :param args: Player 玩家对象
        :return:
        """
        self.players = list(args)
        self.static_players = list(args)

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
                player.turn = True
                self.current_cards['player'] = player
                return player

    def __play_game(self):
        h3 = self.__who_has_heart_3()  # 红桃3 设置牌权
        while len(self.players) > 1:
            for player in self.players:
                if player.turn:
                    if player == self.current_cards['player']:
                        self.__play_cards(player)
                    else:
                        self.__over_cards(player)


    def __play_cards(self, player):
        """
        随机出牌 玩家的手牌减少，出的牌更新到 self.current_cards 中
        :param player: 玩家对象
        :return: None
        """
        self.current_cards['cards'] = []
        self.current_cards['player'] = player
        played_cards = random_play_card(player.cards)
        player.cards, self.current_cards['cards'] = post_cards(played_cards, player.cards)
        self.__is_blank(player)

    def __over_cards(self, player):
        over = False
        played_cards = card_hint(self.current_cards['cards'], player.cards)
        for key, value in played_cards.items():
            if value:
                over = True
                player.cards, self.current_cards['cards'] = post_cards(value[0], player.cards)
                break
        if over:
            pass
            # print(f"{player.name}管了: {self.current_cards['cards']}")
        else:
            pass
            # print(f"{player.name}管不起: Pass！")
        self.__is_blank(player)

    def __is_blank(self, player):
        p_index = self.players.index(player)
        if p_index == len(self.players) - 1:
            self.players[0].turn = True
        else:
            self.players[p_index + 1].turn = True

        if len(player.cards) == 0:
            if p_index == len(self.players) - 1:
                self.current_cards['player'] = self.players[0]
            else:
                self.current_cards['player'] = self.players[p_index + 1]
            if len(self.players) == 4:
                player.king = True
                player.win_times += 1
            self.players.remove(player)
