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

        match data["MODE"]:
            case "READY":
                game.add_player(self.client_address)

                t.mode = "RECORD_ADDR"
                t.addr = self.client_address
                t.inform = f'当前有{len(game.players)}名玩家，' \
                           f'您是【{game.addr_to_player(self.client_address).name}】，请等待！'
                t.send(self.client_address)

                if len(game.players) == 4:
                    time.sleep(1)

                    t.mode = "INFORM"
                    t.inform = '4名玩家已到齐，开始游戏!'
                    t.send_all()

                    while game.round_cards:
                        for player in game.players:
                            if game.round_cards:
                                t.mode = 'DISTRIBUTE_POKER'  # 发牌
                                t.cards = [game.round_cards.pop()]
                                time.sleep(0.05)
                                t.send(player.addr)

                    t.mode = 'STOP_DISTRIBUTE_POKER'  # 停止发牌
                    t.inform = '发牌结束，请拥有【红桃3】的玩家要朋友！'
                    t.send_all()

            case "HEART3":
                player = game.addr_to_player(self.client_address)
                game.circle(player)  # 调整玩家顺序
                t.mode = "HEART3"
                t.inform = f"红桃3在【{player.name}】手中，要了【{data['CARD'][0]}】"
                t.cards = data['CARD']
                t.addr = self.client_address
                t.send_all()

            case "PLAYCARD":
                player = game.addr_to_player(self.client_address)
                t.mode = "PLAYCARD"
                t.inform = f"【{player.name}】出了 {data['CARD']}"
                t.cards = data['CARD']
                t.addr = self.client_address
                t.next = game.next(player)
                t.send_all()

            case "OVERCARD":
                player = game.addr_to_player(self.client_address)
                t.mode = "OVERCARD"
                t.inform = f"【{player.name}】管了 {data['CARD']}"
                t.cards = data['CARD']
                t.addr = self.client_address
                t.next = game.next(player)
                t.send_all()