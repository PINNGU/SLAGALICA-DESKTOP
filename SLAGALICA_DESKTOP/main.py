from login import Login
from gameone import GameOne

GAME_THEME = "DarkBlue10"
VERSION = "V1.1"

player = Login(GAME_THEME,VERSION)
if player.start_win():
    game_one = GameOne(GAME_THEME)
    game_one.start_win()