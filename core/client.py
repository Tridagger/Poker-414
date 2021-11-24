# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: client.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/24
-------------------------------------------------
"""

import socket


def player_client(name):
    s = socket.socket()
    s.connect(('127.0.0.1', 35652))
    s.sendall(bytes(name, encoding='utf8'))
    print(str(s.recv(1024), encoding='utf8'))
    while True:
        send_data = input('请输入需要发送的内容：')
        s.sendall(bytes(send_data, encoding='utf8'))
        if send_data == 'bye':
            break

        recv_data = str(s.recv(1024), encoding='utf8')
        print(recv_data)
    s.close()


player_client('P1')