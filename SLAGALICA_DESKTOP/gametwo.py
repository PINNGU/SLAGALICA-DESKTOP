import numpy as np
import PySimpleGUI as psg
import random
import time

class GameTwo():

    game_going = True
    score = 0

    def __init__(self,theme):
        self.theme = theme

    def get_digits(self):

        digits = random.sample(range(1,10),k = 4)
        mid_dig = random.choice((5,10,15,20))
        hight_dig = random.choice((25,50,75,100))

        digits.extend((mid_dig,hight_dig))
        return digits
    
    def get_score(self,number):
        if number == self.number:
            self.score = 25
        elif number + 1 == self.number or number - 1 == self.number:
            self.score = 20
        elif number + 2 == self.number or number - 2 == self.number:
            self.score = 15
        elif number + 3 == self.number or number - 3 == self.number:
            self.score = 10
        elif number + 4 < self.number or number - 4 > self.number:
            self.score = 5

    
    def is_divisible(self,one,two,three = 0):
        ret = True

        if one % two != 0:
            ret = False
        if three != 0:
            if one % (two + three) != 0:
                ret = False
        
            if (one  + two) % three != 0:
                ret = False

        return ret    
    def get_signs(self):
        ex = []
        digits = self.get_digits()
        i = 5
        while True:

            if self.is_divisible(digits[i],digits[i - 1],digits[i - 2]):
                sign = random.choice(["/","/","/","/","*","+","-","("])
            elif i == 0:
                sign = random.choice(["*","+","-"])
            else:
                sign = random.choice(("*","+","-","("))

            if sign == "(":
                
                ex.append(sign)
                ex.append(str(digits[i]))
                

                if self.is_divisible(digits[i],digits[i - 1]):
                    sign = random.choice(["/","/","/","*","+","-"])
                  
                else:
                    sign = random.choice(("*","+","-"))

                i = i -1
                ex.append(sign)
                ex.append(str(digits[i]))
                i = i - 1
                ex.append(")")
                
            else:
                ex.append(str(digits[i]))
                i = i - 1
            if i < 0:
                break

            if self.is_divisible(digits[i],digits[i - 1],digits[i - 2]):
                sign = random.choice(["/","/","/","*","+","-"])
            else:
                sign = random.choice(("*","+","-"))
            ex.append(sign)
                
        ex = "".join(ex)
        res = round(eval(ex))
        return res,ex,digits
    

    def get_number(self):
        while True:
            res,ex,digits = self.get_signs()

            if  99 < res < 999:
                self.number = int(res)
                self.digits = digits
                self.solution = ex
                break
    
    def make_window(self):
        psg.theme(self.theme)

        psg.set_options()

        lay = [
                [psg.Push(),psg.Image("images/close.png",enable_events=True,pad = (0,0),key = "CLOSE",size = (24,24))],
                [psg.Push(),psg.Frame("",layout = 
                                      [ 
                                        [psg.Text(f"{self.number}",key = "NUMBER",font="Franklin 36",text_color="#FCC80D")]
                                        ]),psg.Push()],
                [psg.ProgressBar(orientation = 'h',max_value = 60,key = "TIME",size = (60,15))],
                [
                    psg.Text(""),
                    psg.Button(button_text = self.digits[0],size=(7,4),key = "D0",pad = (0,0),mouseover_colors="#006685",button_color=("#F2FF00","#010345")),
                    psg.Button(button_text = self.digits[1],size=(7,4),key = "D1",pad = (0,0),mouseover_colors="#006685",button_color=("#F2FF00","#010345")),
                    psg.Button(button_text = self.digits[2],size=(7,4),key = "D2",pad = (0,0),mouseover_colors="#006685",button_color=("#F2FF00","#010345")),
                    psg.Button(button_text = self.digits[3],size=(7,4),key = "D3",pad = (0,0),mouseover_colors="#006685",button_color=("#F2FF00","#010345")),
                    psg.Text("              "),
                    psg.Button(button_text = self.digits[4],size=(14,4),key = "D4",pad = (0,0),mouseover_colors="#006685",button_color=("#F2FF00","#010345")),
                    psg.Text("                      "),
                    psg.Button(button_text = self.digits[5],size=(26,4),key = "D5",pad = (0,0),mouseover_colors="#006685",button_color=("#F2FF00","#010345")),

                 
                ],
                [
                    psg.Frame("Your input:",size = (580,65),key = "INPUTF",layout = [
                        [psg.Text("",key = "INPUT",font="Franklin 20",text_color="#FCC80D")]
                    ]) ,
                psg.Image("images/backspace.png",enable_events=True,key = "BACK",size = (40,40)),
                psg.Text(),
                psg.Image("images/submit.png",enable_events=True,key = "SUBMIT")
                ],
                [
                 psg.Text("",key = "CHECK",font="Franklin 14",text_color="#FCC80D"),
                 psg.Push(),
                 psg.Button("+",size=(5,3),key = "+",pad = (0,0),mouseover_colors="#006685"),
                 psg.Button("-",size=(5,3),key = "-",pad = (0,0),mouseover_colors="#006685"),
                 psg.Button("*",size=(5,3),key = "*",pad = (0,0),mouseover_colors="#006685"),
                 ],
                [
                psg.Frame("Machine's solution:",key = "MSOLUTION",layout = [
                        [psg.Text("",key = "SOLUTION",font="Franklin 18",text_color="#FCC80D")]
                    ]) ,
                psg.Text("",key = "POINTS",font="Franklin 14",text_color="#FCC80D"), 
                psg.Image("images/continue.png",key = "CONTINUE",pad = (0,0),visible=False,enable_events=True),
                psg.Push(),
                 psg.Button("/",size=(5,3),key = "/",pad = (0,0),mouseover_colors="#006685"),
                 psg.Button("(",size=(5,3),key = "(",pad = (0,0),mouseover_colors="#006685"),
                 psg.Button(")",size=(5,3),key = ")",pad = (0,0),mouseover_colors="#006685"),
                 ],
              
            
            ]
        
        return psg.Window(title="Game Two",layout = lay,size = (800,400),no_titlebar=True)
    
    def start_win(self):

        win = self.make_window()
        start = time.time()
        text_out = [""]
        x = 0
        dig_dict = {"D0":self.digits[0],"D1":self.digits[1],"D2":self.digits[2],"D3":self.digits[3],"D4":self.digits[4],"D5":self.digits[5]}
        clicked = []
        must_sign = True

        while True:
            event,values = win.read(timeout=10)

            cur_time = 60 - (time.time() - start)
            if self.game_going:
                win["TIME"].update(cur_time)

            if cur_time < 0 and self.game_going:
                self.game_going = False
                win["CHECK"].update(f"Time ran out.You've submitted {x}.")
                self.get_score(x)
                win["POINTS"].update(f"You won {self.score} points.")
                win["MSOLUTION"].update(visible = True)
                win["SOLUTION"].update(self.solution)
                win["CONTINUE"].update(visible = True)
                win["/"].update(visible = False)
                win["("].update(visible = False)
                win[")"].update(visible = False)
                win["*"].update(visible = False)
                win["-"].update(visible = False)
                win["+"].update(visible = False)

            if event == "SUBMIT" and self.game_going:
                self.game_going = False
                win["CHECK"].update(f"You've submitted {x}.")
                self.get_score(x)
                win["POINTS"].update(f"You won {self.score} points.")
                win["MSOLUTION"].update(visible = True)
                win["SOLUTION"].update(self.solution)
                win["CONTINUE"].update(visible = True)
                win["/"].update(visible = False)
                win["("].update(visible = False)
                win[")"].update(visible = False)
                win["*"].update(visible = False)
                win["-"].update(visible = False)
                win["+"].update(visible = False)

            if event == "CONTINUE":
                win.close()
                return True

            if event == psg.WIN_CLOSED or event == "CLOSE":
                break

            if event in dig_dict and event not in clicked and must_sign and self.game_going:
                clicked.append(event)
                text_out.append(str(dig_dict[event]))
                win["INPUT"].update("".join(text_out))
                win[event].update("")
                must_sign = False
           

            if event in ["*","/","+","-","(",")"] and self.game_going:
                text_out.append(event)
                win["INPUT"].update("".join(text_out))
                must_sign = True
                

            if event == "BACK" and len(clicked) > 0 and text_out[-1] not in ["*","/","+","-","(",")"] and self.game_going:
                win[clicked[-1]].update(dig_dict[clicked[-1]])
                text_out.pop()
                clicked.pop()
                win["INPUT"].update("".join(text_out))
                must_sign = True
            elif event == "BACK"  and text_out[-1] in ["*","/","+","-","(",")"] and self.game_going:
                text_out.pop()
                win["INPUT"].update("".join(text_out))
                if text_out[-1] not in ["*","/","+","-","(",")"] and text_out[0] != "":
                    must_sign = False
            if self.game_going:
                try:
                    x = eval("".join(text_out))
                    win["CHECK"].update(f"Result is {x}.")

                except:
                    win["CHECK"].update("Not a valid expression.")



        win.close()
        return False