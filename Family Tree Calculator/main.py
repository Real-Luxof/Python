import random

list_of_people = {}
names = []
genders = ["M", "F"] # To reduce complexity, there will only be males and females.

for i in range(100000):
    names.append(f"John.{i}")


def random_name():
    global names
    name = random.choice(names)
    names.remove(name)
    return name


def is_int(string: str):
    """Determines whether a string contains only integers or not.

    Args:
        string (str): The string.

    Returns (Bool): True if the string contains only integers, False otherwise.

    """
    try:
        int(string)
        return True
    except ValueError:
        return False


class Person:
    def __init__(self, name, gender, partner=None, family_members=None):
        global list_of_people
        self.name = name
        self.gender = gender
        self.partner = partner
        self.family_members = family_members
    
    def is_family(self, person_name):
        return person_name in self.family_members

    def not_same_gender(self, person):
        return self.gender != person.gender
    
    def get_partner(self, person_name):
        global list_of_people
        person = list_of_people[person_name]
        if not self.partner and not person.partner and not self.is_family(person.name) and self.not_same_gender(person):
            self.family_members += person.family_members
            self.partner = person.name
            person.family_members = self.family_members
            person.partner = self.name
    
    def birth(self):
        global list_of_people
        if self.partner and self.gender == "F":
            child_name = random_name()
            
            list_of_people[child_name] = Person(
                child_name,
                random.choice(genders),
                None,
                self.family_members
            )
            
            self.family_members += child_name


print("Hello, this script was created to determine whether X number of ", end="")
print("people could sustain Y birth rate with no inbreeding.\n")

print("Note: for reasons such as reducing complexity and getting speed, ",end="")
print("there can only be 100,000 people, everyone must be heterosexual, etc.")
print("You may doubt the results of this script as you please, as in real ", end="")
print("life there would be much more going on to combat a birth rate crisis ", end="")
print("in a limited population. Also keep in mind people may choose their ", end="")
print("own genders etc. etc. blah blah blah.\n")

number_of_people = ""
birth_rate = ""

while not is_int(number_of_people):
    number_of_people = input("Number of people >")

while not is_int(birth_rate):
    birth_rate = input("Birth rate >")

for spawn_person in range(number_of_people):
    person = Person(
        random_name(),
        random.choice(genders),
        None,
        []
    )
    list_of_people[person.name] = person

inbreeding = False

while not inbreeding:
    birth_count_this_generation = 0
    
    for birth in range(birth_rate):
        for person in list(list_of_people.values()):
            
