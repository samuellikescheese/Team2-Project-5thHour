from Master import *

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
def dodge(arm):
    if arm == 1:
        if secondattack >= fighter1.AC:
            dodgevar = random.randint(1,6)
            if dodgevar == 1:
                print("The attack was dodged!")
            else:
                fighter1.health -= fighter2.damage
    else:
        if firstattack >= fighter2.AC:
            dodgevar = random.randint(1,6)
            if dodgevar == 1:
                print("The attack was dodged!")
            else:
                fighter2.health -= fighter1.damage

#resistance is for iron, only happens when hit is landed, allows for less damage to be taken
def resistance(arm):
    if arm == 1:
        if secondattack >= fighter1.AC:
            resistancevar = random.randint(0,10)
            fighter2.damage -= resistancevar
            fighter1.health -= fighter2.damage
            print(f"{resistancevar} damage was stopped by the armor!")
    else:
        if firstattack >= fighter2.AC:
            resistancevar = random.randint(0,10)
            fighter1.damage -= resistancevar
            fighter2.health -= fighter1.damage

#counter is for samurai, only happens when hit is missed
def counter(arm):
    if arm == 1:
        if secondattack < fighter1.AC:
            countervar = random.randint(1,3)
            if countervar == 1:
                fighter2.health -= fighter1.damage
                print("The attack was countered!")
        else:
            fighter1.health -= fighter2.damage
    else:
        if firstattack < fighter2.AC:
            countervar = random.randint(1,3)
            if countervar == 1:
                fighter1.health -= fighter2.damage
                print("The attack was countered!")
        else:
            fighter2.health -= fighter1.damage

#thorns is for overgrown, only happens when hit is landed, can force damage upon opponent, but does not count as the wearer's turn.
def thorns(arm):
    if arm == 1:
        if secondattack >= fighter1.AC:
            fighter1.health -= fighter2.damage
            thornsvar = random.randint(0,5)
            fighter2.health -= thornsvar
            print(f"The armor has given {thornsvar} damage!")
    else:
        if firstattack >= fighter2.AC:
            fighter2.health -= fighter1.damage
            thornsvar = random.randint(0,5)
            fighter1.health -= thornsvar
            print(f"The armor has given {thornsvar} damage!")

#rage is only for champion, gives the wearer hightened AC when on lower health
def rage(arm):
    if arm == 1:
        if fighter1.health <= 10:
            fighter1.AC += 1
            print("Sudden rage has given an AC increase of 1!")
        elif fighter1.health <= 25:
            fighter1.AC += 1
            print("Sudden rage has given an AC increase of 1!")
        if secondattack >= fighter1.AC:
            fighter1.health -= fighter2.damage
    else:
        if fighter2.health <= 10:
            fighter2.AC += 1
            print("Sudden rage has given an AC increase of 1!")
        elif fighter2.health <= 25:
            fighter2.AC += 1
            print("Sudden rage has given an AC increase of 1!")
        if firstattack >= fighter2.AC:
            fighter2.health -= fighter1.damage

#heal is only for radiant, allowing for the wearer to regain health if an attack is missed
def heal(arm):
    if arm == 1:
        if secondattack >= fighter1.AC:
            healvar = random.randint(0,10)
            fighter1.health += healvar
            print(f"The missed attack has given an oprotunity to replinish {healvar} health!")
        else:
            fighter1.health -= fighter2.damage
    else:
        if firstattack >= fighter2.AC:
            healvar = random.randint(0,10)
            fighter2.health += healvar
            print(f"The missed attack has given an oprotunity to replinish {healvar} health!")
        else:
            fighter2.health -= fighter1.damage

#hide is only for ninja, giving the opponent a lower attack score
def hide(arm):
    if arm == 1:
        hidevar = random.randint(0,4)
        secondattack -= hidevar
        if secondattack < fighter1.AC:
            print("The attack has missed!")
        else:
            fighter1.health -= fighter2.damage
    else:
        hidevar = random.randint(0, 4)
        firstattack -= hidevar
        if firstattack < fighter2.AC:
            print("The attack has missed!")
        else:
            fighter2.health -= fighter1.damage

#change is only for cursed, swapping the AC of itself
def change(arm):
    if arm == 1:
        changeAC = [6,16]
        random.shuffle(changeAC)
        newAC = changeAC[0]
        Cursed.AC = newAC
        if secondattack >= fighter1.AC:
            fighter1.health -= fighter2.damage
    else:
        changeAC = [6, 16]
        random.shuffle(changeAC)
        newAC = changeAC[0]
        Cursed.AC = newAC
        if firstattack >= fighter2.AC:
            fighter2.health -= fighter1.damage

#absorb is only for charge, allowing for the wearer's next attack to deal more damage if a hit is taken
def absorb(arm):
    if arm == 1:
        if secondattack >= fighter1.AC:
            figher1.health -= fighter2.damage
            absorbvar = random.randint(1,7)
            fighter1.damage += absorbvar
            print(f"The armor has absorbed {absorbvar} damage, allowing the next strike to deal more damage!")
    else:
        if firstattack >= fighter2.AC:
            figher2.health -= fighter1.damage
            absorbvar = random.randint(1,7)
            fighter2.damage += absorbvar
            print(f"The armor has absorbed {absorbvar} damage, allowing the next strike to deal more damage!")

#adjust is only for tank, allowing for the wearer to gain or lose AC depending on if the attack has missed or succeeded
def adjust(arm):
    if arm == 1:
        if secondattack >= fighter1.AC:
            fighter1.health -= fighter2.damage
            fighter1.AC += 2
            print("Defence has been adjusted!")
        else:
            fighter1.AC -= 2
            print("Defence has been adjusted!")
    else:
        if firstattack >= fighter2.AC:
            fighter2.health -= fighter1.damage
            fighter2.AC += 2
            print("Defence has been adjusted!")
        else:
            fighter2.AC -= 2
            print("Defence has been adjusted!")

#Battle loop
firstattack = random.randint(1,15)
secondattack = random.randint(1,15)
arm = 2
while fighter1.health >= 1 and fighter2.health >= 1:
    def attack1():
        firstattack = random.randint(1,15)
        if fighter2.armor == Leather:
            dodge(2)
        if fighter2. armor == Iron:
            resistance(2)
        if fighter2.armor == Samurai:
            counter(2)
        if fighter2.armor == Overgrown:
            thorns(2)
        if fighter2.armor == Champion:
            rage(2)
        if fighter2.armor == Radiant:
            heal(2)
        if fighter2.armor == Ninja:
            hide(2)
        if fighter2.armor == Cursed:
            change(2)
        if fighter2.armor == Charge:
            absorb(2)
        if fighter2.armor == Tank:
            adjust(2)
    def attack2():
        secondattack = random.randint(1,15)
        if fighter1.armor == Leather:
            dodge(1)
        if fighter1. armor == Iron:
            resistance(1)
        if fighter1.armor == Samurai:
            counter(1)
        if fighter1.armor == Overgrown:
            thorns(1)
        if fighter1.armor == Champion:
            rage(1)
        if fighter1.armor == Radiant:
            heal(1)
        if fighter1.armor == Ninja:
            hide(1)
        if fighter1.armor == Cursed:
            change(1)
        if fighter1.armor == Charge:
            absorb(1)
        if fighter1.armor == Tank:
            adjust(1)
    attack1()
    attack2()