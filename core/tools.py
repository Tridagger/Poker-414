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

# def __card_to_num(cards, m=0, duplicate=True):
#     """
#     将扑克牌对象转换为数字对象，并过滤掉不大于m的值
#     :param cards: 扑克列表
#     :param m: 过滤参数
#     :param duplicate: 是否去重排序
#     :return: 数字列表
#     """
#     cl = sorted([__calc_card_level(card) for card in cards])
#     cl_after = list(filter(lambda x: x > m, cl))
#     if not duplicate:
#         cl_after = sorted(list(set(cl_after)))
#     return cl_after


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
    assert isinstance(cards, list)
    level_list = sorted([card.level for card in cards])
    assert 3 <= len(cards) == len(level_list)
    level_list = sorted([card.level for card in cards])
    print(level_list)
    # if len(cards) == (cards[-1] - cards[0] + 1):
    #     return True, 0
    # else:
    #     return False, 0
