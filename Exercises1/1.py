class Scoop(object):
    def __init__(self, flavour):
        self.flavour = flavour


s1 = Scoop('vanilla')
s2 = Scoop('chocolate')
s3 = Scoop('strawberry')

print(s1.flavour)

for one_scoop in [s1, s2, s3]:
    print(one_scoop.flavour)
