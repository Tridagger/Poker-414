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
import random
import sys
import socket
import time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core.poker import Card, PokerCard
from core.utils import C2S
from core.player import CPlayer
from core.poker_tools import sort_card

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c2s = C2S(client, ("127.0.0.1", 9999))
player = CPlayer()

c2s.send({"mode": "ready"})  # 先向服务器发一条消息，让服务器记录自己
while True:
    data = c2s.load()
    print(data['inform'])
    if data['inform'] == '4名玩家已到齐，开始游戏!':
        break

while True:  # 接收扑克牌
    data = c2s.load()
    print(data)
    if data['inform'] == 'stop':
        break
    else:
        player.cards.append(data['cards'])
        print(data['cards'])

print(sort_card(player.cards))

if Card('3', "红桃", 3) in player.cards:
    c2s.send({"mode": "IamH3"})
    data = c2s.load()
    print(data)
    time.sleep(1)
    card = random.choice([Card('A', suit, 14) for suit in PokerCard.suits])
    c2s.send({"mode": "make friend", "cards": card})
else:
    data = c2s.load()
    print(data)

data = c2s.load()
print(data)

while True:
    pass
