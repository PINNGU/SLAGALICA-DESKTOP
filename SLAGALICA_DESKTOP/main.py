from login import Login
from gameone import GameOne
import json

GAME_THEME = "DarkBlue10"
VERSION = "V1.1"

#player = Login(GAME_THEME,VERSION)
#if player.start_win():
file = open("words.json","r")

words = json.load(file)
words = tuple(words.keys())
game_one = GameOne(GAME_THEME,words)


game_one.start_win()

file.close()



#TODO change to icons the word check?? mauybe,add timer for words,add end popup for score and the machine word...