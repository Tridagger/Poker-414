# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Poker-414
File Name: main.py
Author: Tridagger
Email: san.limeng@qq.com
Create Date: 2021/11/18
-------------------------------------------------
"""

import socketserver
from core.game import GameRound
from core.server import PokerServer
import threading
import time

def run(debug=False):
    if debug:
        pass

    # 创建一个多线程TCP服务器
    server = socketserver.ThreadingUDPServer(('0.0.0.0', 9999), PokerServer)  # 实例化一个多线程服务器

    def run_server():
        print("启动游戏服务器！")
        server.serve_forever()

    def game_task():
        pass

    t1 = threading.Thread(target=run_server)
    t2 = threading.Thread(target=game_task)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
