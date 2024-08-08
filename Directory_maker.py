import os

welcome = ("welcome to Kenzie's directory maker!")
end = ("enjoy your new directory!")

print(welcome)

user_in = input('where shall we be making your new directory?')

os.chdir(user_in)

exists = os.path.exists(user_in)
print(f"Directory exists : {exists}")

os.mkdir(input('what would you like your new directory to be called? : '))

print(end)
