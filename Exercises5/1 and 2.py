class Scoop(object):
    def __init__(self, flavour):
        self.flavour = flavour

    def __repr__(self):
        return f"Scoop of {self.flavour}"


class Bowl(object):
    max_scoops = 3

    def __init__(self):
        self.nr_scoops = 0
        self.bowl = []

    def add_scoops(self, *args):
        for one_arg in args:
            self.nr_scoops += 1

        if (self.nr_scoops <= self.max_scoops):
            self.bowl += args
        else:
            print("Can't add more scoops of icecream")

    def flavours(self):
        for one_scoop in range(len(self.bowl)):
            print(self.bowl[one_scoop].flavour)

    def __len__(self):
        return len(self.bowl)

    def __repr__(self):
        output = 'Bowl with: \n'
        output += '\n'.join(f"\t{index}) {one_scoop}"
                            for index, one_scoop in enumerate(self.bowl, 1))

        return output


class BigBowl(Bowl):
    max_scoops = 5


s1 = Scoop('vanilla')
s2 = Scoop('chocolate')
s3 = Scoop('strawberry')
s4 = Scoop('coffee')
s5 = Scoop('flavour 5')
s6 = Scoop('flavour 6')
my_list = [s1, s2]
# print(my_list)

b = Bowl()
b.add_scoops(s1, s2, s3)
# b.flavours()
# print(len(b))
# print(b)

bb = BigBowl()
bb.add_scoops(s1, s2, s3, s4, s5)
# bb.flavours()
# print(len(bb))
print(bb)
