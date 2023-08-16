import numpy as np
import PySimpleGUI as psg
import random

class GameTwo():

    def __init__(self,theme):
        self.theme = theme

    def get_digits(self):

        digits = random.choices(range(1,10),k = 4)
        mid_dig = random.choice((5,10,20))
        hight_dig = random.choice((25,50,75,100))

        digits.extend((mid_dig,hight_dig))
        return digits
    