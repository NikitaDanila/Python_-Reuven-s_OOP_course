class Animal(object):
    def __init__(self, color):
        self.color = color

    def __str__(self):

        return f"{self.color:6}{self.species:6}{self.legs:2} legs"


class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.species = 'wolf'
        self.legs = 4


class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.species = 'sheep'
        self.legs = 4


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.species = 'snake'
        self.legs = 0


class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.species = 'parrot'
        self.legs = 2


class Cage(object):

    def __init__(self, id_number):
        self.cage_id = id_number
        self.caged_animals = []

    def add_animals(self, *animal):
        self.caged_animals += animal

    def __str__(self):
        output = []
        output.append(f"Cage {self.cage_id}:")
        output += (['\t' + str(index) + ') ' + str(one_animal)
                    for index, one_animal in enumerate(self.caged_animals, 1)])

        return '\n'.join(output)


class Zoo(object):
    def __init__(self):
        self.cages = []

    def add_cages(self, *cage):
        self.cages += cage

    def animals_by_color(self, color):
        my_list = []
        for one_cage in self.cages:
            for index, one_animal in enumerate(one_cage.caged_animals, 1):
                if one_animal.color == color:
                    my_list.append(f"{index}) {one_animal}")
        return '\n'.join(my_list)

    def number_of_legs(self):
        total = 0
        for one_cage in self.cages:
            for one_animal in one_cage.caged_animals:
                total += one_animal.legs

        return f"The total number of legs is: {total}"

    def __str__(self):
        return '\n'.join([str(one_cage) for one_cage in self.cages])


wolf = Wolf('black')            # species, color, # legs
sheep1 = Sheep('white')
sheep2 = Sheep('white')
snake = Snake('brown')
parrot = Parrot('black')

# print(wolf)  # black wolf, 4 legs
# print(sheep1)  # white sheep, 4 legs
# print(sheep2)  # white sheep, 4 legs
# print(snake)  # brown snake, 0 legs
# print(parrot)  # black parrot, 2 legs

c1 = Cage(1)   # ID numbers
c2 = Cage(2)

c1.add_animals(wolf, sheep1, sheep2)
c2.add_animals(snake, parrot)
# print(c1)
# print(c2)
z = Zoo()
z.add_cages(c1, c2)
print(z)

# print(z.animals_by_color('black'))
# print(z.number_of_legs())
