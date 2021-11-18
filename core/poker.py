# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: poker.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/18
-------------------------------------------------
"""

import collections
import random

Card = collections.namedtuple('扑克牌', ['大小', '花色'])  # 定义单张扑克牌


class PokerCard:
    """
    生成一套扑克牌，54张，包含大小王
    """

    # 列表生成式，牌大小
    ranks = list(str(n) for n in range(2, 11)) + ['J', 'Q', 'K', 'A']
    # 牌花色
    suits = ['红桃', '黑桃', '方片', '梅花']

    def __init__(self):
        # 列表生成式
        # 创建对象时自动赋值_cards
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks] \
                      + [Card('15', '小王'), Card('16', '大王')]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]

    def shuffle(self, n=2):
        """
        洗牌，将扑克牌打乱
        :param n: 洗牌次数
        :return: "洗牌结束"
        """
        for i in range(n):
            random.shuffle(self._cards)
        return "洗牌结束"
