import os

welcome = ("welcome to Kenzie's directory maker!")
end = ("enjoy your new directory!")

print(welcome)

os.chdir(input('where shall we be making your new directory?'))

os.mkdir(input('what would you like your new directory to be called? : '))

print(end)