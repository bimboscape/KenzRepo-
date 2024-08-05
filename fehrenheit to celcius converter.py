#(5-32) / 1.8

import random

welcome = ("thank you for choosing kenz converter!", 'welcome to kenz convertor :3')
exit = ("enjoy your numbers :3", 'thank you for using kenz convertor!')

random_item = random.choice(welcome)
random_item2 = random.choice(exit)

print("uwu", random_item)

num1 = float(input('please enter a number in fehrenheit:'))
num2 = int(32)
num3 = float(1.8)
num4 = (num1 - num2)

sum = (num4 / num3)

print(f"{num1} in celsius is {sum}")
print('uwu', random_item2)