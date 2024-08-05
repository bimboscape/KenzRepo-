#c * 1.8 + 32 = f
import random
#imports the random module

num1 = float(input("please let me convert your celcius for you! I'm desperate:"))
num2 = int(32)
num3 = float(1.8)
thanks = ('thank you so much for feeding me the numbers!', 'MMMM numbers :3')

sum = num1 * num3 + num2

print(f"{num1}°c is {sum} in fehrenheit!")

random_item = random.choice(thanks)
print("uwu", random_item)
