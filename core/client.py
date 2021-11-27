# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: client.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/24
-------------------------------------------------
"""
import os
import sys
import socket
import pickle
import time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core.poker import Card
from core.utils import C2S

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c2s = C2S(client, ("127.0.0.1", 9999))

c2s.send("link to server")  # 先向服务器发一条消息，让服务器记录自己
cards = []
while True:
    data = c2s.load()
    print(data)
    if data == '4名玩家已到齐，开始游戏!':
        break

while True:  # 接收扑克牌
    data = c2s.load()
    print(data)
    if data == 'stop':
        break
    else:
        cards.append(data)

print(cards)
print(type(cards[0]))

while True:
    pass