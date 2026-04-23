import random, time
print ("welcome to Gladiator Battle Simulator")
print ("Your first gladiator")
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
            print(f"Your gladiators name is {Name}")
    namer()
    def forge():
        try:
            print("1,2,3,4,5,6,7,8,9,10")
            Weapon = int(input("Type which weapon you desire "))
            if Weapon <= 0 or Weapon >= 11 :
                print ("try again")
                forge()
            else:
                print (f"Your weapon is {Weapon -1}")
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
                print (f"Your armor is {Armor -1}")
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
                print (f"Your Skill is {Skill -1}")
        except ValueError:
            print ("That is not a number")
            origin()
    origin()
    def change():
        print("Now the your second gladiator")
    change()
    def battle():
        print("Welcome to the COLOSSEUM")
    battle()
master()