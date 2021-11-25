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
from core.poker import PokerCard, Card
from core.utils import *
import time
import os
import logging


class GameRound:
    def __init__(self, path):
        self.static_players = []
        self.players = []
        self.all_cards = PokerCard().shuffle(2)  # 生成一副新的扑克牌, 洗两次牌
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
        have_king = False
        for player in self.players:
            if player.king:
                have_king = True
        if not have_king:
            random.choice(self.players).king = True  # 随机一个人先抓牌
        for player in self.players:
            player.clean_up()  # 清空手里的牌
            player.turn = False
            if player.king and log:
                with open(self.path, 'a+', encoding='utf-8') as f:
                    f.write(f"{player.name} 先抓牌！\n")
        self.__distribute_cards()  # 发牌
        if self.log:
            for player in self.players:
                with open(self.path, 'a+', encoding='utf-8') as f:
                    f.write(f"{player.name}有{len(player.cards)}张牌：{player.cards}\n")

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
        if self.log:
            with open(self.path, 'a+', encoding='utf-8') as f:
                f.write(f"红桃3在{h3.name}手中！{h3.name}先出牌！\n\n")
        while len(self.players) > 1:
            for player in self.players:
                with open(self.path, 'a+', encoding='utf-8') as f:
                    f.write(f"牌堆上是{self.current_cards['player'].name}的牌\n")
                if player.turn:
                    if player == self.current_cards['player']:
                        self.__play_cards(player)
                    else:
                        self.__over_cards(player)
        if self.log:
            with open(self.path, 'a+', encoding='utf-8') as f:
                f.write(f"{self.players[0].name}成为了娘娘！！！游戏结束！\n")
                f.write("-" * 200 + "\n\n\n\n\n\n\n")

    def __play_cards(self, player):
        """
        随机出牌 玩家的手牌减少，出的牌更新到 self.current_cards 中
        :param player: 玩家对象
        :return: None
        """
        self.current_cards['cards'] = []
        self.current_cards['player'] = player
        if player.ai:
            played_cards = random_play_card(player.cards, ai=True)
        else:
            played_cards = random_play_card(player.cards)
        player.cards, self.current_cards['cards'] = post_cards(played_cards, player.cards)
        if self.log:
            with open(self.path, 'a+', encoding='utf-8') as f:
                f.write(f"{player.name}出了 {self.current_cards['cards']}\n")
                f.write(f"{player.name}手里还剩 {player.cards}\n\n")

        self.__is_blank(player)

    def __over_cards(self, player):
        over = False
        if player.ai:
            played_cards = card_hint(self.current_cards['cards'], player.cards, ai=True)
        else:
            played_cards = card_hint(self.current_cards['cards'], player.cards)
        for key, value in played_cards.items():
            if value:
                over = True
                player.cards, self.current_cards['cards'] = post_cards(value[0], player.cards)
                self.current_cards['player'] = player
                break

        # 记录到文件
        if over and self.log:
            with open(self.path, 'a+', encoding='utf-8') as f:
                f.write(f"{player.name}管了: {self.current_cards['cards']}\n")
                f.write(f"{player.name}手里还剩 {player.cards}\n\n")
        else:
            with open(self.path, 'a+', encoding='utf-8') as f:
                f.write(f"{player.name} 要不起！\n")
                f.write(f"{player.name}手里还剩 {player.cards}\n\n")
        self.__is_blank(player)

    def __is_blank(self, player):
        p_index = self.players.index(player)
        if p_index == len(self.players) - 1:
            self.players[0].turn = True
        else:
            self.players[p_index + 1].turn = True

        if len(player.cards) == 0:
            if self.log:
                with open(self.path, 'a+', encoding='utf-8') as f:
                    f.write(f"{player.name} 没牌了\n\n")
            if p_index == len(self.players) - 1:
                self.current_cards['player'] = self.players[0]
            else:
                self.current_cards['player'] = self.players[p_index + 1]
            if len(self.players) == 4:
                if self.log:
                    with open(self.path, 'a+', encoding='utf-8') as f:
                        f.write(f"{player.name} 成为了皇上！\n\n")
                for p in self.players:
                    p.king = False
                player.king = True
                player.win_times += 1
            self.players.remove(player)