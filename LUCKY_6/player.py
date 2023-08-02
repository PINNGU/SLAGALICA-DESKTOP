import logging

logging.basicConfig(level = logging.INFO,filename ="log.log",filemode = "w",
                    format = "%(asctime)s - %(levelname)s ---mod: %(module)s --line:%(lineno)s")

class Player():

    total_money = 0
    bid = 0
    bid_count = 0
    name = ""
    guesses = []

    def get_user(self):
        print("Welcome to LUCKY-6.Test your luck! Win big! ")
        
        self.name = input("Enter your name:")
        self.money  = self.get_money()
        self.bid = self.get_bid_from_money()

        self.get_user_guess()

        return self.money,self.bid,self.guesses
    def get_money(self):

        while(True):
            x = input("Enter your funds(positive number):")
            if x == "exit":
                break
            try:
                x = int(x)
                if x > 0:
                    break
                else:
                    continue
            except:
                print("Wrong input for funds.")
                logging.exception("")
                continue
            
        return x
    
    def get_bid_from_money(self):
         
        while(True):
            x = input("How much of your money should be your bid?")
            
            try:
                x = int(x)
                if self.money % x != 0 or x <= 0:
                    continue
                elif self.money / x > 10:
                    print("Cant have more than 10 games.")
                    continue
                else:
                    break
            except:
                print("Wrong input.")
                logging.exception("")
                continue
        
        return x
    
    def get_user_guess(self):

        print("Enter your six guesses,must be different and within limits.")
        while(len(self.guesses) < 6):
            i = 1
            while(i < 7):
                print(f"GUESS #{i}:")
                x = input()
                try:
                    x = int(x)
                    if x in self.guesses or x <= 0 or x > 48:
                        continue
                    else:
                        i = i + 1
                        self.guesses.append(x)
                except:
                    print("Wrong input.")
                    logging.exception("")
                    continue


