# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: server.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/24
-------------------------------------------------
"""
import socketserver
import time
from core.game import GameRound
import pickle
from core.utils import S2C, Content

game = GameRound()


class PokerServer(socketserver.BaseRequestHandler):
    """
    必须继承socketserver.BaseRequestHandler类
    """

    def handle(self):
        data, file = self.request
        s2c = S2C(file, game.static_players)
        t = Content(s2c)
        data = pickle.loads(data)
        match data["mode"]:
            case "ready":
                game.add_player(self.client_address)
                t.inform = f'当前有{len(game.players)}名玩家，' \
                           f'您是【{game.addr_to_player(self.client_address).name}】，请等待！'
                t.send(self.client_address)

                if len(game.players) == 4:
                    time.sleep(1)
                    t.inform = '4名玩家已到齐，开始游戏!'
                    t.send_all()
                    while game.round_cards:
                        for player in game.players:
                            if game.round_cards:
                                t.cards = game.round_cards.pop()
                                time.sleep(0.05)
                                t.send(player.addr)
                    t.inform = 'stop'
                    t.send_all()

            case "IamH3":
                player = game.addr_to_player(self.client_address)
                game.circle(player)
                s2c.send_all(f'红桃3在【{player.name}】手中，等待【{player.name}】要朋友！')
                print(game.players)

            case "make friend":
                s2c.send_all(data["cards"])
