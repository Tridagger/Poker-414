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
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.poker import Card

c = Card(1, 1, 1)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"link to server", ("127.0.0.1", 9999))  # 先向服务器发一条消息，让服务器记录自己
cards = []
while True:
    data, _ = client.recvfrom(1024)
    print(data.decode())
    if data == '4名玩家已到齐，开始游戏!'.encode():
        break

while True:  # 接收扑克牌
    data, _ = client.recvfrom(1024)
    if data == 'stop'.encode():
        break
    else:
        cards.append(pickle.loads(data))

print(cards)

while True:
    pass