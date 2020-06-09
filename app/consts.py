import os
from enum import Enum


PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
TMP_DIR = os.path.join(PROJECT_DIR, "tmp")
DATA_DIR = os.path.join(PROJECT_DIR, "data")


class Hand(Enum):
    # _type
    LEFT = 0
    RIGHT = 1


class Arrow(Enum):
    # _cutDirection
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    NORTH_WEST = 4  # 左上
    NORTH_EAST = 5  # 右上
    SOUTH_WEST = 6  # 左下
    SOUTH_EAST = 7  # 右下
    DOT = 8  # 方向なし


class Layer(Enum):
    # _lineLayer
    BOTTOM = 0  # 一番下
    CENTER = 1  # 真ん中
    TOP = 2  # 一番上


class Point(Enum):
    # _lineIndex
    LEFT1 = 0
    LEFT2 = 1
    RIGHT1 = 2
    RIGHT2 = 3
