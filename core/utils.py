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
import random
from collections import Counter


def __calc_card_level(card):
    """
    计算单张牌的level值，用来比较牌面大小
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
        'black': 18,
        'red': 19
    }
    if str(card[0]) in card_dict:
        return card_dict[str(card[0])]
    else:
        return int(card[0])


def __card_to_num(cards, m=0, duplicate=True):
    """
    将扑克牌对象转换为数字对象，并过滤掉不大于m的值
    :param cards: 扑克列表
    :param m: 过滤参数
    :param duplicate: 是否去重排序
    :return: 数字列表
    """
    cl = sorted([__calc_card_level(card) for card in cards])
    cl_after = list(filter(lambda x: x > m, cl))
    if not duplicate:
        cl_after = sorted(list(set(cl_after)))
    return cl_after


def __is_solo(cards):
    """
    判断是否为单牌
    :param cards: List类型，扑克牌列表
    :return: True是单牌，最小牌点数   False不是单牌
    """
    assert isinstance(cards, list)
    cl = __card_to_num(cards)
    return len(cl) == 1, min(cl)


def __is_pair(cards):
    """
    判断是否为对牌
    :param cards: List类型，扑克牌列表
    :return: True：是对牌，最小牌点数   False不是对牌
    """
    assert isinstance(cards, list)
    cl = __card_to_num(cards)
    if len(cl) == 2:
        if cl[0] == cl[1]:
            return True, min(cl)
        elif (18 in cl) and (19 in cl):
            return True, min(cl)
        else:
            return False, 0
    else:
        return False, 0


def __is_chain(cards):
    """
    判断是否为顺子
    :param cards: List类型，扑克牌列表
    :return: True：是顺子，最小牌点数   False不是顺子
    """
    assert isinstance(cards, list)
    cl = __card_to_num(cards)
    if 2 < len(cl) == (cl[-1] - cl[0] + 1) and len(cl) == len(set(cl)):
        return True, min(cl), len(cl)
    else:
        return False, 0


def __is_pair_chain(cards):
    """
    判断是否为连对
    :param cards: List类型，扑克牌列表
    :return: True：是连对，最小牌点数   False不是连对
    """
    assert isinstance(cards, list)
    cl = __card_to_num(cards)
    cs = sorted(list(set(cl)))  # 去重后的列表
    if len(cl) > 5 and len(cl) == len(cs) * 2:
        for i in range(int(len(cl) / 2)):
            if cl[i * 2] != cl[i * 2 + 1]:
                return False, 0
        if len(cs) == (cs[-1] - cs[0] + 1):
            return True, min(cs), len(cl)
        else:
            return False, 0
    else:
        return False, 0


def __is_bomb(cards):
    """
    判断是否为炸弹
    :param cards: List类型，扑克牌列表
    :return: True：是炸弹，最小牌点数   False不是炸弹
    """
    assert isinstance(cards, list)
    cl = __card_to_num(cards)
    if len(cl) == 3 and len(set(cl)) == 1:
        return True, min(cl)
    else:
        return False, 0


def __is_missile(cards):
    """
    判断是否为导弹
    :param cards: List类型，扑克牌列表
    :return: True：是导弹，最小牌点数   False不是导弹
    """
    assert isinstance(cards, list)
    cl = __card_to_num(cards)
    if len(cl) == 4 and len(set(cl)) == 1:
        return True, min(cl)
    else:
        return False, 0


def __is_rocket(cards):
    """
    判断是否为火箭
    :param cards: List类型，扑克牌列表
    :return: 是火箭，最大牌点数   False不是火箭
    """
    assert isinstance(cards, list)
    cl = __card_to_num(cards)
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
    if __is_solo(cards)[0]:
        return {"牌型": "单牌", "等级": 1, "牌数": 1, "大小": __is_solo(cards)[1]}
    elif __is_pair(cards)[0]:
        return {"牌型": "对牌", "等级": 1, "牌数": 2, "大小": __is_pair(cards)[1]}
    elif __is_bomb(cards)[0]:
        return {"牌型": "炸弹", "等级": 2, "牌数": 3, "大小": __is_bomb(cards)[1]}
    elif __is_missile(cards)[0]:
        return {"牌型": "导弹", "等级": 3, "牌数": 4, "大小": __is_missile(cards)[1]}
    elif __is_chain(cards)[0]:
        return {"牌型": "顺子", "等级": 1, "牌数": __is_chain(cards)[2], "大小": __is_chain(cards)[1]}
    elif __is_pair_chain(cards)[0]:
        return {"牌型": "连对", "等级": 1, "牌数": __is_pair_chain(cards)[2], "大小": __is_pair_chain(cards)[1]}
    elif __is_rocket(cards)[0]:
        return {"牌型": "火箭", "等级": 4, "牌数": 3, "大小": __is_rocket(cards)[1]}
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


def __have_rocket(cards):
    """
    扑克列表中是否含有火箭
    :param cards: list: 扑克列表
    :return: 符合要求的列表
    """
    cl = __card_to_num(cards)
    cnt = Counter(cl)
    hcl = []
    if cnt[4] >= 2 and cnt[14] >= 1:
        hcl.append([4, 4, 14])
    return hcl


def __have_missile(cards, m=2):
    """
    扑克列表中是否含有大于 m 导弹
    :param cards: list: 扑克列表
    :param m: 最小值
    :return: 符合要求的列表
    """
    cl = __card_to_num(cards, m)
    cnt = Counter(cl)
    hcl = []
    for c in cnt:
        if cnt[c] == 4:
            hcl.append([c, c, c, c])
    return hcl


def __have_bomb(cards, m=2):
    """
    扑克列表中是否含有大于 m 炸弹
    :param cards: list: 扑克列表
    :param m: 最小值
    :return: 符合要求的列表
    """
    cl = __card_to_num(cards, m)
    cnt = Counter(cl)
    hcl = []
    for c in cnt:
        if cnt[c] >= 3:
            hcl.append([c, c, c])
    return hcl


def __have_chain(cards, m=2, n=3):
    """
    扑克列表中是否含大于 m 的 n 连顺子
    :param cards: list: 扑克列表
    :param m: 最小值
    :param n: 牌数
    :return: 符合要求的列表
    """
    hcl = []
    cl = __card_to_num(cards, m, duplicate=False)
    for i in [16, 18, 19]:
        if i in cl:
            cl.remove(i)
    for i in range(len(cl)-n+1):
        cl_piece = cl[i: i+n]
        if len(cl_piece) == (cl_piece[-1] - cl_piece[0] + 1):
            hcl.append(cl_piece)
    return hcl


def __have_pair_chain(cards, m=2, n=6):
    """
    扑克列表中是否含大于 m 的 n 连对
    :param cards: list: 扑克列表
    :param m: 最小值
    :param n: 牌数
    :return: 符合要求的列表
    """
    assert n in [6, 8, 10, 12, 14]
    cl = __card_to_num(cards, m)
    cnt = Counter(cl)
    hcl = []
    s = int(n/2)
    cl_copy = []
    for item in cl:
        if cnt[item] >= 2:
            cl_copy.append(item)
    cl_set = sorted(list(set(cl_copy)))
    if 16 in cl_set:
        cl_set.remove(16)
    for i in range(len(cl_set)-s+1):
        cl_piece = cl_set[i: i+s]
        if len(cl_piece) == (cl_piece[-1] - cl_piece[0] + 1):
            cl_pieces = []
            for j in cl_piece:
                cl_pieces.append(j)
                cl_pieces.append(j)
            hcl.append(cl_pieces)
    return hcl


def __have_pair(cards, m=2):
    """
    扑克列表中是否含大于 m 的对牌
    :param cards: list: 扑克列表
    :param m: 最小值
    :return: 符合要求的列表
    """
    cl = __card_to_num(cards, m)
    cnt = Counter(cl)
    hcl = []
    cl_copy = []
    for item in cl:
        if cnt[item] >= 2:
            cl_copy.append(item)
    hcs = sorted(list(set(cl_copy)))
    for i in hcs:
        hcl.append([i, i])
    if 18 in cl and 19 in cl:  # 判断牌里是否有对王
        hcl.append([18, 19])
    return hcl


def __use_bomb(card_dict, cards):
    """
    把所有炸弹，导弹，火箭添加进字典
    :param card_dict: 提示字典
    :param cards: 手牌
    :return: 添加好的字典
    """
    card_dict['炸弹'] = __have_bomb(cards)
    card_dict['导弹'] = __have_missile(cards)
    card_dict['火箭'] = __have_rocket(cards)
    return card_dict


def card_hint(card_1, card_2):
    """
    出牌提示
    :param card_1: 被管的牌
    :param card_2: 手牌
    :return: dict 所有出牌方法的集合
    """
    ht = hand_type(card_1)
    card_dict = {
        '单牌': [],
        '对牌': [],
        '顺子': [],
        '连对': [],
        '炸弹': [],
        '导弹': [],
        '火箭': []
    }
    match ht['等级']:
        case 1:
            match ht['牌型']:
                case '单牌':
                    sl = __card_to_num(card_2, ht['大小'], duplicate=False)  # 把能管上的单牌加入字典
                    for i in sl:
                        card_dict['单牌'].append([i])  # 封装成列表 保持统一

                case '对牌':
                    card_dict['对牌'] = __have_pair(card_2, ht['大小'])  # 把能管上的对牌加入字典

                case '顺子':
                    card_dict['顺子'] = __have_chain(card_2, ht['大小'], ht['牌数'])  # 把能管上的顺子加入字典

                case '连对':
                    card_dict['连对'] = __have_pair_chain(card_2, ht['大小'], ht['牌数'])  # 把能管上的连对加入字典
            return __use_bomb(card_dict, card_2)  # 返回加入炸弹
        case 2:
            card_dict['炸弹'] = __have_bomb(card_2, ht['大小'])  # 把能管上的炸弹加入字典
            card_dict['导弹'] = __have_missile(card_2)  # 把所有导弹加入字典
            card_dict['火箭'] = __have_rocket(card_2)  # 把火箭加入字典
            return card_dict

        case 3:
            card_dict['导弹'] = __have_missile(card_2, ht['大小'])  # 把能管上的导弹加入列表
            card_dict['火箭'] = __have_rocket(card_2)  # 把火箭加入列表
            return card_dict

        case 4:
            return card_dict
        case _:
            return None


def random_play_card(cards, ai=False):
    card_list = []
    match ai:
        case True:
            pass
        case False:
            if __have_pair_chain(cards):
                card_list.append(__have_pair_chain(cards)[0])
                return card_list
            if __have_chain(cards):
                card_list.append(__have_chain(cards)[0])
                return card_list
            if __have_pair(cards):
                if __have_pair(cards)[0][0] == __card_to_num(cards, duplicate=True)[0]:
                    card_list.append(__have_pair(cards)[0])
                    return card_list
            card_list.append((__card_to_num(cards, duplicate=True)[0]))

    return card_list
