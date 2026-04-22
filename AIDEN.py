# Hi I'm Aiden and I will be making the armor.
import random
def Aiden():
    class armor:
        def __init__(self,name,AC):
            self.name=name
            self.AC=AC
    Leather = armor('Leather',13)
    Iron = armor('Iron',17)
    Samurai = armor('Samurai',15)
    Overgrown = armor('Overgrown',11)
    Champion = armor('Champion',14)
    Radiant = armor('Radiant',13)

#dodge is for leather, only happens when a hit is above AC to give a second chance
def dodge():
    dodgevar = random.randint(1,6)
    if dodgevar == 1:
        #code for opponent attack failing

#resistance is for iron, only happens when hit is landed, allows for less damage to be taken
def resistance():
    resistancevar = random.randint(0,10)
    #make resistance be taken away from damage taken

#counter is for samurai, only happens when hit is missed, but does not count as the wearer's turn.
def counter():
    countervar = random.randint(1,3)
    if countervar == 1:
        #code for attack

#thorns is for overgrown, only happens when hit is landed, can force damage upon opponent, but does not count as the wearer's turn.
def thorns():
    thornsvar = random.randint(0,5)
    #code for attacker to take thorns damage

#rage is only for champion, gives the wearer hightened AC when on lower health
def rage():
    #if statement stating if the wearer's HP is 10 or below
        #code for AC to be raised by 3
    #if statement stating if the wearer's HP is 25 or below
        #code for AC to be raised by 2

#heal is only for radiant, allowing for the wearer to regain health if an attack is missed
def heal():
    healvar = random.randint(0,10)
    #add healvar to health