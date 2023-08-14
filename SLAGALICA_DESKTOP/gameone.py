import PySimpleGUI as psg
import random

class GameOne():

    won_points = 0

    def __init__(self,theme):
        self.theme = theme

    def get_letters(self):
        letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

        ret = random.choices(letters,k=12)

        return ret



    def create_win(self):
        psg.theme(self.theme)
        psg.set_options()
        l = self.get_letters() # letters

        lay = [
            [psg.Push(),psg.Image("close.png",enable_events=True,pad = (0,0),key = "CLOSE",size = (24,24))],
            [psg.Button(button_text = l[0],size=(13,5),pad = (0,0),key = "L0",),
                 psg.Button(button_text = l[1],size=(13,5),pad = (0,0),key = "L1"),
                 psg.Button(button_text = l[2],size=(13,5),pad = (0,0),key = "L2"),
                 psg.Button(button_text = l[3],size=(13,5),pad = (0,0),key = "L3"),
                 psg.Button(button_text = l[4],size=(13,5),pad = (0,0),key = "L4"),
                 psg.Button(button_text = l[5],size=(13,5),pad = (0,0),key = "L5")
                 ],
                [
                 psg.Button(button_text = l[6],size=(13,5),pad = (0,0),key = "L6"),
                 psg.Button(button_text = l[7],size=(13,5),pad = (0,0),key = "L7"),
                 psg.Button(button_text = l[8],size=(13,5),pad = (0,0),key = "L8"),
                 psg.Button(button_text = l[9],size=(13,5),pad = (0,0),key = "L9"),
                 psg.Button(button_text = l[10],size=(13,5),pad = (0,0),key = "L10"),
                 psg.Button(button_text = l[11],size=(13,5),pad = (0,0),key = "L11")
                 ],
                 [psg.Text()],
                 [psg.Frame("Your Word",layout = [
                        [
                            psg.Button(size = (5,3),pad = (0,0),visible=False,key = "0"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,key = "1"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,key = "2"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,key = "3"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,key = "4"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,key = "5"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,key = "6"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,key = "7"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,key = "8"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,key = "9"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,key = "10"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,key = "11"),
                            psg.Push(),
                        ]]),psg.Image("backspace.png",enable_events=True,key = "BACK")]

        ]

                 
        

        return psg.Window(layout = lay,no_titlebar=True,title="GAME1",size = (800,400))


    def start_win(self):
        win = self.create_win()
        cur_letter = 0
        
        while True:

            event,values = win.read()

            if event == "CLOSE" or event == psg.WIN_CLOSED:
                break

            if event in ["L0","L1","L2","L3","L4","L5","L6","L7","L8","L9","L10","L11"]:
                win[event].update(visible=False)

                win[str(cur_letter)].update(visible = True)
                cur_letter = cur_letter + 1

            #if event == 
   

        win.close()



