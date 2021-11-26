# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: poker.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/24
-------------------------------------------------
"""

import collections
import random


class Card(collections.namedtuple('Poker', ['rank', 'suit', 'level'])):  # 定义单张扑克牌
    def __repr__(self):
        if self.suit in ['红桃', '方片', '大']:
            # return f'\033[1;31m{self.suit}{self.rank}\033[0m'
            return f'{self.suit}{self.rank}'
        return f'{self.suit}{self.rank}'


class PokerCard:
    """
    扑克牌，54张，包含大小王
    """
    suits = ['红桃', '黑桃', '方片', '梅花']
    cards = {'14': [Card('A', suit, 14) for suit in suits],
             '16': [Card('2', suit, 16) for suit in suits],
             '3': [Card('3', suit, 3) for suit in suits],
             '4': [Card('4', suit, 4) for suit in suits],
             '5': [Card('5', suit, 5) for suit in suits],
             '6': [Card('6', suit, 6) for suit in suits],
             '7': [Card('7', suit, 7) for suit in suits],
             '8': [Card('8', suit, 8) for suit in suits],
             '9': [Card('9', suit, 9) for suit in suits],
             '10': [Card('10', suit, 10) for suit in suits],
             '11': [Card('J', suit, 11) for suit in suits],
             '12': [Card('Q', suit, 12) for suit in suits],
             '13': [Card('K', suit, 13) for suit in suits],
             '18': [Card('王', '小', 18)],
             '20': [Card('王', '大', 20)]
             }

    def __init__(self):
        # 列表生成式
        # 创建对象时自动赋值_cards
        self._cards = [c for card in self.cards.values() for c in card]

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
        return self._cards
