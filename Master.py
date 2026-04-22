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
        except ValueError:
            print ("That is not a number")
            forge()
        finally:
            print (Weapon -1)
    forge()
    def smith():
        try:
            print("1,2,3,4,5,6,7,8,9,10")
            Armor = int(input("Type which armor you desire "))
            if Armor <= 0 or Armor >= 11 :
                print ("try again")
                smith()
        except ValueError:
            print ("That is not a number")
            smith()
        finally:
            print (Armor -1)
    smith()
master()