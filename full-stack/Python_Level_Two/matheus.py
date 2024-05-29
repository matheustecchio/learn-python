class Animal():
    def __init__(self, name):
        print("Animal created")
        self.name = name

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)  
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog("Maya")
d.whoAmI()
d.eat()
d.bark()
print(d.name)
