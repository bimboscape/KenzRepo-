#ft = km ÷ 0.0003048
import random
welcome = ("kenz's km to ft convertor", 'thank you for using kenz km convertor!')
exit = ('mmmm numbers uwu', 'enjoy your numbers!')

random_item = random.choice(welcome)
random_item2 = random.choice(exit)

print(random_item)

num1 = float(input("Please enter your number in km :3 : "))
num2 = float(0.0003048)
sum = num1 / num2

print(f"{num1} in ft is {sum} ft")

print(":3", random_item2)