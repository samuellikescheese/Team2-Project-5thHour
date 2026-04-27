#Scrum document: https://docs.google.com/document/d/1_zBj3TbMbulobdO4XD9UXrmrTHvDDRmD4JMZqRfPbXE/edit?tab=t.0

import random, time
print ("welcome to Gladiator Battle Simulator")
print ("Your first gladiator")
changer = 1
class armor:
    def __init__(self,sub,AC):
        self.sub=sub
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
lister = ["Leather","Iron","Samurai","Overgrown","Champion","Radiant","Ninja","Cursed","Charge","Tank"]
def master():
    class Gladi:
        def __init__(self,title,damage,defence,back):
            self.title=title
            self.damage=damage
            self.defence=defence
            self.back=back
    fighter1 = Gladi(0,0,0,0)
    fighter2 = Gladi(0,0,0,0)
    fighter1.damage = 5
    fighter2.damage = 5
    def namer():
        Name = input("Type your gladiators Name ")
        if Name == "":
            print("Thats not a name")
            namer()
        else:
            if changer == 1:
                print(f"Your 1st gladiators name is {Name}")
                fighter1.title = Name
            else:
                print(f"Your 2nd gladiators name is {Name}")
                fighter2.title = Name
    namer()
    def forge():
        try:
            print("1,2,3,4,5,6,7,8,9,10")
            Weapon = int(input("Type which weapon you desire "))
            if Weapon <= 0 or Weapon >= 11 :
                print ("try again")
                forge()
            else:
                if changer == 1:
                    print(f"Your 1st gladiator, {fighter1.title}s weapon is {Weapon - 1}")
                    fighter1.damage = Weapon
                else:
                    print(f"Your 2nd gladiators, {fighter2.title}s weapon is {Weapon - 1}")
                    fighter2.damage = Weapon
        except ValueError:
            print ("That is not a number")
            forge()
    forge()
    def smith():
        try:
            print("1,2,3,4,5,6,7,8,9,10")
            Armor = int(input("Type which armor you desire "))
            if Armor <= 0 or Armor >= 11 :
                print ("try again")
                smith()
            else:
                if changer == 1:
                    print(f"Your 1st gladiator, {fighter1.title}s armor is {lister[Armor - 1]}")
                    if Armor == 1:
                        fighter1.defence = Leather.AC
                    if Armor == 2:
                        fighter1.defence = Iron.AC
                    if Armor == 3:
                        fighter1.defence = Samurai.AC
                    if Armor == 4:
                        fighter1.defence = Overgrown.AC
                    if Armor == 5:
                        fighter1.defence = Champion.AC
                    if Armor == 6:
                        fighter1.defence = Radiant.AC
                    if Armor == 7:
                        fighter1.defence = Ninja.AC
                    if Armor == 8:
                        fighter1.defence = Cursed.AC
                    if Armor == 9:
                        fighter1.defence = Charge.AC
                    if Armor == 10:
                        fighter1.defence = Tank.AC
                else:
                    print(f"Your 2nd gladiators, {fighter2.title}s armor is {lister[Armor - 1]}")
                    if Armor == 1:
                        fighter2.defence = Leather.AC
                    if Armor == 2:
                        fighter2.defence = Iron.AC
                    if Armor == 3:
                        fighter2.defence = Samurai.AC
                    if Armor == 4:
                        fighter2.defence = Overgrown.AC
                    if Armor == 5:
                        fighter2.defence = Champion.AC
                    if Armor == 6:
                        fighter2.defence = Radiant.AC
                    if Armor == 7:
                        fighter2.defence = Ninja.AC
                    if Armor == 8:
                        fighter2.defence = Cursed.AC
                    if Armor == 9:
                        fighter2.defence = Charge.AC
                    if Armor == 10:
                        fighter2.defence = Tank.AC
        except ValueError:
            print ("That is not a number")
            smith()
    smith()
    def origin():
        try:
            print("1,2,3,4,5,6,7,8,9,10")
            Skill = int(input("Type which skill you desire "))
            if Skill <= 0 or Skill >= 11 :
                print ("try again")
                origin()
            else:
                if changer == 1:
                    print(f"Your 1st gladiator, {fighter1.title}s skill is {Skill - 1}")
                    fighter1.back = Skill
                else:
                    print(f"Your 2nd gladiators, {fighter2.title}s skill is {Skill - 1}")
                    fighter2.back = Skill
        except ValueError:
            print ("That is not a number")
            origin()
    origin()
    def change():
        print("Now the your second gladiator")
        global changer
        changer = 2
        namer()
        forge()
        smith()
        origin()
    change()
    def battle():
        print("Welcome to the COLOSSEUM")
        print(fighter1.title, fighter1.damage, fighter1.defence, fighter1.back)
        print(fighter2.title, fighter2.damage, fighter2.defence, fighter2.back)
    battle()
master()