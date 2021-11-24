# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: tools.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/24
-------------------------------------------------
"""


def remove_duplicate_card(cards):
    new_cards = []
    for card in cards:
        if card.level not in [c.level for c in new_cards]:
            new_cards.append(card)
    return sorted(new_cards, key=lambda cd: cd.level)


def is_solo(cards):
    """
    判断是否为单牌
    :param cards: list类型，扑克牌列表
    :return: True是单牌，最小牌点数   False不是单牌
    """
    assert isinstance(cards, list)
    return len(cards) == 1, cards[0].level


def is_pair(cards):
    """
    判断是否为对牌
    :param cards: List类型，扑克牌列表
    :return: True：是对牌，最小牌点数   False不是对牌
    """
    assert isinstance(cards, list)
    assert len(cards) == 2
    return cards[0].rank == cards[1].rank, cards[0].level


def is_chain(cards):
    """
    判断是否为顺子
    :param cards: List类型，扑克牌列表
    :return: True：是顺子，最小牌点数   False不是顺子
    """
    assert isinstance(cards, list) and 3 <= len(cards) == len(remove_duplicate_card(cards))
    return len(cards) == (cards[-1].level - cards[0].level + 1), cards[0].level, len(cards)


def is_dual_chain(cards):
    assert isinstance(cards, list)
    cl = sorted(cards, key=lambda cd: cd.level)
    cs = remove_duplicate_card(cards)
    assert len(cards) >= 6 and len(cards) == len(cs) * 2
    for i in range(len(cs)):
        assert cl[i * 2].level == cl[i * 2 + 1].level
    return len(cs) == (cs[-1].level - cs[0].level + 1), len(cards), cs[0].level


def is_bomb(cards):
    assert isinstance(cards, list)
    return len(cards) == 3 and len(remove_duplicate_card(cards)) == 1, cards[0].level, 3


def is_missile(cards):
    assert isinstance(cards, list)
    return len(cards) == 4 and len(remove_duplicate_card(cards)) == 1, cards[0].level, 4


def is_rocket(cards):
    assert isinstance(cards, list)
    assert len(cards) == 3
    cl = sorted([c.level for c in cards])
    return cl == [4, 4, 14], 99, 3
