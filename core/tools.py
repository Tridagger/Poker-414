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
from collections import Counter
from core.poker import PokerCard


def sort_card(cards):
    if not cards:
        return []
    if isinstance(cards[0], list):
        return sorted(cards, key=lambda cd: cd[0].level)
    else:
        return sorted(cards, key=lambda cd: cd.level)


def remove_duplicate_card(cards, m=2):
    new_cards = []
    for card in cards:
        if card.level > m and card.level not in [c.level for c in new_cards]:
            new_cards.append(card)
    return sort_card(new_cards)


def is_solo(cards):
    assert isinstance(cards, list)
    return len(cards) == 1, cards[0].level


def is_pair(cards):
    assert isinstance(cards, list)
    if len(cards) == 2:
        return cards[0].rank == cards[1].rank, cards[0].level, 2
    else:
        return False, 0, 0


def is_chain(cards):
    assert isinstance(cards, list)
    rd_cards = remove_duplicate_card(cards)
    if 3 <= len(cards) == len(rd_cards):
        return len(rd_cards) == (rd_cards[-1].level - rd_cards[0].level + 1), rd_cards[0].level, len(rd_cards)
    else:
        return False, 0, 0


def is_dual_chain(cards):
    assert isinstance(cards, list)
    cl = sorted(cards, key=lambda cd: cd.level)
    cs = remove_duplicate_card(cards)
    if len(cards) >= 6 and len(cards) == len(cs) * 2:
        for i in range(len(cs)):
            if cl[i * 2].level != cl[i * 2 + 1].level:
                return False, 0, 0
        return len(cs) == (cs[-1].level - cs[0].level + 1), cs[0].level, len(cards)
    else:
        return False, 0, 0


def is_bomb(cards):
    assert isinstance(cards, list)
    return len(cards) == 3 and len(remove_duplicate_card(cards)) == 1, cards[0].level, 3


def is_missile(cards):
    assert isinstance(cards, list)
    return len(cards) == 4 and len(remove_duplicate_card(cards)) == 1, cards[0].level, 4


def is_rocket(cards):
    assert isinstance(cards, list)
    cl = sorted([c.level for c in cards])
    return len(cards) == 3 and cl == [4, 4, 14], 99, 3


def cards_type(cards):
    assert isinstance(cards, list)
    if is_solo(cards)[0]:
        return {"??????": "??????", "??????": 1, "??????": 1, "??????": is_solo(cards)[1]}
    elif is_pair(cards)[0]:
        return {"??????": "??????", "??????": 1, "??????": 2, "??????": is_pair(cards)[1]}
    elif is_bomb(cards)[0]:
        return {"??????": "??????", "??????": 2, "??????": 3, "??????": is_bomb(cards)[1]}
    elif is_missile(cards)[0]:
        return {"??????": "??????", "??????": 3, "??????": 4, "??????": is_missile(cards)[1]}
    elif is_chain(cards)[0]:
        return {"??????": "??????", "??????": 1, "??????": is_chain(cards)[2], "??????": is_chain(cards)[1]}
    elif is_dual_chain(cards)[0]:
        return {"??????": "??????", "??????": 1, "??????": is_dual_chain(cards)[2], "??????": is_dual_chain(cards)[1]}
    elif is_rocket(cards)[0]:
        return {"??????": "??????", "??????": 4, "??????": 3, "??????": is_rocket(cards)[1]}
    else:
        return False


def cards_compare(cards1, cards2):
    assert cards_type(cards2)
    if cards_type(cards2)['??????'] != cards_type(cards1)['??????']:
        return cards_type(cards2)['??????'] > cards_type(cards1)['??????']
    else:
        assert cards_type(cards2)['??????'] == cards_type(cards1)['??????'] and \
               cards_type(cards2)['??????'] == cards_type(cards1)['??????']
        return cards_type(cards2)['??????'] > cards_type(cards1)['??????']


def have_rocket(cards):
    if len(cards) < 3:
        return []
    have_four = set(cards) & set(PokerCard.cards['4'])
    have_ace = set(cards) & set(PokerCard.cards['14'])
    if len(have_four) >= 2 and len(have_ace) >= 1:
        return [[have_four.pop(), have_ace.pop(), have_four.pop()]]
    else:
        return []


