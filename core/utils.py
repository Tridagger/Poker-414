# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: utils.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/19
-------------------------------------------------
"""


def calc_card_level(card):
    """
    计算单牌的level值，用来比较牌面大小
    :param card: Card类型，单张牌
    :return: level值
    """
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


def is_solo(cards):
    """
    判断是否为单牌
    :param cards: List类型，扑克牌列表
    :return: True是单牌，最大牌点数   False不是单牌
    """
    assert isinstance(cards, list)
    cl = sorted([calc_card_level(card) for card in cards])
    return len(cl) == 1, max(cl)


def is_pair(cards):
    """
    判断是否为对牌
    :param cards: List类型，扑克牌列表
    :return: True：是对牌，最大牌点数   False不是对牌
    """
    assert isinstance(cards, list)
    cl = sorted([calc_card_level(card) for card in cards])
    if len(cl) == 2:
        if cl[0] == cl[1]:
            return True, max(cl)
        elif (18 in cl) and (19 in cl):
            return True, max(cl)
        else:
            return False, 0
    else:
        return False, 0


def is_chain(cards):
    """
    判断是否为顺子
    :param cards: List类型，扑克牌列表
    :return: True：是顺子，最大牌点数   False不是顺子
    """
    assert isinstance(cards, list)
    cl = sorted([calc_card_level(card) for card in cards])
    if 2 < len(cl) == (cl[-1] - cl[0] + 1) and len(cl) == len(set(cl)):
        return True, max(cl), len(cl)
    else:
        return False, 0


def is_pair_chain(cards):
    """
    判断是否为连对
    :param cards: List类型，扑克牌列表
    :return: True：是连对，最大牌点数   False不是连对
    """
    assert isinstance(cards, list)
    cl = sorted([calc_card_level(card) for card in cards])
    cs = sorted(list(set(cl)))  # 去重后的列表
    if len(cl) > 5 and len(cl) == len(cs) * 2:
        for i in range(int(len(cl) / 2)):
            if cl[i * 2] != cl[i * 2 + 1]:
                return False, 0
        if len(cs) == (cs[-1] - cs[0] + 1):
            return True, max(cs), len(cl)
        else:
            return False, 0
    else:
        return False, 0


def is_bomb(cards):
    """
    判断是否为炸弹
    :param cards: List类型，扑克牌列表
    :return: True：是炸弹，最大牌点数   False不是炸弹
    """
    assert isinstance(cards, list)
    cl = sorted([calc_card_level(card) for card in cards])
    if len(cl) == 3 and len(set(cl)) == 1:
        return True, max(cl)
    else:
        return False, 0


def is_missile(cards):
    """
    判断是否为导弹
    :param cards: List类型，扑克牌列表
    :return: True：是导弹，最大牌点数   False不是导弹
    """
    assert isinstance(cards, list)
    cl = sorted([calc_card_level(card) for card in cards])
    if len(cl) == 4 and len(set(cl)) == 1:
        return True, max(cl)
    else:
        return False, 0


def is_rocket(cards):
    """
    判断是否为火箭
    :param cards: List类型，扑克牌列表
    :return: 是火箭，最大牌点数   False不是火箭
    """
    assert isinstance(cards, list)
    cl = sorted([calc_card_level(card) for card in cards])
    if cl == [4, 4, 14]:
        return True, 99
    else:
        return False, 0


def hand_type(cards):
    """
    判断牌型
    :param cards: List类型，扑克牌列表
    :return: 字典：{"牌型": value, "等级": value, "牌数": value, "大小": value}
    """
    if is_solo(cards)[0]:
        return {"牌型": "单牌", "等级": 1, "牌数": 1, "大小": is_solo(cards)[1]}
    elif is_pair(cards)[0]:
        return {"牌型": "对牌", "等级": 1, "牌数": 2, "大小": is_pair(cards)[1]}
    elif is_bomb(cards)[0]:
        return {"牌型": "炸弹", "等级": 2, "牌数": 3, "大小": is_bomb(cards)[1]}
    elif is_missile(cards)[0]:
        return {"牌型": "导弹", "等级": 3, "牌数": 4, "大小": is_missile(cards)[1]}
    elif is_chain(cards)[0]:
        return {"牌型": "顺子", "等级": 1, "牌数": is_chain(cards)[2], "大小": is_chain(cards)[1]}
    elif is_pair_chain(cards)[0]:
        return {"牌型": "连对", "等级": 1, "牌数": is_pair_chain(cards)[2], "大小": is_pair_chain(cards)[1]}
    elif is_rocket(cards)[0]:
        return {"牌型": "火箭", "等级": 4, "牌数": 3, "大小": is_rocket(cards)[1]}
    else:
        return False


def card_compare(cards_1, cards_2):
    """
    牌型比较大小
    :param cards_1: 前出的牌
    :param cards_2: 后出的牌
    :return: cards_2比cards_1大则返回True，反之返回False
    """
    assert hand_type(cards_2)
    if hand_type(cards_2)['等级'] > hand_type(cards_1)['等级']:
        return True
    elif hand_type(cards_2)['牌型'] == hand_type(cards_1)['牌型'] \
            and hand_type(cards_2)['牌数'] == hand_type(cards_1)['牌数']:
        return hand_type(cards_2)['大小'] > hand_type(cards_1)['大小']
    else:
        return False


