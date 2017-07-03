import random

def rungame(game):
    car = random.randint(1,3)
    guess = random.randint(1,3)

    if car == guess:        
        d = [1,2,3]
        d.remove(car)
        reveal = random.choice(d)
    else:
        d = [1,2,3]
        d.remove(car)
        d.remove(guess)
        reveal = d[0]

    if game == "stick":     #What happens if we stick
        if guess == car:
            result = 1      # If we win return a 1
        else:
            result = 0      # If we loose return 0
        return result    
    else:                   #What happens if we switch
        d = [1,2,3]         
        d.remove(reveal)    
        d.remove(guess)     #Remove our current guess
        if d[0] == car:
            result = 1      #won
        else:
            result = 0      #lost
        return result

stick = 0
switch = 0
num_of_games = int(raw_input("How many games? "))
          
if __name__ == '__main__':

    for game in range(0,num_of_games):
        stick = stick + rungame("stick")
        switch = switch + rungame("switch")
    print "The result for stick is a %s%% win rate, the result for switch is a %s%% win rate out of %s games." % (float(stick) / float(num_of_games) * 100, float(switch) / float(num_of_games) * 100, num_of_games) 
