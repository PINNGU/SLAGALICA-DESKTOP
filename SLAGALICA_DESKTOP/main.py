from login import Login
from gameone import GameOne
from gametwo import GameTwo
import json

GAME_THEME = "DarkBlue10"
VERSION = "V1.3"

player = Login(GAME_THEME,VERSION)
finished_login = player.start_win()#
if finished_login:
    file = open("words.json","r")

    words = json.load(file)
    words = tuple(words.keys())
    game_one = GameOne(GAME_THEME,words)

    game_one_finished = game_one.start_win()
    player.score = player.score + game_one.won_points # get the won points in first game,conc

    if game_one_finished:  # if the first game has concluded and the player chose to keep playing
        game_two = GameTwo(GAME_THEME)  # init the second game

        game_two.get_number()
        game_two_finished =  game_two.start_win()
        player.score = player.score + game_two.score

        if game_two_finished:
            print(player.score)

file.close()




#TODO third game,scoreboard and db
