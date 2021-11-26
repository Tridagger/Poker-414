# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: game.py
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
        self.players_out_list = []  # 跑出去的人
        self.all_cards = PokerCard().shuffle(2)
        self.left_cards = PokerCard()
        self.current_cards = {'cards': [], 'player': None}
        self.path = path
        self.log = False
        self.h3 = None
        self.friends_card = None
        self.h3_team = []
        self.not_h3_team = []
        self.base_point = 1
        self.answer_player = None
        self.top_dog = None  # 立棍
        self.publicised = False
        self.king = False  # 皇上
        self.stop = False  # 游戏结束标志位
        self.winner = None
        self.player_out = False

    def start_game(self, log=False):
        assert len(self.players) == 4  # 保证四个玩家
        if log:
            self.log = True
            with open(self.path, 'a+', encoding='GBK') as f:
                f.write("-"*100+"\n")
                f.write("4名玩家已就位，准备开始游戏！\n\n")

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
                self.h3_team.append(self.h3)
                break
        k = self.players.index(self.h3)
        self.players = self.players[k:] + self.players[:k]  # 红桃3持有者放到列表第一位
        if self.log:
            with open(self.path, 'a+', encoding='GBK') as f:
                f.write(f"红桃3在{self.h3.name}手中！\n")

        # 是否有人立棍
        player = random.choice(self.players)
        if (player.top_dog()) and (not self.top_dog):
            self.top_dog = player
            if self.top_dog == self.h3:
                self.h3_team = [player]
                self.not_h3_team = player.other_players
            else:
                self.not_h3_team = [player]
                self.h3_team = player.other_players
            self.publicise()
            self.base_point *= 5
            if self.log:
                with open(self.path, 'a+', encoding='GBK') as f:
                    f.write(f"{player}决定立棍！\n")

        # 要朋友
        if not self.top_dog:  # 判断是否有人立棍
            self.friends_card = self.h3.make_friends(), self.h3
            if self.log:
                with open(self.path, 'a+', encoding='GBK') as f:
                    f.write(f"{self.h3.name}要了：{self.friends_card[0]}\n\n")
            for player in self.players:
                player.set_friends_card(self.friends_card)
                if player.echo_flag:
                    self.h3_team.append(player)
                if player.find_flag:
                    self.not_h3_team.append(player)

        # 第一轮出牌
        self.first_turn()

        # 后续出牌
        while not self.stop:
            self.later_turn()
            self.borrow_light()  # 进入借光判定

        print(self.winner)

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

    def publicise(self):
        for player in self.players:
            player.get_info(self.h3_team, self.not_h3_team)
            self.publicised = True

    def turn_cards(self, player):
        self.current_cards = player.my_turn(**self.current_cards)
        self.left_cards = list(set(self.left_cards) - set(self.current_cards['cards']))
        if self.friends_card[0] in self.current_cards['cards']:
            if not self.publicised:
                self.publicise()
        if not player.cards:  # 玩家没手牌了
            if not self.king:
                self.king = player
            if self.top_dog:
                if player != self.top_dog:
                    self.winner = player.team
                    self.stop = True
            i = self.players.index(player)
            self.players_out_list.append(player)
            if player in self.h3_team:
                self.h3_team.remove(player)
            else:
                self.not_h3_team.remove(player)
            self.players.remove(player)
            self.players = self.players[i:] + self.players[:i]  # 重新排序玩家
            print((not self.h3_team) or (not self.not_h3_team))
            if (not self.h3_team) or (not self.not_h3_team):  # 判断游戏是否结束
                if not self.h3_team:
                    self.winner = self.h3.team
                else:
                    self.winner = self.h3.enemy
                self.stop = True
            self.player_out = True

    def borrow_light(self):  # 借光判定
        print('before', self.current_cards)
        table_cards = self.current_cards
        for player in self.players:
            self.turn_cards(player)
            if self.log:
                with open(self.path, 'a+', encoding='GBK') as f:
                    if player == self.current_cards['player']:
                        f.write(f"{player}出了{self.current_cards['cards']} 剩余：{len(player.cards)}张牌！\n")
                    else:
                        f.write(f"{player} 不要  剩余：{len(player.cards)}张牌！\n")
            print(player, self.current_cards)
        if table_cards == self.current_cards:
            print('借光判定')
            if self.publicised:  # 知道身份
                for player in self.players:
                    if self.players_out_list[-1] in player.friend:
                        print(player, '借光了！', player.friend)
                        self.current_cards['player'] = player
                        break
            elif self.players[0] == self.h3:
                print("你是红3，你不能借光！")
                self.current_cards['player'] = self.players[1]
            else:
                print(f"{self.players[0]}, 借光借光借光")
                self.current_cards['player'] = self.players[0]
        self.player_out = False

    def first_turn(self):
        if self.log:
            with open(self.path, 'a+', encoding='GBK') as f:
                f.write(f"\n第一轮出牌！\n")
        for player in self.players:
            if (player != self.h3) and (not self.top_dog):
                if (not self.answer_player) or (player not in self.answer_player.friend):
                    if self.answer_player != player.answer(self.answer_player):
                        self.answer_player = player.answer(self.answer_player)
                        self.base_point *= 2
                        if not self.publicised:
                            self.publicise()
                        if self.log:
                            with open(self.path, 'a+', encoding='GBK') as f:
                                f.write(f"{player}要求翻倍！\n")
            self.turn_cards(player)
            if self.log:
                with open(self.path, 'a+', encoding='GBK') as f:
                    if player == self.current_cards['player']:
                        f.write(f"{player}出了{self.current_cards['cards']} 剩余：{len(player.cards)}张牌！\n\n")
                    else:
                        f.write(f"{player} 不要  剩余：{len(player.cards)}张牌！\n\n")
        if self.log:
            with open(self.path, 'a+', encoding='GBK') as f:
                f.write(f"红桃3一伙：{self.h3_team}\n")
                f.write(f"其他一伙：{self.not_h3_team}\n")
                f.write(f"基础分值：{self.base_point}\n")

    def later_turn(self):
        if self.log:
            with open(self.path, 'a+', encoding='GBK') as f:
                f.write(f"\n后续出牌！\n")
        while not self.player_out:
            for player in self.players:
                self.turn_cards(player)
                if self.log:
                    with open(self.path, 'a+', encoding='GBK') as f:
                        if player == self.current_cards['player']:
                            f.write(f"{player}出了{self.current_cards['cards']} 剩余：{len(player.cards)}张牌！\n")
                        else:
                            f.write(f"{player} 不要  剩余：{len(player.cards)}张牌！\n")
                if self.player_out:
                    if self.log:
                        with open(self.path, 'a+', encoding='GBK') as f:
                            f.write(f"{self.players_out_list[-1]} 跑了！\n\n")
                    break
