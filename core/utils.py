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

    def send(self, contents, player):
        contents = pickle.dumps(contents)
        self.file.sendto(contents, player)

    def send_all(self, contents):
        contents = pickle.dumps(contents)
        for player in self.players:
            self.file.sendto(contents, player)


class C2S:
    def __init__(self, client, server):
        self.client = client
        self.server = server

    def load(self):
        contents, _ = self.client.recvfrom(1024)
        contents = pickle.loads(contents)
        return contents

    def send(self, contents):
        contents = pickle.dumps(contents)
        self.client.sendto(contents, self.server)
