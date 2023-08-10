# gerador de placas
import random
import string

alph = string.ascii_uppercase

def generatePlate():
    return (random.choice(alph) + random.choice(alph) + random.choice(alph) + str(random.randint(1,9)) + random.choice(alph) + str(random.randint(1,9)) + str(random.randint(1,9)))

quantity = input("How many plates do you want to generate?\n")

for i in range(int(quantity)):
    print(generatePlate())