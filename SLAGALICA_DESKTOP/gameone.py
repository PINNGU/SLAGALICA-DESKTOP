import PySimpleGUI as psg
import random

class GameOne():

    won_points = 0
    win_word = ""
    but_keys = {"L0":0,"L1":1,"L2":2,"L3":3,"L4":4,"L5":5,"L6":6,"L7":7,"L8":8,"L9":9,"L10":10,"L11":11}

    def __init__(self,theme,words):
        self.theme = theme
        self.words = words

    def get_word(self):
        
        while True:
            num = random.randint(0,len(self.words))

            if len(self.words[num]) == 12:
                return self.words[num] 

    def get_letters(self):

        word = self.get_word()
        word = word.upper()
        self.win_word = word
        ret = list(word)
        random.shuffle(ret)
        random.shuffle(ret)
        self.letters = ret


    def create_win(self):
        psg.theme(self.theme)
        psg.set_options() 
        self.get_letters()

        lay = [
            [psg.Push(),psg.Image("images/close.png",enable_events=True,pad = (0,0),key = "CLOSE",size = (24,24))],
            [
                 psg.Button(button_text = self.letters[0],size=(13,5),pad = (0,0),key = "L0"),
                 psg.Button(button_text = self.letters[1],size=(13,5),pad = (0,0),key = "L1"),
                 psg.Button(button_text = self.letters[2],size=(13,5),pad = (0,0),key = "L2"),
                 psg.Button(button_text = self.letters[3],size=(13,5),pad = (0,0),key = "L3"),
                 psg.Button(button_text = self.letters[4],size=(13,5),pad = (0,0),key = "L4"),
                 psg.Button(button_text = self.letters[5],size=(13,5),pad = (0,0),key = "L5")
                 ],
                [
                 psg.Button(button_text = self.letters[6],size=(13,5),pad = (0,0),key = "L6"),
                 psg.Button(button_text = self.letters[7],size=(13,5),pad = (0,0),key = "L7"),
                 psg.Button(button_text = self.letters[8],size=(13,5),pad = (0,0),key = "L8"),
                 psg.Button(button_text = self.letters[9],size=(13,5),pad = (0,0),key = "L9"),
                 psg.Button(button_text = self.letters[10],size=(13,5),pad = (0,0),key = "L10"),
                 psg.Button(button_text = self.letters[11],size=(13,5),pad = (0,0),key = "L11")
                 ],
                 [psg.Text()],
                 [psg.Frame("Your Word",layout = [
                        [
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "0"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "1"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "2"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "3"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "4"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "5"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "6"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "7"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "8"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "9"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "10"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "11"),
                        ]]),psg.Image("images/backspace.png",enable_events=True,key = "BACK",size = (40,40)),
                            psg.Text("",key = "TEST",font="Franklin 16",text_color="#DAFC6A")]

        ]

                 
        

        return psg.Window(layout = lay,no_titlebar=True,title="GAME1",size = (800,400))


    def start_win(self):
        win = self.create_win()
        clicked = []
        current_word = []
        while True:

            event,values = win.read()
            

            if event == "CLOSE" or event == psg.WIN_CLOSED:
                break

            if event in list(self.but_keys.keys()):
                win[event].update(visible=False) # MAKE THE CLICKED LETTER INVISIBLE
                clicked.append(event)  #ADD THAT LETTERS KEY TO THE LIST OF CLICKED LETTERS 
                current_letter = self.but_keys[event]
                win[str(current_letter)].update(visible = True) #MAKE THAT LETTER VISIBLE BELOW
                win[str(current_letter)].update(self.letters[current_letter])  # WRITE THAT LETTER
                current_word.append(self.letters[current_letter])
                string_form_word = "".join(current_word).lower()
                if string_form_word in self.words and len(string_form_word) > 2:
                    win["TEST"].update("The word exists")
                else:
                    win["TEST"].update("Word doesn't exist")
                

            if event == "BACK" and len(clicked) > 0:
                win[str(self.but_keys[clicked[-1]])].update("")  # THE LAST PRINTED BELOW LETTER GETS DELETED
                win[str(self.but_keys[clicked[-1]])].update(visible = False) # .. AND BECOMES INVISIBLE
                l = clicked.pop()  # POP THE LAST CLICKED LETTER,THE JUST DELETED ONE,GET ITS KEY
                win[l].update(visible = True)  # AND MAKE IT VISIBLE UP
                current_word.pop()
                string_form_word = "".join(current_word).lower()
                if string_form_word in self.words and len(string_form_word) > 2:
                    win["TEST"].update("The word exists")
                else:
                    win["TEST"].update("Word doesn't exist")
                
   

        win.close()



