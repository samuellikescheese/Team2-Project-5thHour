print ("welcome to Gladiator Battle Simulator")
def master():
    def namer():
        Name = input("Type your gladiators Name ")
        print(f"your gladiators name is {Name}")
    namer()
    def forge():
        try:
            print("1,2,3,4,5,6,7,8,9,10")
            Weapon = int(input("Type which weapon you desire "))
            if Weapon <= 0 or Weapon >= 11 :
                print ("try again")
                forge()
            else:
                print (Weapon -1)
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
                print (Armor -1)
        except ValueError:
            print ("That is not a number")
            smith()
    smith()
    def origin():
        try:
            print("1,2,3,4,5,6,7,8,9,10")
            Skill = int(input("Type which armor you desire "))
            if Skill <= 0 or Skill >= 11 :
                print ("try again")
                origin()
            else:
                print (Skill -1)
        except ValueError:
            print ("That is not a number")
            origin()
    origin()
master()