from player import Player
from game import Game

player = Player()

money,bid_value,guesses = player.get_user()

game = Game(money,bid_value,guesses)

#game = Game(1000,200,[5,6,7,8,9,10])           #testcase
#game.one_game()                                #
#game.get_stats()                               #

c = 0
stake = 0
win = 0

f = open("stats.txt","w") #stats
g = open("ticket.txt","w") #ticket
fjs = open("signs.json","w") # json
while(not game.run_alot()):     # this will run until lucky loser,gold or silver bonuses - can be changed in the class method
    
    c = c + 1
    stake = stake + money
    win = win + game.get_full_game_wins()

game.get_stats(f,fjs) #this will print only the last iteration,or the one that got it out of the loop
                  #for printint all iterations,include the function in the loop
game.get_ticket(g)  #a real life representation of the gambling ticket

g.close()
f.close()
fjs.close()
print(f"Total bid amount: {stake} , Won amount: {win} , Profit: {win - stake}\n")
print(f"Total games: {c}")

print("More information can be found in statistics and ticket....\n")