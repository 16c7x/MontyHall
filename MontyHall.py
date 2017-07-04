import random

class Game:

    def rungame(self, game):
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
                return(1)       #If we win return a 1
            else:
                return(0)       #If we loose return 0
        else:                   #What happens if we switch
            d = [1,2,3]
            d.remove(reveal)
            d.remove(guess)     #Remove our current guess
            if d[0] == car:
                return(1)       #If we win return a 1
            else:
                return(0)       #If we loose return 0

if __name__ == '__main__':
    print "I can't run on my own"
