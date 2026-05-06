#Scrum document: https://docs.google.com/document/d/1_zBj3TbMbulobdO4XD9UXrmrTHvDDRmD4JMZqRfPbXE/edit?tab=t.0

import random, time
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
    def __init__(self,sub,DG,Atkmod):
        self.sub=sub
        self.DG=DG
        self.Atkmod=Atkmod
Gladius = weapon('Gladius',random.randint(1,12),3)
Spatha = weapon('Spatha',random.randint(1,6) + random.randint(1,6),2)
Pugio = weapon('Pugio',random.randint(1,4) + random.randint(1,4),4)
Hasta = weapon('Hasta',random.randint(1,8) + random.randint(1,8),1)
Fascina = weapon('Fascina',random.randint(1,6) + random.randint(1,6),3)
Semispatha = weapon('Semispatha',random.randint(1,4) + random.randint(1,4) + random.randint(1,4),3)
Lancea = weapon('Lancea',10,5)
Sica = weapon('Sica',random.randint(1,6) + random.randint(1,6) + random.randint(1,6),1)
Pilum = weapon('Pilum',random.randint(1,12),2)
Arcus = weapon('Arcus',random.randint(1,4),0)
weaplist = ["Gladius","Spatha","Pugio","Hasta","Fascina","Semispatha","Lancea","Sica","Pilum","Arcus"]
def master():
    class Gladi:
        def __init__(self,title,health,damage,fAC,WN,AN,cheese):
            self.title=title
            self.health=health
            self.damage=damage
            self.fAC=fAC
            self.WN=WN
            self.AN=AN
            self.cheese=cheese
    fighter1 = Gladi(0,50,0,0,"","",0)
    fighter2 = Gladi(0,50,0,0,"","",0)
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
                        fighter1.cheese = Gladius.Atkmod
                    if Weapon == 2:
                        fighter1.damage = Spatha.DG
                        fighter1.cheese = Spatha.Atkmod
                    if Weapon == 3:
                        fighter1.damage = Pugio.DG
                        fighter1.cheese = Pugio.Atkmod
                    if Weapon == 4:
                        fighter1.damage = Hasta.DG
                        fighter1.cheese = Hasta.Atkmod
                    if Weapon == 5:
                        fighter1.damage = Fascina.DG
                        fighter1.cheese = Fascina.Atkmod
                    if Weapon == 6:
                        fighter1.damage = Semispatha.DG
                        fighter1.cheese = Semispatha.Atkmod
                    if Weapon == 7:
                        fighter1.damage = Lancea.DG
                        fighter1.cheese = Lancea.Atkmod
                    if Weapon == 8:
                        fighter1.damage = Sica.DG
                        fighter1.cheese = Sica.Atkmod
                    if Weapon == 9:
                        fighter1.damage = Pilum.DG
                        fighter1.cheese = Pilum.Atkmod
                    if Weapon == 10:
                        fighter1.damage = Arcus.DG
                        fighter1.cheese = Arcus.Atkmod
                else:
                    print(f"Your 2nd gladiator, {fighter1.title}s weapon is {weaplist[Weapon - 1]}")
                    global wb
                    wb = weaplist[Weapon - 1]
                    if Weapon == 1:
                        fighter2.damage = Gladius.DG
                        fighter2.cheese = Gladius.Atkmod
                    if Weapon == 2:
                        fighter2.damage = Spatha.DG
                        fighter2.cheese = Spatha.Atkmod
                    if Weapon == 3:
                        fighter2.damage = Pugio.DG
                        fighter2.cheese = Pugio.Atkmod
                    if Weapon == 4:
                        fighter2.damage = Hasta.DG
                        fighter2.cheese = Hasta.Atkmod
                    if Weapon == 5:
                        fighter2.damage = Fascina.DG
                        fighter2.cheese = Fascina.Atkmod
                    if Weapon == 6:
                        fighter2.damage = Semispatha.DG
                        fighter2.cheese = Semispatha.Atkmod
                    if Weapon == 7:
                        fighter2.damage = Lancea.DG
                        fighter2.cheese = Lancea.Atkmod
                    if Weapon == 8:
                        fighter2.damage = Sica.DG
                        fighter2.cheese = Sica.Atkmod
                    if Weapon == 9:
                        fighter2.damage = Pilum.DG
                        fighter2.cheese = Pilum.Atkmod
                    if Weapon == 10:
                        fighter2.damage = Arcus.DG
                        fighter2.cheese = Arcus.Atkmod
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
    def change():
        print("Now the your second gladiator")
        global changer
        changer = 2
        namer()
        forge()
        smith()
    change()
    def battle():
        print("Welcome to the COLOSSEUM")
        print(fighter1.title, wa, aa)
        print(fighter2.title, wb, ab)
        roll1 = random.randint(1, 20)
        roll2 = random.randint(1, 20)
        print(f"{fighter1.title} VS {fighter2.title}")
        time.sleep(0.5)
        if roll1 >= roll2:
            while 5 > 3:
                print(f"{fighter1.title} attacks {fighter2.title}")
                time.sleep(0.5)
                hero = random.randint(1, 20)
                evil = random.randint(1, 20)
                if fighter1.WN == "Gladius":
                    fighter1.damage = random.randint(1,12)
                elif fighter1.WN == "Spatha":
                    fighter1.damage = random.randint(1,6) + random.randint(1,6)
                elif fighter1.WN == "Pugio":
                    fighter1.damage = random.randint(1,4) + random.randint(1,4)
                elif fighter1.WN == "Hasta":
                    fighter1.damage = random.randint(1,8) + random.randint(1,8)
                elif fighter1.WN == "Fascina":
                    fighter1.damage = random.randint(1,6) + random.randint(1,6)
                elif fighter1.WN == "Semispatha":
                    fighter1.damage = random.randint(1,4) + random.randint(1,4) + random.randint(1,4)
                elif fighter1.WN == "Lancea":
                    fighter1.damage = 10
                elif fighter1.WN == "Sica":
                    fighter1.damage = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
                elif fighter1.WN == "Pilum":
                    fighter1.damage = random.randint(1,12)
                elif fighter1.WN == "Arcus":
                    fighter1.damage = random.randint(1,4)
                if fighter2.WN == "Gladius":
                    fighter2.damage = random.randint(1,12)
                elif fighter2.WN == "Spatha":
                    fighter2.damage = random.randint(1,6) + random.randint(1,6)
                elif fighter2.WN == "Pugio":
                    fighter2.damage = random.randint(1,4) + random.randint(1,4)
                elif fighter2.WN == "Hasta":
                    fighter2.damage = random.randint(1,8) + random.randint(1,8)
                elif fighter2.WN == "Fascina":
                    fighter2.damage = random.randint(1,6) + random.randint(1,6)
                elif fighter2.WN == "Semispatha":
                    fighter2.damage = random.randint(1,4) + random.randint(1,4) + random.randint(1,4)
                elif fighter2.WN == "Lancea":
                    fighter2.damage = 10
                elif fighter2.WN == "Sica":
                    fighter2.damage = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
                elif fighter2.WN == "Pilum":
                    fighter2.damage = random.randint(1,12)
                elif fighter2.WN == "Arcus":
                    fighter2.damage = random.randint(1,4)
                if not hero == 1 or hero + fighter1.cheese >= fighter2.fAC or hero == 20:
                    fighter2.health -= fighter1.damage
                    if fighter2.health <= 0:
                        print(f"{fighter2.title} is dead")
                        exit()
                    else:
                        print(f"{fighter2.title} stands")
                        time.sleep(0.5)
                else:
                    print("he misses")
                    time.sleep(0.5)
                print(f"{fighter2.title} attacks")
                time.sleep(0.5)
                if not evil == 1 or evil + fighter2.cheese >= fighter1.fAC or evil == 20:
                    fighter1.health -= fighter2.cheese
                    if fighter1.health <= 0:
                        print(f"{fighter1.title} is dead")
                        exit()
                    else:
                        print(f"{fighter1.title} stands")
                        time.sleep(0.5)
                else:
                    print("he misses")
                    time.sleep(0.5)
        if roll2 > roll1:
            while 5 > 3:
                if fighter1.WN == "Gladius":
                    fighter1.damage = random.randint(1,12)
                elif fighter1.WN == "Spatha":
                    fighter1.damage = random.randint(1,6) + random.randint(1,6)
                elif fighter1.WN == "Pugio":
                    fighter1.damage = random.randint(1,4) + random.randint(1,4)
                elif fighter1.WN == "Hasta":
                    fighter1.damage = random.randint(1,8) + random.randint(1,8)
                elif fighter1.WN == "Fascina":
                    fighter1.damage = random.randint(1,6) + random.randint(1,6)
                elif fighter1.WN == "Semispatha":
                    fighter1.damage = random.randint(1,4) + random.randint(1,4) + random.randint(1,4)
                elif fighter1.WN == "Lancea":
                    fighter1.damage = 10
                elif fighter1.WN == "Sica":
                    fighter1.damage = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
                elif fighter1.WN == "Pilum":
                    fighter1.damage = random.randint(1,12)
                elif fighter1.WN == "Arcus":
                    fighter1.damage = random.randint(1,4)
                if fighter2.WN == "Gladius":
                    fighter2.damage = random.randint(1,12)
                elif fighter2.WN == "Spatha":
                    fighter2.damage = random.randint(1,6) + random.randint(1,6)
                elif fighter2.WN == "Pugio":
                    fighter2.damage = random.randint(1,4) + random.randint(1,4)
                elif fighter2.WN == "Hasta":
                    fighter2.damage = random.randint(1,8) + random.randint(1,8)
                elif fighter2.WN == "Fascina":
                    fighter2.damage = random.randint(1,6) + random.randint(1,6)
                elif fighter2.WN == "Semispatha":
                    fighter2.damage = random.randint(1,4) + random.randint(1,4) + random.randint(1,4)
                elif fighter2.WN == "Lancea":
                    fighter2.damage = 10
                elif fighter2.WN == "Sica":
                    fighter2.damage = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
                elif fighter2.WN == "Pilum":
                    fighter2.damage = random.randint(1,12)
                elif fighter2.WN == "Arcus":
                    fighter2.damage = random.randint(1,4)
                print(f"{fighter2.title} attacks")
                time.sleep(0.5)
                hero = random.randint(1, 20)
                evil = random.randint(1, 20)
                if not evil == 1 or evil + fighter2.cheese >= fighter1.fAC or evil == 20:
                    fighter1.health -= fighter2.cheese
                    if fighter1.health <= 0:
                        print(f"{fighter1.title} is dead")
                        exit()
                    else:
                        print(f"{fighter1.title} stands")
                        time.sleep(0.5)
                else:
                    print("he misses")
                    time.sleep(0.5)
                print(f"{fighter1.title} attacks {fighter2.title}")
                time.sleep(0.5)
                if not hero == 1 or hero + fighter1.cheese >= fighter2.fAC or hero == 20:
                    fighter2.health -= fighter1.damage
                    if fighter2.health <= 0:
                        print(f"{fighter2.title} is dead")
                        exit()
                    else:
                        print(f"{fighter2.title} stands")
                        time.sleep(0.5)
                else:
                    print("he misses")
                    time.sleep(0.5)
    battle()
master()