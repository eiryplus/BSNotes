import os
import math
import json
import pygame
import consts


def get_music_length():
    # 曲の長さを取得
    music_path = os.path.join(
        consts.DATA_DIR,
        r"Wish upon Twin Stars - That_One_Narwhal",
        r"Wish.egg"
    )
    pygame.mixer.init()
    sc = pygame.mixer.Sound(music_path)
    return sc.get_length()


def get_notes_count():
    # ノーツの数を取得
    dat_path = os.path.join(
        consts.DATA_DIR,
        r"Wish upon Twin Stars - That_One_Narwhal",
        r"ExpertStandard.dat",
    )
    with open(dat_path, "r") as fp:
        map_ = json.load(fp)
    return len(map_.get("_notes"))


def get_nps():
    # notes per sec
    return math.floor(get_notes_count() / get_music_length() * 100) / 100


def main():
    print(get_nps())


if __name__ == "__main__":
    main()
