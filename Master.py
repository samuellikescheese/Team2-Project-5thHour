import random, time
print ("welcome to Gladiator Battle Simulator")
print ("Your first gladiator")
changer = 1
def master():
    class Gladi:
        def __init__(self,title,damage,defence,back):
            self.title=title
            self.damage=damage
            self.defence=defence
            self.back=back
    fighter1 = Gladi(0,0,0,0)
    fighter2 = Gladi(0,0,0,0)
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
                    print(f"Your 1st gladiator, {fighter1.title}s armor is {Armor - 1}")
                    fighter1.defence = Armor
                else:
                    print(f"Your 2nd gladiators, {fighter2.title}s armor is {Armor - 1}")
                    fighter2.defence = Armor
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