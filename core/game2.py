# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: game2.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/25
-------------------------------------------------
"""
from core.poker import PokerCard
import random


class GameRound:
    def __init__(self, path):
        self.players = []
        self.all_cards = PokerCard().shuffle(2)
        self.current_cards = {'cards': [], 'player': None}
        self.path = path
        self.log = False
        self.h3 = None
        self.friends_card = None

    def start_game(self, log=False):
        assert len(self.players) == 4  # 保证四个玩家
        if log:
            self.log = True
            with open(self.path, 'a+', encoding='GBK') as f:
                f.write("-"*200+"\n")
                f.write("4名玩家已就位，准备开始游戏！\n")

        # 确定谁先抓牌
        have_king = False
        for player in self.players:
            player.clean_up()  # 清空手里的牌
            player.turn = False
            if player.king:
                have_king = True
        if not have_king:
            random.choice(self.players).king = True  # 随机一个人先抓牌
        if self.log:
            for player in self.players:
                if player.king and log:
                    with open(self.path, 'a+', encoding='GBK') as f:
                        f.write(f"{player.name} 先抓牌！\n")

        # 抓牌
        self.__distribute_cards()
        for player in self.players:  # 整理手牌
            player.sort_hand_cards()
        if self.log:
            for player in self.players:
                with open(self.path, 'a+', encoding='GBK') as f:
                    f.write(f"{player.name}有{len(player.cards)}张牌：{player.cards}\n")

        # 确定红桃3在谁手中
        for player in self.players:
            if player.have_h3():
                self.h3 = player
                break
        if self.log:
            with open(self.path, 'a+', encoding='GBK') as f:
                f.write(f"红桃3在{self.h3.name}手中！\n")

        # 要朋友
        self.friends_card = self.h3.make_friends(), self.h3
        if self.log:
            with open(self.path, 'a+', encoding='GBK') as f:
                f.write(f"{self.h3.name}要了：{self.friends_card}\n")
        for player in self.players:
            player.set_friends_card(self.friends_card)
            if self.log:
                with open(self.path, 'a+', encoding='GBK') as f:
                    f.write(f"{player.name}的同伙：{player.friend}，{player.name}的敌人：{player.enemy}\n")

        # 测试吱声
        for player in self.players:
            player.echo()
            player.find()

    def add_player(self, *args):
        self.players = list(args)
        for player in self.players:
            player.set_player(self.players)

    def __distribute_cards(self):
        while self.all_cards:
            for player in self.players:
                if self.all_cards and player.king:
                    for p in self.players:
                        p.king = True
                    assert self.all_cards
                    player.cards.append(self.all_cards.pop(0))