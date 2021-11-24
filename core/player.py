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


class Player:
    def __init__(self, name, robot=True):
        self.name = name  # 玩家的游戏名称
        self.cards = set()  # 玩家的手牌
        self.king = False  # 第一个出完牌的，成为皇上，主要决定下把先抓牌，他和下家都是 14 张牌，其他玩家 13 张牌
        self.ai = False  # 是否用 AI 出牌
        self.score = 0  # 玩家积分
        self.win_times = 0  # 游戏次数
        self.win_times = 0  # 获胜次数
        self.robot = robot  # 玩家是否是机器人
        self.friend = []  # 玩家的同伙

    def play_cards(self):
        pass

    def set_ai(self):
        assert self.robot
        self.ai = True

    def next_round(self):
        """
        下一轮游戏，初始化部分参数
        """
        self.cards = set()
        self.friend = []
