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
                self.digits = np.array(digits)
                self.solution = ex
                print(f"{ex}  =  {res} , {digits}")
                break
    
    def make_window(self):
        pass # implement