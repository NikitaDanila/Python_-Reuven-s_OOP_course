class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


p1 = Person('Nikita Danila', 'danila.nikitamihai@gmail.com', '0773822951')
p2 = Person('Mario Casas', 'mario.casas@gmail.com', '0771467213')
p3 = Person('Juan Enrique', 'juan.enrique@gmail.com', '0773764581')

all_contacts = [p1, p2, p3]


def print_contacts():

    for one_contact in all_contacts:
        print(
            f"Name: {one_contact.name}\nemail: {one_contact.email}\nphone: {one_contact.phone}\n\n")


print_contacts()

p2.name = 'Julio Jimenez'
p2.email = 'julio.jimenez@gmail.com'
p2.phone = '0771998341'

print_contacts()
