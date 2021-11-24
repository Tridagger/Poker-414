# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: server.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/24
-------------------------------------------------
"""

import socketserver


class PokerServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        addr = self.client_address
        player = str(conn.recv(1024), encoding='utf8')
        print(player, 'from', addr)
        conn.sendall(bytes(f'{player}与服务器建立链接', encoding='utf8'))
        while True:
            recv_data = str(conn.recv(1024), encoding='utf8')
            print(recv_data)
            if recv_data == 'bye':
                break

            send_data = bytes(input('请输入回复消息：'), encoding='utf8')
            conn.sendall(send_data)
        conn.close()


game_server = socketserver.ThreadingTCPServer(('0.0.0.0', 35652), PokerServer)

