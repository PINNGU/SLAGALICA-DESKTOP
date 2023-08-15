import PySimpleGUI as psg
import random
import time

class GameOne():

    won_points = 0
    win_word = ""
    but_keys = {"L0":0,"L1":1,"L2":2,"L3":3,"L4":4,"L5":5,"L6":6,"L7":7,"L8":8,"L9":9,"L10":10,"L11":11}
    game_done = False

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

        lay1 = psg.Column(size = (680,400),layout = [
            
            [
                 psg.Button(button_text = self.letters[0],size=(13,5),pad = (0,0),key = "L0",mouseover_colors="#006685"),
                 psg.Button(button_text = self.letters[1],size=(13,5),pad = (0,0),key = "L1",mouseover_colors="#006685"),
                 psg.Button(button_text = self.letters[2],size=(13,5),pad = (0,0),key = "L2",mouseover_colors="#006685"),
                 psg.Button(button_text = self.letters[3],size=(13,5),pad = (0,0),key = "L3",mouseover_colors="#006685"),
                 psg.Button(button_text = self.letters[4],size=(13,5),pad = (0,0),key = "L4",mouseover_colors="#006685"),
                 psg.Button(button_text = self.letters[5],size=(13,5),pad = (0,0),key = "L5",mouseover_colors="#006685")
                 ],
                [
                 psg.Button(button_text = self.letters[6],size=(13,5),pad = (0,0),key = "L6",mouseover_colors="#006685"),
                 psg.Button(button_text = self.letters[7],size=(13,5),pad = (0,0),key = "L7",mouseover_colors="#006685"),
                 psg.Button(button_text = self.letters[8],size=(13,5),pad = (0,0),key = "L8",mouseover_colors="#006685"),
                 psg.Button(button_text = self.letters[9],size=(13,5),pad = (0,0),key = "L9",mouseover_colors="#006685"),
                 psg.Button(button_text = self.letters[10],size=(13,5),pad = (0,0),key = "L10",mouseover_colors="#006685"),
                 psg.Button(button_text = self.letters[11],size=(13,5),pad = (0,0),key = "L11",mouseover_colors="#006685"),
                 psg.Push(),
                 ],
                 [psg.Text()],
                 [psg.Frame("Your Word",title_color="#72FCD5",layout = [
                        [
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "0",mouseover_colors="#006685"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "1",mouseover_colors="#006685"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "2",mouseover_colors="#006685"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "3",mouseover_colors="#006685"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "4",mouseover_colors="#006685"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "5",mouseover_colors="#006685"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "6",mouseover_colors="#006685"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "7",mouseover_colors="#006685"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "8",mouseover_colors="#006685"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "9",mouseover_colors="#006685"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "10",mouseover_colors="#006685"),
                            psg.Button(size = (5,3),pad = (0,0),visible=False,enable_events=False,key = "11",mouseover_colors="#006685"),
                        ]]),psg.Image("images/backspace.png",enable_events=True,key = "BACK",size = (40,40)),
                            psg.Text("",key = "TEST",font="Franklin 16",text_color="#72FCD5"),
                            psg.Push(),
                 ],
                 [
                    psg.Frame("Machine's Word",visible=False,title_color="#72FCD5",key = "MACH_FRAME",layout = [[
                        psg.Text(self.win_word,key = "MACH_WORD",text_color="#72FCD5",font = "Franklin 16",visible=False)
                        ]]
                             ),
                    psg.Text("",key = "SCORE",text_color="#72FCD5",font = "Franklin 16",visible=False),
                    psg.Image("images/continue.png",key = "CONTINUE",pad = (0,0),visible=False,enable_events=True)
                 ]
                 

        ])

        lay2 = psg.Column(size = (120,400),layout = [[
            psg.Push(),
            psg.Image("images/submit.png",enable_events=True,key = "SUBMIT"),
             psg.ProgressBar(orientation = 'v',max_value = 60,key = "TIME",size = (30,15))
        ]])

                 
        lay = [
            [psg.Push(),psg.Image("images/close.png",enable_events=True,pad = (0,0),key = "CLOSE",size = (24,24))],
            [lay1,psg.Push(),lay2]
        ]
        return psg.Window(layout = lay,no_titlebar=True,title="GAME1")


    def start_win(self):
        win = self.create_win()
        clicked = []
        current_word = []
        start = time.time()
        string_form_word = ""
        while True:

            event,values = win.read(timeout = 10)
            
            cur_time = round(60 - (time.time() - start))
            if cur_time < 0  or event == "SUBMIT" and not self.game_done:
                if string_form_word in self.words and len(current_word) > 2:
                    self.won_points = 2 * len(current_word)
                win["MACH_FRAME"].update(visible = True)
                win["MACH_WORD"].update(visible = True)
                win["SCORE"].update(visible = True)
                win["SCORE"].update(f"You won {self.won_points} points.")
                win["CONTINUE"].update(visible = True)
                self.game_done = True

            if event == "CONTINUE":
                win.close()
                return True

            if not self.game_done:
                win["TIME"].update(cur_time)
            
            if event == "CLOSE" or event == psg.WIN_CLOSED:
                break

            if event in list(self.but_keys.keys()) and not self.game_done:
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
                

            if event == "BACK" and len(clicked) > 0 and not self.game_done:
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
        return False


