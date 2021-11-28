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
from core.utils import C2S, Content
from core.player import CPlayer
from core.poker_tools import sort_card
from core.poker_tools import cards_hint, play_cards
import time


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c2s = C2S(client, ("127.0.0.1", 9999))
player = CPlayer()
t = Content(c2s)
t.mode = 'READY'
t.send()  # 先向服务器发一条消息，让服务器记录自己，准备开始游戏！

while True:
    data = c2s.load()  # 读取服务器发来的消息
    match data['MODE']:
        case 'INFORM':
            print(data['INFO'])

        case 'RECORD_ADDR':
            print(data['INFO'])
            player.addr = data['ADDR']
        case 'DISTRIBUTE_POKER':
            player.cards.append(data['CARD'][0])

        case 'STOP_DISTRIBUTE_POKER':  # 停止发牌，开始要朋友
            print(sort_card(player.cards))
            if Card('3', "红桃", 3) in player.cards:
                t.mode = "HEART3"
                t.cards = [random.choice([Card('A', suit, 14) for suit in PokerCard.suits])]
                t.send()

        case "HEART3":  # 公开红桃3信息，及要朋友信息
            print(data['INFO'])
            friend_card = data['CARD'][0]
            h3_addr = data['ADDR']
            if Card('3', "红桃", 3) in player.cards:
                t.mode = "PLAYCARD"
                t.cards = play_cards(player.cards)
                player.cards = list(set(player.cards)-set(t.cards))
                time.sleep(0.5)
                t.send()

        case "PLAYCARD":  # 有玩家出牌
            print(data['INFO'])
            if data['NEXT'] == player.addr:
                t.mode = "OVERCARD"
                t.cards = cards_hint(data['CARD'], player.cards)[0]
                player.cards = list(set(player.cards) - set(t.cards))
                time.sleep(0.5)
                t.send()

        case "OVERCARD":
            print(data['INFO'])