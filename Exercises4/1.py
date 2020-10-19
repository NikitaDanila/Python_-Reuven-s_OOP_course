class Person(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"


class VerbosePerson(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        return f"{super().greet()}, you are {self.age}"


p1 = Person('Nikita')
p2 = VerbosePerson('Marian', 35)

print(p1.greet())
print(p2.greet())
