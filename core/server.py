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
game = GameRound()
import pickle


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

        if data == b"link to server":
            game.add_player(self.client_address)
            file.sendto(f'当前有{len(game.players)}名玩家，请等待！'.encode(), self.client_address)

        if len(game.players) == 4:
            time.sleep(1)
            for addr in game.players:
                file.sendto('4名玩家已到齐，开始游戏!'.encode(), addr)

            while game.round_cards:
                for player_addr in game.players:
                    if game.round_cards:
                        player_hand_cards = game.round_cards.pop()
                        time.sleep(0.1)
                        file.sendto(str(player_hand_cards).encode(), player_addr)
            for addr in game.players:
                file.sendto('stop'.encode(), addr)

