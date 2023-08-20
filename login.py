import PySimpleGUI as psg
import json


class Login():

    name = ""
    age = ""
    gender = ""
    password = ""
    tutorial = False
    score = 0
    players = []
    LOGGED_IN = False

    def __init__(self,theme,version):
        self.theme = theme
        self.version = version

    def get_player_values(self,values):
        self.name = values["NAME"]
        self.password = values["PASS"]
        self.age = round(values["AGE"])
        self.gender = "M" if  values["GENDER"] else "F"

    def get_all_players(self):
        with open("players.txt","r") as f:
            pl = f.read()
            pl = pl.replace(",","\n")
            pl = pl.split("\n")
            for i in range(0,len(pl)//5):
                temp = {"NAME":pl[i * 5],"PASS":pl[i * 5 + 1],"AGE":pl[i * 5 + 2],"GENDER":pl[i  * 5 + 3],"SCORE":pl[i * 5 + 4]}
                self.players.append(temp)
  

    def name_exists(self,name):
        for player in self.players:
            if player["NAME"] == name:
                return True
        
        return False
    
    def match_passwords(self):
        for player in self.players:
            if self.name == player["NAME"]:
                if self.password == player["PASS"]:
                    return True
                else:
                    return False



    def add_new_user(self):
        temp = {"NAME":self.name,"PASS":self.password,"AGE":self.age,"GENDER":self.gender,"SCORE":self.score}
        self.players.append(temp)



    def tutorial_window(self):
        psg.theme(self.theme)
        lay = [
            [psg.Push(),psg.Image("images/close.png",enable_events=True,pad = (0,0),key = "CLOSE",size = (24,24))],
            [psg.Text("Slagalica,popular Serbian quiz-show, made in english.",text_color="#72FCD5",font = "Franklin 14")],
            [psg.Frame("Game #1",title_color="#72FCD5",expand_x=True,font = "Calibri 14",layout = [[
                psg.Text("Very simple, test your vocabulary - enter the longest possible word!",text_color="#72FCD5",font = "Franklin 12")]])],
            [psg.Frame("Game #2",title_color="#72FCD5",expand_x=True,font = "Calibri 14",layout = [[
                psg.Text("Using the given digits,get as closest as you can to the main number!",text_color="#72FCD5",font = "Franklin 12")]])],
            [psg.Frame("Game #3",title_color="#72FCD5",expand_x=True,font = "Calibri 14",layout = [[
                psg.Text("Nothing yet...",text_color="#72FCD5",font = "Franklin 12")]])],
            [psg.Frame("Game #4",title_color="#72FCD5",expand_x=True,font = "Calibri 14",layout = [[
                psg.Text("Nothing yet...",text_color="#72FCD5",font = "Franklin 12")]])],
            [psg.VPush()],
            [psg.Push(),psg.Button("READY!",key = "START",font = "Calibri 24",mouseover_colors="#006685",border_width=0),psg.Push()]
        ]

        win = psg.Window(title="TUTORIAL",layout = lay,no_titlebar=True,size = (800,400))

        while True:

            event,values = win.read()
            if event == psg.WINDOW_CLOSED or event == "CLOSE":
                win.close()
                return False
            
            if event == "START":
                win.close()
                return True
            


    def create_win(self):

        psg.theme(self.theme)
        

        left = psg.Column(size=(480,350),layout = [
            [psg.Text("USERNAME:",text_color="#72FCD5",font = "Franklin 18"),psg.Input(key = "NAME",text_color="#24004A",font="Franklin 16")],
            [psg.Text("PASSWORD:",text_color="#72FCD5",font = "Franklin 18"),psg.Input(key = "PASS",text_color="#24004A",font="Franklin 16",password_char="•")],
            [psg.Frame("Gender",title_color="#72FCD5",expand_x=True,font = "Calibri 18",layout = [
                [psg.Radio("Male","GENDER",text_color="#A5f2CF",font = "Calibri 16",key = "GENDER"),psg.Radio("Female","GENDER",text_color="#A5f2CF",font = "Calibri 16",key = "GENDER")]])],
            [psg.Frame("Age",title_color="#72FCD5",expand_x=True,font = "Calibri 18",layout = [[
                psg.Slider(orientation="h",default_value="14",range = (8,88),trough_color="#006685",key = "AGE")]])],
            [psg.Button("Sign In",key = "SIGNIN",font = "Calibri 18",mouseover_colors="#006685",border_width=0,button_color=("#F2FF00","#010345")),
             psg.Button("Log In",key = "LOGIN",font = "Calibri 18",mouseover_colors="#006685",border_width=0,button_color=("#F2FF00","#010345"))],
             [psg.Text("",key="NOTIFY",font = "TimesNewRoman 18",text_color="#A5f2CF")]
        ])

        right = psg.Column(size= (320,350),layout = [
            [psg.Text("Do you wish to play the tutorial?",font="Franklin 16",text_color="#DAFC6A")],
            [psg.Button("Lets do it!",key = "PLAY-TUT",font = "Calibri 14",mouseover_colors="#006685",border_width=0,button_color=("#F2FF00","#010345")),
             psg.Button("No thank you.",key = "NO-TUT",font = "Calibri 14",mouseover_colors="#006685",border_width=0,button_color=("#F2FF00","#010345"))],
            [psg.Text("",key = "GOTO-TUT",font = "Franklin 16",text_color="#DAFC6A"),psg.VPush()],
            [psg.Text("")],
            [psg.Text("")],
            [psg.Push(),psg.Image("images/logo.png",size = (200,140))],
            [psg.Push(),psg.Text(f"VERSION {self.version}",key = "VERSION",font="Franklin 12",text_color="#DAFC6A")]
            
        ])

        lay = [
            [psg.Push(),psg.Image("images/close.png",enable_events=True,pad = (0,0),key = "CLOSE",size = (24,24))],
            [left,psg.VerticalSeparator(),right],

            
        ]

        return psg.Window(title="SLAGALICA",layout = lay,no_titlebar=True)


    def start_win(self):
        window = self.create_win()
        self.get_all_players()

        while True:

            event,values = window.read()
            if event == psg.WINDOW_CLOSED or event == "CLOSE":
                break

            if event == "SIGNIN":
                    self.get_player_values(values)

                    if self.name_exists(self.name):
                       window["NOTIFY"].update("This player already exists,try logging in.") 
                    elif self.name == "":
                        window["NOTIFY"].update("Not a valid username.") 
                    else:
                        self.add_new_user()
                        window["NOTIFY"].update("Successfuly signed in!")
                        self.LOGGED_IN = True

            if event == "LOGIN":

                self.get_player_values(values)

                if not self.name_exists(self.name):
                    window["NOTIFY"].update("This player doesn't exist.Sign in first.") 
                elif self.name_exists(self.name):
                    if self.match_passwords():
                        window["NOTIFY"].update("Successfuly logged in!")
                        self.LOGGED_IN = True
                    else:
                        window["NOTIFY"].update("Wrong Password!")
                

            if event == "PLAY-TUT":
                if not self.LOGGED_IN:
                    window["GOTO-TUT"].update("You must enter credentials first.")
                else:
                    window.close()
                    return self.tutorial_window()

    
            if event == "NO-TUT":
                if not self.LOGGED_IN:
                    window["GOTO-TUT"].update("You must enter credentials first.")
                else:
                    window.close()
                    return True

                
            

        window.close()
        return False
    
    def new_scoreboard(self):
        with open("players.txt","w") as f:
            for i in self.players:
                if i["NAME"] == self.name:
                    conv = int(i["SCORE"]) + self.score
                    i["SCORE"] = conv
            
                f.write(f"{i['NAME']},{i['PASS']},{i['AGE']},{i['GENDER']},{i['SCORE']}\n")

