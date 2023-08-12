import PySimpleGUI as psg
import json


class Login():

    theme = "DarkBlue10"
    name = ""
    age = ""
    gender = ""
    tutorial = False
    score = 0
    total_score = "0"
    players = []

    def get_all_players(self):
        with open("players.txt","r") as f:
            pl = f.read()
            pl = pl.replace(",","\n")
            pl = pl.split("\n")
            for i,p in enumerate(pl):
                if i % 4 == 0:
                    self.players.append(p)


    def names_exists(self):
        pass

    def add_name(self):
        pass


    def create_win(self):

        psg.theme(self.theme)
        

        left = psg.Column(size=(480,350),layout = [
            [psg.Text("USERNAME:",text_color="#72FCD5",font = "Franklin 18"),psg.Input(key = "NAME",text_color="#24004A",font="Franklin 16")],
            [psg.Frame("Gender",title_color="#72FCD5",expand_x=True,font = "Calibri 18",layout = [
                [psg.Radio("Male","GENDER",text_color="#A5f2CF",font = "Calibri 16",key = "GENDER"),psg.Radio("Female","GENDER",text_color="#A5f2CF",font = "Calibri 16",key = "GENDER")]])],
            [psg.Frame("Age",title_color="#72FCD5",expand_x=True,font = "Calibri 18",layout = [[
                psg.Slider(orientation="h",default_value="14",range = (8,88),trough_color="#006685",key = "AGE")]])],
            [psg.Button("Create Account",key = "START",font = "Calibri 18",mouseover_colors="#006685")]
        ])

        right = psg.Column(size= (320,350),layout = [
            [psg.Text("Do you wish to play the tutorial?",font="Franklin 16",text_color="#DAFC6A")],
            [psg.Button("Lets do it!",key = "PLAY-TUT",font = "Calibri 14",mouseover_colors="#006685"),psg.Button("No thank you.",key = "NO-TUT",font = "Calibri 14",mouseover_colors="#006685")],
            [psg.Text("",key = "GOTO-TUT",font = "Franklin 16",text_color="#DAFC6A")]
            
        ])

        lay = [
            [psg.Push(),psg.Image("close.png",enable_events=True,pad = (0,0),key = "CLOSE",size = (24,24))],
            [left,psg.VerticalSeparator(),right],
            [psg.VPush()]
            
        ]

        return psg.Window(title="SLAGALICA",layout = lay,no_titlebar=True)


    def start_win(self):
        window = self.create_win()
        self.get_all_players()

        while True:

            event,values = window.read()
            if event == psg.WINDOW_CLOSED or event == "CLOSE":
                break

            if event == "START":
                    #implement to check if name in list and then add
                    self.name = values["NAME"]
                    self.age = str(values["AGE"])
                    self.gender = "M" if  values["GENDER"] else "F"
                    self.add_name()
                    print(self.players)


                

            if event == "PLAY-TUT" or event == "NO-TUT":
                window["GOTO-TUT"].update("You must enter credentials first.")
                with open("players.json","r") as f:
                    for line in f:
                        print(json.dumps(line))
                
                print(self.players)
                f.close()

            

        window.close()
        return
    
