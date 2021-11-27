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


class Player:
    def __init__(self, name):
        self.name = name
        pass

    def __repr__(self):
        return f"Client - {self.name}"

    def ready(self):
        pass