import os
import sys
from core.main import run

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)


if __name__ == '__main__':
    run()

