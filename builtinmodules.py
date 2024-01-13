import random

#for i in range(3):
    #print(random.random())

#for i in range(3):
    #print(random.random(10, 20))

#members = ["John", "Mary", "Bob", "Gadwen"]
#leader = random.choice(members)
#print(leader)


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(f"The numbers are {dice.roll()}")