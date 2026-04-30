#Scrum document: https://docs.google.com/document/d/1_zBj3TbMbulobdO4XD9UXrmrTHvDDRmD4JMZqRfPbXE/edit?tab=t.0

import random, time
time.sleep(0.000000001)
print ("welcome to Gladiator Battle Simulator")
print ("Your first gladiator")
changer = 1
wa = ""
wb = ""
aa = ""
ab = ""
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
class weapon:
    def __init__(self,sub,DG):
        self.sub=sub
        self.DG=DG
Gladius = weapon('Gladius',random.randint(1,12))
Spatha = weapon('Spatha',random.randint(2,6))
Pugio = weapon('Pugio',random.randint(2,4))
Hasta = weapon('Hasta',random.randint(2,8))
Fascina = weapon('Fascina',random.randint(2,6))
Semispatha = weapon('Semispatha',random.randint(3,4))
Lancea = weapon('Lancea',10)
Sica = weapon('Sica',random.randint(3,6))
Pilum = weapon('Pilum',random.randint(1,12))
Arcus = weapon('Arcus',random.randint(3,4))
weaplist = ["Gladius","Spatha","Pugio","Hasta","Fascina","Semispatha","Lancea","Sica","Pilum","Arcus"]
def master():
    class Gladi:
        def __init__(self,title,health,damage,fAC,back):
            self.title=title
            self.health=health
            self.damage=damage
            self.fAC=fAC
            self.back=back
    fighter1 = Gladi(0,100,0,0,0)
    fighter2 = Gladi(0,100,0,0,0)
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
                    print(f"Your 1st gladiator, {fighter1.title}s weapon is {weaplist[Weapon - 1]}")
                    global wa
                    wa = weaplist[Weapon - 1]
                    if Weapon == 1:
                        fighter1.damage = Gladius.DG
                    if Weapon == 2:
                        fighter1.damage = Spatha.DG
                    if Weapon == 3:
                        fighter1.damage = Pugio.DG
                    if Weapon == 4:
                        fighter1.damage = Hasta.DG
                    if Weapon == 5:
                        fighter1.damage = Fascina.DG
                    if Weapon == 6:
                        fighter1.damage = Semispatha.DG
                    if Weapon == 7:
                        fighter1.damage = Lancea.DG
                    if Weapon == 8:
                        fighter1.damage = Sica.DG
                    if Weapon == 9:
                        fighter1.damage = Pilum.DG
                    if Weapon == 10:
                        fighter1.damage = Arcus.DG
                else:
                    print(f"Your 2nd gladiator, {fighter1.title}s weapon is {weaplist[Weapon - 1]}")
                    global wb
                    wb = weaplist[Weapon - 1]
                    if Weapon == 1:
                        fighter2.damage = Gladius.DG
                    if Weapon == 2:
                        fighter2.damage = Spatha.DG
                    if Weapon == 3:
                        fighter2.damage = Pugio.DG
                    if Weapon == 4:
                        fighter2.damage = Hasta.DG
                    if Weapon == 5:
                        fighter2.damage = Fascina.DG
                    if Weapon == 6:
                        fighter2.damage = Semispatha.DG
                    if Weapon == 7:
                        fighter2.damage = Lancea.DG
                    if Weapon == 8:
                        fighter2.damage = Sica.DG
                    if Weapon == 9:
                        fighter2.damage = Pilum.DG
                    if Weapon == 10:
                        fighter2.damage = Arcus.DG
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
                    global aa
                    aa = lister[Armor - 1]
                    if Armor == 1:
                        fighter1.fAC = Leather.AC
                    if Armor == 2:
                        fighter1.fAC = Iron.AC
                    if Armor == 3:
                        fighter1.fAC = Samurai.AC
                    if Armor == 4:
                        fighter1.fAC = Overgrown.AC
                    if Armor == 5:
                        fighter1.fAC = Champion.AC
                    if Armor == 6:
                        fighter1.fAC = Radiant.AC
                    if Armor == 7:
                        fighter1.fAC = Ninja.AC
                    if Armor == 8:
                        fighter1.fAC = Cursed.AC
                    if Armor == 9:
                        fighter1.fAC = Charge.AC
                    if Armor == 10:
                        fighter1.fAC = Tank.AC
                else:
                    print(f"Your 2nd gladiators, {fighter2.title}s armor is {lister[Armor - 1]}")
                    global ab
                    ab = lister[Armor - 1]
                    if Armor == 1:
                        fighter2.fAC = Leather.AC
                    if Armor == 2:
                        fighter2.fAC = Iron.AC
                    if Armor == 3:
                        fighter2.fAC = Samurai.AC
                    if Armor == 4:
                        fighter2.fAC = Overgrown.AC
                    if Armor == 5:
                        fighter2.fAC = Champion.AC
                    if Armor == 6:
                        fighter2.fAC = Radiant.AC
                    if Armor == 7:
                        fighter2.fAC = Ninja.AC
                    if Armor == 8:
                        fighter2.fAC = Cursed.AC
                    if Armor == 9:
                        fighter2.fAC = Charge.AC
                    if Armor == 10:
                        fighter2.fAC = Tank.AC
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
        print(fighter1.title, wa, aa, fighter1.back)
        print(fighter2.title, wb, ab, fighter2.back)
    battle()
master()