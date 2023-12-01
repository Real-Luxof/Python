"""The product that requires a DRM. Since we don't have a key pre-written in this "newly bought copy", we ask for one instead."""
import keys
key = input("Input a key, or you're a pirate!\n>")
if key not in keys.keys: print("Argh! You're a pirate, matey!")
else: print("Thank you for supporting the official release.")