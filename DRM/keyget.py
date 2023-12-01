"""This would be the backend for generating new keys upon the buying of a product. The resulting key would be put in the database and the newly bought copy."""
import random, string, keys
key = None
while key in keys.keys:
    letters = string.ascii_lowercase
    key = ''.join(random.choice(letters) for letter in range(100))
nowkeys = keys.keys
nowkeys.append(key)
with open("keys.py", "w") as f: f.write("keys = " + str(nowkeys))