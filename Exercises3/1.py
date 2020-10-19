class Scoop(object):
    def __init__(self, flavour):
        self.flavour = flavour


class Bowl(object):
    max_scoops = 3

    def __init__(self):
        self.nr_scoops = 0
        self.bowl = []

    def add_scoops(self, *args):
        for one_arg in args:
            self.nr_scoops += 1

        if (self.nr_scoops <= Bowl.max_scoops):
            self.bowl += args
        else:
            print("Can't add more scoops of icecream")

    def flavours(self):
        for one_scoop in range(len(self.bowl)):
            print(self.bowl[one_scoop].flavour)


s1 = Scoop('vanilla')
s2 = Scoop('chocolate')
s3 = Scoop('strawberry')
s4 = Scoop('coffee')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s2)
b.add_scoops(s3)
b.add_scoops(s4)
b.flavours()
