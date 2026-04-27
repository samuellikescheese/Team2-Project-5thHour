# Hi I'm Aiden and I will be making the armor.
import random
def Aiden():
    class armor:
        def __init__(self,name,AC):
            self.name=name
            self.AC=AC
    Leather = armor('Leather',13)
    Iron = armor('Iron',15)
    Samurai = armor('Samurai',15)
    Overgrown = armor('Overgrown',11)
    Champion = armor('Champion',14)
    Radiant = armor('Radiant',13)
    Ninja = armor('Ninja',12)
    Cursed = armor('Cursed',16)
    Charge = armor('Charge',13)
    Tank = armor('Tank',8)

global Cursed
#dodge is for leather, only happens when a hit is above AC to give a second chance
def dodge():
    #if opponents attack hits
        dodgevar = random.randint(1,6)
        if dodgevar == 1:
            #code for opponent attack failing
            print("The attack was dodged!")
        else:
            #take damage

#resistance is for iron, only happens when hit is landed, allows for less damage to be taken
def resistance():
    #if opponents attack hits
        resistancevar = random.randint(0,10)
        #make resistance be taken away from damage taken
        print(f"{resistancevar} damage was stopped by the armor!")

#counter is for samurai, only happens when hit is missed, but does not count as the wearer's turn.
def counter():
    #if opponents attack misses
        countervar = random.randint(1,3)
        if countervar == 1:
            #code for attack
            print("The attack was countered!")
    #if attack hits
        #take damage

#thorns is for overgrown, only happens when hit is landed, can force damage upon opponent, but does not count as the wearer's turn.
def thorns():
    #if opponents attack hits
        #take damage
        thornsvar = random.randint(0,5)
        #code for attacker to take thorns damage
        print(f"The armor has given {thornsvar} damage!")

#rage is only for champion, gives the wearer hightened AC when on lower health
def rage():
    #if statement stating if the wearer's HP is 10 or below
        #code for AC to be raised by 1
        print("Sudden rage has given an AC increase of 3!")
    #elif statement stating if the wearer's HP is 25 or below
        #code for AC to be raised by 1
        print("Sudden rage has given an AC increase of 2!")
    #if opponents attack hits
        #take damage

#heal is only for radiant, allowing for the wearer to regain health if an attack is missed
def heal():
    #if opponents attack misses
        healvar = random.randint(0,10)
        #add healvar to health
        print(f"The missed attack has given an oprotunity to replinish {healvar} health!")
    #if opponents attack hits
        #take damage

#hide is only for ninja, giving the opponent a lower attack score
def hide():
    hidevar = random.randint(0,4)
    #take hidevar away from opponent's attack roll
    #if opponents attack misses
        print("The attack has missed!")
    #if opponents attack hits
        #take damage

#change is only for cursed, swapping the AC of itself
def change():
    changeAC = [6,16]
    random.shuffle(changeAC)
    newAC = changeAC[0]
    Cursed.AC = newAC
    #if opponents attack hits
        #take damage

#absorb is only for charge, allowing for the wearer's next attack to deal more damage if a hit is taken
def absorb():
    #if statement for if attack hits
        #take damage
        absorbvar = random.randint(1,7)
        #add absorbvar to next attack
        print(f"The armor has absorbed {absorbvar} damage, allowing the next strike to deal more damage!")

#adjust is only for tank, allowing for the wearer to gain or lose AC depending on if the attack has missed or succeeded
def adjust():
    #if opponents attack hits
        #take damage
        #add 2 AC to the armor
        print("Defence has been adjusted!")
    #if opponents attack misses
        #subtract 2 AC to the armor
        print("Defence has been adjusted!")