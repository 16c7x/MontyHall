
import MontyHall

stick = 0
switch = 0
#num_of_games = int(raw_input("How many games? ")) # Use this for intereactive
num_of_games = 1000000 # use this to run in Atom Runner.

for games in range(0,num_of_games):
    stick = stick + MontyHall.Game().rungame("stick")
    switch = switch + MontyHall.Game().rungame("switch")
print "The result for stick is a %s%% win rate, the result for switch is a %s%% win rate out of %s games." % (float(stick) / float(num_of_games) * 100, float(switch) / float(num_of_games) * 100, num_of_games)
