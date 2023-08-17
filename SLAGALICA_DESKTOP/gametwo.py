import numpy as np
import PySimpleGUI as psg
import random

class GameTwo():

    def __init__(self,theme):
        self.theme = theme

    def get_digits(self):

        digits = random.sample(range(1,10),k = 4)
        mid_dig = random.choice((5,10,15,20))
        hight_dig = random.choice((25,50,75,100))

        digits.extend((mid_dig,hight_dig))
        return digits
    
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
                print(f"{ex}  =  {res} , {digits}")
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
                [psg.HorizontalSeparator()],
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
                psg.Image("images/backspace.png",enable_events=True,key = "BACK",size = (40,40))
                ],
                [psg.Push(),
                 psg.Button("+",size=(5,3),key = "+",pad = (0,0),mouseover_colors="#006685"),
                 psg.Button("-",size=(5,3),key = "-",pad = (0,0),mouseover_colors="#006685"),
                 psg.Button("*",size=(5,3),key = "*",pad = (0,0),mouseover_colors="#006685"),
                 ],
                [psg.Push(),
                 psg.Button("/",size=(5,3),key = "/",pad = (0,0),mouseover_colors="#006685"),
                 psg.Button("(",size=(5,3),key = "(",pad = (0,0),mouseover_colors="#006685"),
                 psg.Button(")",size=(5,3),key = ")",pad = (0,0),mouseover_colors="#006685"),
                 ],
            
            ]
        
        return psg.Window(title="Game Two",layout = lay,size = (800,400),no_titlebar=True)
    
    def start_win(self):

        win = self.make_window()
        text_out = [""]
        dig_dict = {"D0":self.digits[0],"D1":self.digits[1],"D2":self.digits[2],"D3":self.digits[3],"D4":self.digits[4],"D5":self.digits[5]}
        clicked = []
        must_sign = True

        while True:
            event,values = win.read()

            if event == psg.WIN_CLOSED or event == "CLOSE":
                break

            if event in dig_dict and event not in clicked and must_sign:
                clicked.append(event)
                text_out.append(str(dig_dict[event]))
                win["INPUT"].update("".join(text_out))
                win[event].update("")
                must_sign = False

            if event == "BACK" and len(clicked) > 0 and text_out[-1] not in ["*","/","+","-","(",")"]:
                win[clicked[-1]].update(dig_dict[clicked[-1]])
                text_out.pop()
                clicked.pop()
                win["INPUT"].update("".join(text_out))
                must_sign = True

            if event == "BACK"  and text_out[-1] in ["*","/","+","-","(",")"]:
                text_out.pop()
                win["INPUT"].update("".join(text_out))


            if event in ["*","/","+","-","(",")"]:
                if event == "(":
                    if text_out[-1] not in str(dig_dict.values()):
                        text_out.append(event)
                else:
                    text_out.append(event)
                    win["INPUT"].update("".join(text_out))
                    if event in ["*","/","+","-","("]:
                        must_sign = True



        win.close()