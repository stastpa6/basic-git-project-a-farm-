#cow
#chicken
#goat
#dog
#sheep

class Animal:

    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def make_a_sound(self):
        print(f" {self.sound} ")

cow = Animal("Cow", "moo")
chicken = Animal("Chicken", "cha-caw")
goat = Animal("Goat", "maa")
dog = Animal("Dog", "woof")
sheep = Animal("Sheep", "bee")