def have_missile(cards, m=2, n=4):
    if len(cards) < 3:
        return []
    level_list = [c.level for c in cards if c.level > m]
    cnt = Counter(level_list)
    cards_list = []
    for c in cnt:
        if cnt[c] == n:
            cards_list.append(PokerCard.cards[str(c)])
    return sort_card(cards_list)


def have_bomb(cards, m=2, n=3):
    if len(cards) < 4:
        return []
    cards_list = []
    level_list = [c.level for c in cards if c.level > m]
    cnt = Counter(level_list)
    for c in cnt:
        if cnt[c] >= n:
            cards_list.append(list(set(cards) & set(PokerCard.cards[str(c)]))[0:3])
    return sort_card(cards_list)


def have_chain(cards, m=2, n=3):
    if len(cards) < n:
        return []
    cards_list = []
    out_cards = PokerCard.cards['16'] + PokerCard.cards['18'] + PokerCard.cards['20']
    cards = list(set(cards) - set(out_cards))
    single_cards = remove_duplicate_card(cards, m)
    for i in range(len(single_cards) - n + 1):
        cards_piece = single_cards[i: i + n]
        if len(cards_piece) == (cards_piece[-1].level - cards_piece[0].level + 1):
            cards_list.append(cards_piece)
    return cards_list


def have_dual_chain(cards, m=2, n=6):
    cards_list = []
    out_cards = PokerCard.cards['16'] + PokerCard.cards['18'] + PokerCard.cards['20']
    cards = list(set(cards) - set(out_cards))
    if len(cards) < n:
        return []
    level_list = [c.level for c in cards if c.level > m]
    cnt = Counter(level_list)
    dual_cards = []
    for c in cnt:
        if cnt[c] >= 2:
            cl = list(set(cards) & set(PokerCard.cards[str(c)]))
            dual_cards += cl[0:2]
    if len(dual_cards) < n:
        return []
    dual_cards = sort_card(dual_cards)
    for i in range(0, len(dual_cards)-n+1, 2):
        cards_piece = dual_cards[i:i+n]
        if len(cards_piece) == (cards_piece[-1].level - cards_piece[0].level + 1)*2:
            cards_list.append(cards_piece)
    return cards_list


def have_pair(cards, m=2, n=2):
    cards_list = []
    if len(cards) < n:
        return []
    level_list = [c.level for c in cards if c.level > m]
    cnt = Counter(level_list)
    for c in cnt:
        if cnt[c] >= 2:
            cards_list.append(list(set(cards) & set(PokerCard.cards[str(c)]))[0:2])
    if PokerCard.cards['18'][0] in cards and PokerCard.cards['20'][0] in cards:
        cards_list.append([PokerCard.cards['18'][0], PokerCard.cards['20'][0]])
    return sort_card(cards_list)


def have_solo(cards, m=2, n=1):
    cards_list = [] * n
    single_list = remove_duplicate_card(cards, m)
    for card in single_list:
        cards_list.append([card])
    return sort_card(cards_list)


def cards_hint(cards1, cards2):
    assert cards_type(cards1)
    ct = cards_type(cards1)
    cards_list = []
    if ct['??????'] == '??????':
        return []
    hint_dict = {'??????': have_solo,
                 '??????': have_pair,
                 '??????': have_chain,
                 '??????': have_dual_chain,
                 '??????': have_bomb,
                 '??????': have_missile}
    cards_list += hint_dict[ct['??????']](cards2, ct['??????'], ct['??????'])
    if ct['??????'] == 1:
        cards_list += hint_dict['??????'](cards2)
        cards_list += hint_dict['??????'](cards2)
        cards_list += have_rocket(cards2)
    elif ct['??????'] == 2:
        cards_list += hint_dict['??????'](cards2)
        cards_list += have_rocket(cards2)
    elif ct['??????'] == 3:
        cards_list += have_rocket(cards2)
    return cards_list


def play_cards(cards):
    if have_dual_chain(cards):
        return have_dual_chain(cards)[0]
    elif have_chain(cards):
        return have_chain(cards)[0]
    elif have_pair(cards):
        return have_pair(cards)[0]
    return [sort_card(cards)[0]]
