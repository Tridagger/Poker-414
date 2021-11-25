# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: player.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/24
-------------------------------------------------
"""
from core import tools
from core import poker
import random


class Player:
    def __init__(self, name, robot=True):
        self.other_players = []
        self.name = name  # 玩家的游戏名称
        self.cards = []  # 玩家的手牌
        self.king = False  # 第一个出完牌的，成为皇上，主要决定下把先抓牌，他和下家都是 14 张牌，其他玩家 13 张牌
        self.ai = False  # 是否用 AI 出牌
        self.score = 0  # 玩家积分
        self.win_times = 0  # 游戏次数
        self.win_times = 0  # 获胜次数
        self.robot = robot  # 玩家是否是机器人
        self.friend = []  # 玩家的同伙
        self.enemy = []  # 玩家的敌人
        self.h3 = False
        self.friends_card = None
        self.echo_flag = False
        self.find_flag = False

    def play_cards(self):
        assert self.cards
        out_cards = tools.play_cards(self.cards)
        self.cards = list(set(self.cards) - set(out_cards))
        return out_cards

    def over_cards(self, cards):
        assert self.cards
        out_cards = tools.cards_hint(cards, self.cards)
        if out_cards:
            self.cards = list(set(self.cards) - set(out_cards[0]))
        return out_cards

    def clean_up(self):
        self.cards = []

    def set_ai(self):
        assert self.robot
        self.ai = True

    def next_round(self):
        """
        下一轮游戏，初始化部分参数
        """
        self.cards = []
        self.friend = []
        self.h3 = False
        self.friends_card = None

    def have_h3(self):
        self.h3 = poker.Card('3', '红桃', 3) in self.cards
        return self.h3

    def sort_hand_cards(self):
        self.cards = tools.sort_card(self.cards)

    def make_friends(self):
        if random.randint(1, 1) == 1:
            friends_card = random.choice(poker.PokerCard.cards['14'])
        else:
            friends_card = random.choice(list(set(poker.PokerCard.cards['14']) - set(self.cards)))
        return friends_card

    def set_friends_card(self, friends_card):
        self.friends_card = friends_card
        if self != self.friends_card[1]:
            if self.friends_card[0] in self.cards:
                self.friend.append(self.friends_card[1])
                self.echo_flag = True
            else:
                self.enemy.append(self.friends_card[1])
                self.find_flag = True
        else:
            if self.friends_card[0] in self.cards:
                self.enemy = self.other_players

    def set_player(self, players):
        self.other_players = list(players)
        self.other_players.remove(self)

    def __repr__(self):
        return self.name

    def echo(self, team_info):  # 吱声
        pass

    def find(self, team_info):  # 寻找
        pass

