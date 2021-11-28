# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: player.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/27
-------------------------------------------------
"""


class SPlayer:
    def __init__(self, name, addr):
        self.name = "玩家"+name
        self.addr = addr

    def __repr__(self):
        return self.name


class CPlayer:
    def __init__(self):
        self.addr = None
        self.cards = []
        self.friends = []
        self.enemy = []
        self.h3_owner = None

