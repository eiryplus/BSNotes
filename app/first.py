import math
import json
import pygame

# 曲の長さを取得
music_path = r"C:\var\developments\BSNorts\tmp\Wish upon Twin Stars - That_One_Narwhal\Wish.egg"
pygame.mixer.init()
sc = pygame.mixer.Sound(music_path)
music_len = sc.get_length()

# ノーツの数を取得
dat_path: str = r"C:\var\developments\BSNorts\data\Wish upon Twin Stars - That_One_Narwhal\ExpertStandard.dat"
with open(dat_path, "r") as fp:
    map_: dict = json.load(fp)
notes_count = len(map_.get('_notes'))

# notes per sec
print(math.floor(notes_count/music_len * 100) / 100)
