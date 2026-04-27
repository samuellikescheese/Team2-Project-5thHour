import random
def weapons():
    class Weapons:
        def __init__(self ,name  ,damage ):
            self.name = name
            self.damage = damage
#1 a gladius is a standard roman sword issued to the military
            gladius = Weapons("gladius" ,10)
#2 a spatha is a longer roman sword
            spatha = Weapons("spatha" ,9)

#3  a pugio is a dagger, it is useful for close combat
            pugio = Weapons("pugio" ,6)

#4 a hasta is a spear that is used as a lance
            hasta = Weapons("hasta" ,7)

#5 a fascina is a trident adapted from fishing
            fascina = Weapons("fascina" ,10)

#6 a semispartha is a half sword or shorter sword
            semispatha = Weapons("semispatha",6)

#7 a lancea is a short spear or javelin
            lancea = Weapons("lancea",8)

#8 a sica is a sword with curved blade that is better for slicing
            sica = Weapons("sica" ,9)

#9 a pilum is a spear/ javelin it is heavier than a regular javelin
            pilum = Weapons("pilum" ,7)

#10 an arcus is a standard roman bow
            arcus = Weapons("arcus",8)

def skills():
#heavy is exclusive to the spatha it is a heavy sword and has a chance to do extra damage
    def heavy():
        heavy_odds = random.randint(1,10)
        if heavy_odds % 2 == 0:
            #add plus 5 damage to attack
#bleeding is only for the pugio it is a dagger and makes the opponent bleed
    def bleeding():

        #minus 2 damage for  two rounds

#slice is exclusive to the sica it is a sword used for slicing
def slice():
    slicechance = random.randint(1,20)
        if slicechance == 1:
            #opponent is forced to miss a turn

#Flame is for Gladius only and has a 50% chance to do flame damage
def flame():
    flame_damage = random.randint(1,7)
    flame_odds = random.randint(1,10)
    if flame_odds % 2 == 0:
        #add flame damage to base damage

#Drown is for the fascina, it slows the opponent down and makes them miss a turn
def Drown():
    Drown_odds = random.randint(1,10)
    if Drown_odds == 1:
        #Skip opponents turn
#quickshot is for the arcus it makes your gladiator shoot two arrows at the enemy
def quickshot():
    qshot_damage = random.randint(1,6)
    if qshot_damage == 2:
        #double the damage done by the bow

#double poke is an attack only for the hasta it allows the gladiator to poke the enemy twice before they can react
def dpoke():
    dpokechance = random.randint(1, 5)
    if dpokechance == 1:
        #double the damage of the attack

#pilum throw is an ability where you throw the pilum instead of stab with it, it does more damage but it is unlikely
def throw():
    throwchance = random.randint(1,20)
    if throwchance == 1:
        throwdmg = 20

#tripleswipe is for the semispartha because the sword  is so light it allows the gladiator the chance to swing it three times
def triple():
    triplechance = random.randint(1,5)
    if triplechance == 1:
        #triple the damage done by the sword

#pierce is for the lancea it allows the spear to go through the opponents armor
def pierce():
    piercechance = random.randint(1,6)
    if piercechance == 1:
        #the spear goes straight through the armor