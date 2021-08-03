class Pet:
    def __init__(self, name, type, tricks) -> None:
        self.name = name
        self.type = type
        self.tricks = tricks
    
    energy = 100
    health = 100

    def sleep(self):
        print("sleeping")
        self.energy += 25

    def eat(self):
        print("eating")
        self.energy += 5
        self.health += 10

    def play(self):
        print("playing, from Ninja walk()")
        self.health += 5

    def noise(self):
        print(self.type)
        if self.type == "Dog":
            print("Wuff")
        elif self.type == "Cat":
            print("Meow")
        else:
            print("I have no idea")


class Ninja:
    def __init__(self, fname, lname, treats, pet_food, pet) -> None:
        self.first_name = fname
        self.last_name = lname
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        	
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

daniel = Ninja("Daniel", "Shoemaker", "Bones", "Soft", Pet("Bear", "Bird", "None"))
daniel.feed().walk().bathe()