# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: player.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/19
-------------------------------------------------
"""


class Player:
    def __init__(self, name, robot=True):
        self.name = name
        self.cards = []
        self.king = False  # 第一个出完牌的，成为皇上
        self.robot = robot
        self.score = 0
        self.win_times = 0  # 获胜次数
        self.turn = False

    def clean_up(self):
        self.cards = []

    def draw_cards(self):
        pass

    def play_cards(self):
        pass

