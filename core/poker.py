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
    扑克牌，54张，包含大小王
    """

    # 列表生成式，牌大小
    ranks = list(str(n) for n in range(2, 11)) + ['J', 'Q', 'K', 'A']
    # 牌花色
    suits = ['红桃', '黑桃', '方片', '梅花']

    def __init__(self):
        # 列表生成式
        # 创建对象时自动赋值_cards
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks] \
                      + [Card('black', 'Joker'), Card('red', 'Joker')]

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


def calc_card_level(card):
    assert isinstance(card, tuple)
    card_dict = {
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
        '2': 16,
        'red': 18,
        'black': 19
    }
    if str(card[0]) in card_dict:
        return card_dict[str(card[0])]
    else:
        return int(card[0])


#  判断是否为单牌
def is_solo(cards):
    assert isinstance(cards, list)
    cl = sorted([calc_card_level(card) for card in cards])
    if len(cl) == 1:
        return True
    else:
        return False


#  判断是否为对牌
def is_pair(cards):
    assert isinstance(cards, list)
    cl = sorted([calc_card_level(card) for card in cards])
    if len(cl) == 2:
        if cl[0] == cl[1]:
            return True
        elif (18 in cl) and (19 in cl):
            return True
        else:
            return False
    else:
        return False


#  判断是否为单龙
def is_chain(cards):
    assert isinstance(cards, list)
    cl = sorted([calc_card_level(card) for card in cards])
    if 2 < len(cl) == (cl[-1] - cl[0] + 1) and len(cl) == len(set(cl)):
        return True
    else:
        return False


#  判断是否为双龙
def is_pair_chain(cards):
    assert isinstance(cards, list)
    cl = sorted([calc_card_level(card) for card in cards])
    cs = sorted(list(set(cl)))  # 去重后的列表
    if len(cl) > 5 and len(cl) == len(cs) * 2:
        for i in range(int(len(cl) / 2)):
            if cl[i * 2] != cl[i * 2 + 1]:
                return False
        if len(cs) == (cs[-1] - cs[0] + 1):
            return True
        else:
            return False
    else:
        return False


#  判断是否为炸弹
def is_bomb(cards):
    assert isinstance(cards, list)
    cl = sorted([calc_card_level(card) for card in cards])
    if len(cl) == 3 and len(set(cl)) == 1:
        return True
    else:
        return False


#  判断是否为导弹
def is_missile(cards):
    assert isinstance(cards, list)
    cl = sorted([calc_card_level(card) for card in cards])
    if len(cl) == 4 and len(set(cl)) == 1:
        return True
    else:
        return False


#  判断是否为火箭
def is_rocket(cards):
    assert isinstance(cards, list)
    cl = sorted([calc_card_level(card) for card in cards])
    if cl == [4, 4, 14]:
        return True
    else:
        return False


# 判断牌型
def whats_hand(cards):
    if is_solo(cards):

        return "单牌"
    elif is_pair(cards):
        return "对牌"
    elif is_bomb(cards):
        return "炸弹"
    elif is_missile(cards):
        return "导弹"
    elif is_chain(cards):
        return "顺子"
    elif is_pair_chain(cards):
        return "连对"
    elif is_rocket(cards):
        return "火箭"
    else:
        return "杂牌"
