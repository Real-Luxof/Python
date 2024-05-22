print("I asked Bing Chat to give me some fun coding challenges.")
print("For this one, it told me to make a program that for numbers from 1-100:")
print("- Says Fizz for multiples of 3")
print("- Says Buzz for multiples of 5")
print("- Says FizzBuzz for multiples of both.")
input("Click enter to start. >")

text = ""
for num in range(100):
    if num % 3 == 0: text += "Fizz"
    if num % 5 == 0: text += "Buzz"
    if text:
    print(text)
    text = ""
