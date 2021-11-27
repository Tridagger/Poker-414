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
from core.utils import S2C

game = GameRound()


class PokerServer(socketserver.BaseRequestHandler):
    """
    必须继承socketserver.BaseRequestHandler类
    """

    def handle(self):
        """
        必须实现这个方法！
        :return:
        """
        data, file = self.request
        s2c = S2C(file, game.static_players)
        match pickle.loads(data):
            case "link to server":
                game.add_player(self.client_address)
                s2c.send(f'当前有{len(game.players)}名玩家，请等待！', self.client_address)

                if len(game.players) == 4:
                    time.sleep(1)
                    s2c.send_all('4名玩家已到齐，开始游戏!')

                    while game.round_cards:
                        for player in game.players:
                            if game.round_cards:
                                player_hand_cards = game.round_cards.pop()
                                time.sleep(0.02)
                                s2c.send(player_hand_cards, player)
                    for player in game.players:
                        s2c.send('stop', player)
