class Scoop(object):
    def __init__(self, flavour):
        self.flavour = flavour


class Bowl(object):
    def __init__(self):
        self.bowl = []

    def add_scoops(self, *args):
        self.bowl += args

    def flavours(self):
        for one_scoop in range(len(self.bowl)):
            print(self.bowl[one_scoop].flavour)


s1 = Scoop('vanilla')
s2 = Scoop('chocolate')
s3 = Scoop('strawberry')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.flavours()
