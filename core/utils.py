# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: utils.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/27
-------------------------------------------------
"""
import pickle


class S2C:
    def __init__(self, file, players):
        self.file = file
        self.players = players

    def send(self, contents, addr):
        contents = pickle.dumps(contents)
        self.file.sendto(contents, addr)

    def send_all(self, contents):
        contents = pickle.dumps(contents)
        for player in self.players:
            self.file.sendto(contents, player.addr)


class C2S:
    def __init__(self, client, server):
        self.client = client
        self.server = server

    def load(self):
        contents, _ = self.client.recvfrom(1024)
        contents = pickle.loads(contents)
        return contents

    def send(self, contents, *args):
        contents = pickle.dumps(contents)
        self.client.sendto(contents, self.server)


class Content:
    def __init__(self, send_tools):
        self.mode = None
        self.inform = None
        self.cards = None
        self.addr = None
        self.tools = send_tools

    def send(self, addr):
        cont = {
            'mode': self.mode,
            'inform': self.inform,
            'cards': self.cards,
            'addr': self.addr
        }
        self.tools.send(cont, addr)
        self.clear()

    def send_all(self):
        cont = {
            'mode': self.mode,
            'inform': self.inform,
            'cards': self.cards,
            'addr': self.addr
        }
        self.tools.send_all(cont)
        self.clear()

    def clear(self):
        self.mode = None
        self.inform = None
        self.cards = None
        self.addr = None
