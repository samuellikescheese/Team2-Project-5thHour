import random
def speed():
    print ("you attack twice with speed")
    sped = random.randint(1,10)
speed()
def block():
    print ("you take no damage this turn")
    blck = random.randint(1,9)
def crit():
    print ("you deal double damage")
    crt = random.randint(1,20)
def healer():
    print ("you heal 1d10 hp")
    heal = random.randint(1,10)
def defend():
    print ("you take 1 less damage")
    defd = random.randint(1,10)