class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}!")


yuichi = Person("Yuichi Marie")
yuichi.talk()

marie = Person("Arf Arf")
marie.talk()