Welcome = ("welcome to Kenzie's stupid whatever thing!")
exit = ("i cant belive you needed a computer to remind you of these.")

print(Welcome)

print("What is your name?")
a = (input(" : "))

print("What is your age?")
b = int(input(" : "))

print("Where country do you live in?")
c = (input(" : "))

print("What is your height? (In CM)")
d = int(input(" : "))

print(f"Name: {a}, Age: {b}, Country: {c}, Height: {d}")

print(exit)

user_input = input('do you actually like this garbage code? : ')

if user_input.lower() == 'yes':
    print('WOOOOOOOOOOOOOOOOOO thanks')
elif user_input.lower() == 'no':
    print('rip')
else:
    print('Type yes or no >:(')
