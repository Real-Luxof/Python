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
    def __init__(self, family_members):
        self.family_members = family_members


print("Hello, this script was created to determine whether any number of people could sustain a certain birth", end="")
print("rate with no inbreeding.")

number_of_people = ""
birth_rate = ""

while not is_int(number_of_people):
    number_of_people = input("Number of people >")

while not is_int(birth_rate):
    birth_rate = input("Birth rate >")


