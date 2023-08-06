import random
import json

class Game():

    tot_machine_numbers = []
    tot_machine_colors = []

    possible_colors = ["red","green","blue","purple","brown","yellow","orange","black"]
     #always in this order,mod 8

    tot_winnings =  []
 
    lucky_loser_wins = []
    pulled_numbers = []
    win_mult = []
    multipliers = [10000,7500,5000,2500,1000,500,300,200,150,100,90,80,70,60,50,40,30,25,20,15,10,9,8,7,6,5,4,3,2,1]


    gold_bonuses = []
    silver_bonuses = []
    bronze_bonuses = []
    dollar_bonuses = []

    bronze_numbers = []
    dollar_numbers = []


    def __init__(self,money,bid_v,player_guesses):

        self.game_bid = bid_v
        self.guesses = player_guesses
        self.turns = money // bid_v
        self.money = 0
        self.tot_turns = 0

    def one_game(self):
        self.money = 0
        self.starting_bonuses()  #init the starting random bonuses,they increase in each cycle but restart on


        for j in range(self.tot_turns,self.tot_turns + self.turns):

            self.starting_bonuses()  #init the starting random bonuses 
            cur_machine_numbers,dollar_bonus,bronze_limit = self.get_all_numbers()   #get all numbers in cycle,the ones with $ and bronze limiter

            cur_machine_colors = []   #current colors,used for appending to all 
            cur_guess = self.guesses.copy()   #used for removing from copy to check if won
           
            dollar_three = False
            dollar_two = False  

            for n in cur_machine_numbers:    #get the corresponding color for every number
                cur_machine_colors.append(self.possible_colors[(n % 8) - 1])


            self.tot_machine_numbers.append(cur_machine_numbers) # so we can track stats of every cycle in numbers...
            self.tot_machine_colors.append(cur_machine_colors)  #      .....and colors

            gold_bonus = False
            silver_bonus = False  
            bronze_bonus = False
            p_pos_bon = [] # pulled positions for bonuses

            cur_mult = 0  # getting the winning number and its unique multiplier so we can calc the winning amount
            pulled_nums = []  # so we can track what numbers out of our guess are pulled
            for i in range(0,35):  # for each of total numbers
                if cur_machine_numbers[i] in cur_guess:  # if we have it in our guess track it and remove it ...
                    p_pos_bon.append(i)  #-we track all the positions of the balls to check if we got a bonus
                    pulled_num = cur_machine_numbers[i]
                    pulled_nums.append(pulled_num)
                    cur_guess.remove(pulled_num)
                    if len(cur_guess) == 0:   # .. so that if we got all of them out,we guessed all of them
                        cur_mult = self.multipliers[i - 5]  # get that position and its multiplier so we get the profits

                        if i <= bronze_limit: # if we hit all numbers check to see if we hit bronze bonus
                            bronze_bonus = True

                        break
            
            self.win_mult.append(cur_mult)  #we get just the last numbers mult,without any other bonuses,for stattraking

            if dollar_bonus[0] in self.guesses and dollar_bonus[1] in self.guesses:  #check for dollar sign multipliers
                dollar_three = True
                cur_mult = cur_mult * 3
                self.dollar_bonuses.append(3)
            elif dollar_bonus[0] in self.guesses or dollar_bonus[1] in self.guesses:
                dollar_two = True
                cur_mult = cur_mult * 2
                self.dollar_bonuses.append(2)
            else:
                self.dollar_bonuses.append(1)
            
            #check for positions of silver and gold bonuses
            gold_bonus,silver_bonus = self.check_gold_silver(p_pos_bon)

            #print(cur_machine_numbers)
            #print(pulled_nums)
            self.pulled_numbers.append(pulled_nums)
                    
            cur_win_tot = 0
            if len(cur_guess) == 6:
                print(f"GAME #{j+1}:LUCKY LOSER")
                self.lucky_loser_wins.append(True)
                cur_win_tot = self.game_bid * 50
            elif len(cur_guess) == 0:
                print(f"GAME #{j+1}:YOU WON!")
                self.lucky_loser_wins.append(False)
                cur_win_tot = self.game_bid * cur_mult
                if dollar_three:
                    print("TRIPLE CASH!!!")
                elif dollar_two:
                    print("DOUBLE TROUBLE!!!")                    

                if gold_bonus:
                    print("GOLD BONUS!")
                    cur_win_tot = cur_win_tot + self.gold
                if silver_bonus:
                    print("SILVER BONUS!")
                    cur_win_tot = cur_win_tot + self.silver
                if bronze_bonus:
                    print("BRONZE BONUS!")
                    cur_win_tot = cur_win_tot + self.bronze
            else:
                print(f"GAME #{j+1}:Loss.")
                self.lucky_loser_wins.append(False)
            

            self.tot_winnings.append(cur_win_tot)   # so we track our winnings in each of the cycles

            self.money = self.money + cur_win_tot  # increase our winnings by the amount bid and the determined multiplier

            self.gold_bonuses.append(gold_bonus)
            self.silver_bonuses.append(silver_bonus)
            self.bronze_bonuses.append(bronze_bonus)
            self.bronze = self.bronze + self.game_bid  # all three,have got a random amount on start,they increase in each bid by the bid amount
            self.gold = self.gold + self.game_bid
            self.silver = self.silver + self.game_bid

        

        print(f"Total winnings:{self.money}")
        self.tot_turns = self.tot_turns + self.turns


    def get_stats(self,f,fjs): # print all the characteristics stats and numbers of each cycle
          

        for i in range(self.tot_turns-self.turns,self.tot_turns):

            
            f.write(f"\n-------------------------------CYCLE #{i+1}-------------------------------")
            for j in range(0,35):
                if j % 18 == 0:
                    f.write("\n")

                    
                f.writelines(f"{str(self.tot_machine_numbers[i][j])} ")

            f.writelines(f"\n\n----Correct Guesses: {str(self.pulled_numbers[i])}")  # print the guessed numbers
            f.writelines(f"\n\nDollar Signs: {self.dollar_numbers[i]}  |||   Bronze Multiplier: X{self.multipliers[self.bronze_numbers[i] - 5]}  |||  Lucky loser: {self.lucky_loser_wins[i]}")
            
            #same line just in json format,testing out 

            #json format can be used to easily get data and use it for own purposes,in this case the rarity of symbols and specials
            
            js_dict_temp  = {"CYCLE":i+1,"$":self.dollar_numbers[i],"BRONZE":self.multipliers[self.bronze_numbers[i] - 5],"LUCKY_LOSER":self.lucky_loser_wins[i]}
            json.dump(js_dict_temp,fjs,indent=1)


            f.writelines(f"\n\n-----Won amount: {self.tot_winnings[i]} === Multiplier: X{self.win_mult[i]} -- Bid: {self.game_bid}")

            #added function for color chances
            self.get_color_chances(i,f)


            f.writelines(f"\n              ------Bonuses------\nBronze = {self.bronze_bonuses[i]} ||| Silver = {self.silver_bonuses[i]} ||| Gold = {self.gold_bonuses[i]} ||| Dollar = ")

            if(self.dollar_bonuses[i] == 3):
                f.write("Triple")
            elif(self.dollar_bonuses[i] == 2):
                f.write("Double")
            else:
                f.write("None")


        
        


    def get_ticket(self,g):
        g.write("_________________________________________________")
        for i in range(self.tot_turns - self.turns,self.tot_turns):
            
            
            g.write(f"\n|                Cycle #{i + 1 :08d}                |")
            g.write(f"\n|                                               |")
            g.writelines(f"\n|              {self.guesses[0]:02d},{self.guesses[1]:02d},{self.guesses[2]:02d},{self.guesses[3]:02d},{self.guesses[4]:02d},{self.guesses[5]:02d}                |")
            g.write(f"\n|                                               |")
            g.write(f"\n|-----------------------------------------------|")
            g.write(f"\n|                                  Bid: {self.game_bid:04d}    |")   
            g.write(f"\n|-----------------------------------------------|")

        g.write(f"\n|                                  Total: {self.game_bid * self.turns:05d} |")   
        g.write(f"\n|-----------------------------------------------|")  

    def run_alot(self):
        self.one_game()
        ret = False
        if True in self.gold_bonuses or True in self.silver_bonuses or True in self.lucky_loser_wins:
            ret = True
        
        return ret
    
    def get_full_game_wins(self):
        return self.money
    
    def check_gold_silver(self,pos):
        bonus = [12,16,19,22,26,34]
        b_c = bonus.copy()
        ret_gold = False
        ret_silver = False

        for i in bonus:
            if i in pos:
                b_c.remove(i)

                if len(b_c) == 0:
                    ret_gold = True
                    ret_silver = False
                    break
                elif len(b_c) == 1:
                    ret_silver = True

        return ret_gold,ret_silver
    
    def starting_bonuses(self):
        self.gold = random.randint(45500,61250)
        self.silver = random.randint(17450,21650)
        self.bronze = random.randint(4425,6325)

    def get_all_numbers(self):
        cur_machine_numbers = random.sample(range(1,49),k = 35)

        dollar_bonus = random.sample(cur_machine_numbers,k  = 2) # if one is hit,*2,both * 3
        self.dollar_numbers.append(dollar_bonus)
        bronze_limit = random.randint(6,15) # get the limit for bronze,must hit before the limit to get bronze 
        self.bronze_numbers.append(bronze_limit)

        return cur_machine_numbers,dollar_bonus,bronze_limit
    
    def get_color_chances(self,i,f):
        green_chance = round(self.tot_machine_colors[i].count("green") / 35 * 100,2)
        blue_chance = round(self.tot_machine_colors[i].count("blue") / 35 * 100,2)
        red_chance = round(self.tot_machine_colors[i].count("red") / 35 * 100,2)
        yellow_chance = round(self.tot_machine_colors[i].count("yellow") / 35 * 100,2)
        orange_chance = round(self.tot_machine_colors[i].count("orange") / 35 * 100,2)
        purple_chance = round(self.tot_machine_colors[i].count("purple") / 35 * 100,2)
        brown_chance = round(self.tot_machine_colors[i].count("brown") / 35 * 100,2)
        black_chance = round(self.tot_machine_colors[i].count("black") / 35 * 100,2)       

        f.writelines(f"\n\n              ---COLOR CHANCES---   \nGreen: {green_chance} Blue: {blue_chance} Red: {red_chance} Yellow: {yellow_chance}\nOrange: {orange_chance} Purple: {purple_chance} Brown: {brown_chance} Black: {black_chance} \n")
