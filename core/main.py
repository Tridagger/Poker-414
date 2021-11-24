# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: main.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/18
-------------------------------------------------
"""
import time
import socketserver
from core.game import GameRound
from core.player import Player
from core.poker import *
from core.server import game_server
from threading import Thread


# 运行程序
def run(debug=False):
    if debug:
        pass
    game_server.serve_forever()


