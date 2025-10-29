class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def sound(self):
        print("Some animal sound")

    def show_info(self):
        print("Animal's name is " + self.name)
        print("Animal's species is " + self.species)


class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion")

    def sound(self):
        print("Roar")


class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, "Elephant")

    def sound(self):
        print("Rumble")


class Snake(Animal):
    def __init__(self, name):
        super().__init__(name, "Snake")

    def sound(self):
        print("Hiss")


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def animal_info(self):
        for animal in self.animals:
            animal.show_info()
        print(f"There are {len(self.animals)} animal in the zoo")

    def all_animal_sound(self):
        for animal in self.animals:
            animal.sound()

panthera = Lion("Panthera")
indian = Elephant("Indian")
python = Snake("Python")
tiger = Animal("Devil", "Tiger")

zoo = Zoo()
zoo.add_animal(panthera)
zoo.add_animal(indian)
zoo.add_animal(python)
zoo.add_animal(tiger)

zoo.animal_info()

zoo.all_animal_sound()