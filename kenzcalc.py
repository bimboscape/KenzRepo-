#Whoevers modifying this scipt, whoever you are. 
#I apologize for how spaghetti'd to shit it is <3 -kenz 
script_seperator = ("_______________")
print(script_seperator)
script_welcome = ("Welcome to Kenzie's Calculator Script")
print(script_welcome)
#spaghetti code to seperate all this shit 
#(ive barely been keeping track)
userinput_script = input('Which conversion script would you like to use? : ')
#Calc script
if userinput_script == 'math':
    num_welcome = ("welcome to Ken'z calculator!")
    num_exit = ("Enjoy your numbers!")
    sep = ('----------------------------------------------------------')
    print(sep)
    user_input = input('Welcome, Please enter either +, *, -, or / : ')
    if user_input == ('+'):
        #Addition
        print(sep)
        print(num_welcome)
        num1 = float(input('Please enter your first number : '))
        print(sep)
        num2 = float(input('Please enter your second number : '))
        sum = num1 + num2

        print(sep)
        print(f"{num1} + {num2} = {sum}")
        print(num_exit)
    elif user_input == '*':
        #Multiplication
        print(sep)
        print(num_welcome)
        num3 = float(input('Please enter your first number : '))
        print(sep)
        num4 = float(input('Please enter your second number : '))
        sum = num3 * num4

        print(sep)
        print(f'{num3} x {num4} = {sum}')
        print(num_exit)
    elif user_input == '-':
        #Subtraction
        print(sep)
        print(num_welcome)
        num5 = float(input('Please enter your first number : '))
        print(sep)
        num6 = float(input('Please enter your second number : '))
        sum = num5 - num6

        print(sep)
        print(f'{num5} - {num6} = {sum}')
        print(num_exit)
    elif user_input == '/':
        #Division
        print(sep)
        print(num_welcome)
        num7 = float(input('Please enter your first number : '))
        print(sep)
        num8 = float(input('Please enter your second number : '))
        sum = num7 / num8

        print(sep)
        print(f'{num7} / {num8} = {sum}')
        print(num_exit)
    else:
        #If the script can't detect what you input
        print(sep)
        print("You're options are : ")
        print("+ for addition.")
        print("* for multiplication")
        print("- for subtraction")
        print("/ for division")
#Temp converter script
elif userinput_script == 'temp':
    seperate = ('-------------------------------------------------------------------------')
    print(seperate)
    user_input = input('which temps are you converting? : ')
    print(seperate)
    #Welcome & Exiting print for _ to Kelvin Converters
    Kelvin_welcome = ("kenzie's Kelvin Convertor")
    Kelvin_exit = ('Enjoy your numbers in Kelvin!')

    #welcome & Exiting print for Kelvin to _ Converters

    Kelvin_welcome2 = ("Kenzie's kelvin to Celsius converter!")
    Kelvin_exit2 = ("Enjoy your numbers in Celsius!")
    etc_exit = ('Enjoy your numbers in Farhenheit!')
    etc_welcome = ('Welcome to Kenzies converter!')

    if user_input == 'c to f':   
        #Celsius to Fahrenheit
        num1 = float(input("please let me convert your celsius for you! I'm desperate : "))
        num2 = int(32)
        num3 = float(1.8)
        sum = num1 * num3 + num2

        print(f"{num1} in f is {sum}")
        print(seperate)
    elif user_input == 'Celsius to Fahrenheit':
        #Celsius to Fahrenheit to (Different syntax)
        print(seperate)
        num9 = float(input("Please let me convert your Celsius for you! I'm desperate : "))
        num10 = int(32)
        num11 = float(1.8)
        print(seperate)
        thanks = ('Thank you so much for feeding me the numbers!')
        sum = num9 * num11 + num10
        print(f"{num9}°c is {sum} in Fahrenheit!")
        print(seperate)
    elif user_input == 'f to c':
        #Fahrenheit to Celsius 
        print(seperate)
        print(etc_welcome)
        print(seperate)

        num5 = float(input('please enter a number in Fahrenheit : '))
        num6 = int(32)
        num7 = float(1.8)
        num8 = (num5 - num6)
        sum = (num8 / num7)

        print(seperate)
        print(etc_exit)
        print(f"{num5} in celsius is {sum}")
        print(seperate)
    elif user_input == 'Fahrenheit_to_Celsius':
        #Fahrenheit to Celsius (Different syntax)
        print(seperate)
        print(etc_welcome)
        print(seperate)

        num12 = float(input('please enter a number in Fahrenheit : '))
        num13 = int(32)
        num14 = float(1.8)
        num15 = (num12 - num13)
        sum = (num15 / num14)

        print(seperate)
        print(f"{num12} in celsius is {sum}")
        print(seperate)
    elif user_input == 'Celsius_to_Kelvin':
        #Celsius to Kelvin
        print(seperate)
        print(Kelvin_welcome)
        print(seperate)

        num20 = float(input("Please enter a number in Celsius : "))
        num21 = float(273.15)
        sum = num20 + num21

        print(seperate)
        print(f"{num20} in Kelvin is {sum}")
        print(Kelvin_exit)
        print(seperate)
    elif user_input == 'Fahrenheit_to_Kelvin':
        #Fahrenheit to Kelvin
        print(seperate)
        print(Kelvin_welcome)
        print(seperate)

        num24 = float(input("Please enter a number in Fahrenheit : "))
        num25 = float(32)
        #num26 = float(5)
        #num27 = float(9)
        num26 = float(0.55)
        num28 = float(273.15)
        sum = num24 - num25
        sum2 = sum * num26
        sum3 = sum + num28

        print(seperate)
        print(f"{num24} in Kelvin is {sum3}")
        print(Kelvin_exit)
        print(seperate)
    elif user_input == 'Kelvin_to_Celsius':
        #Kelvin to Celsius
        print(seperate)
        print(Kelvin_welcome2)
        print(seperate)

        #Wait why tf did i make the Kelvin conversions have their
        #own welcome and shit, well whatever I'm not bothering w it now.
        num30 = float(input("Please enter your number in Kelvin"))
        num31 = float(273.15)
        sum = num30 - num31

        print(seperate)
        print(f"{num30} in Celsius is {sum}")
        print(Kelvin_exit2)
        print(seperate)
    else:
        #If script cant detect what you input for the conversion scrip
        print('Options : ')
        print('1: c to f (Converts Celsius to Fahrenheit)')
        print('2: Celsius to Fahrenheit (Convertss Celsius to Fahrenheit')
        print('3: f to c (Converts Fahrenheit to Celsius)')
        print('4: Fahrenheit to Celsius (Converts Fahrenheit to Celsius)')
        print('5: Celsius_to_Kelvin (Converts Celsius to Kelvin)') 
        print("6: Fahrenheit_to_kelvin (Converts Fahrenheit_to_Kelvin) ")
        print(seperate)
elif userinput_script == 'Secret:3':
    print('8====================D')
    print("get cock'd! You've been cock'd")
elif userinput_script == "OwO":
    print('AHHHHHHHHHHHHHHHHHHHHHHH')
    print("OwO")
elif userinput_script == 'unit':
    unit_sep = ('----------------------------')
    print(unit_sep)
    user_input_unit = input("What Units of Measurement do you want to convert? : ")
    if user_input_unit == "cm to ft":
        #cm x 0.0328084 = ft
        welcome = ("welcome to kenz's cm to ft converter!")
        close = ("thank you for using kenz's cm to ft converter!")
        print(welcome)

        num1 = float(input("please input your first number in cm : "))
        num2 = float(0.0328084)

        sum = num1 * num2
        print(unit_sep)
        print(f"{num1} in ft is {sum}ft!")
        print(close)
    #km to ft converter
    elif user_input_unit == "km to ft":
        #ft = km ÷ 0.0003048
        unit_sep2 = ('----------------------------')
        import random
        welcome = ("kenz's km to ft convertor", 'thank you for using kenz km convertor!')
        exit = ('mmmm numbers uwu', 'enjoy your numbers!')

        random_item = random.choice(welcome)
        random_item2 = random.choice(exit)
        print(unit_sep2)
        print(random_item)

        num1 = float(input("Please enter your number in km :3 : "))
        num2 = float(0.0003048)
        sum = num1 / num2
        print(unit_sep2)

        print(f"{num1} in ft is {sum} ft")

        print(":3", random_item2)
    #if it cant figure out what unit of measurements you want it to convert
    elif user_input_unit == 'ft to km':
        #km = ft x 0.0003048
        unit_sep3 = ('----------------------------')
        uwuinput = float(input("Please enter your first number in feet : "))
        a = float(0.0003048)
        sum = uwuinput * a
        print(unit_sep3)
        print(f"{uwuinput} in km is {sum}")
        print("Enjoy your numbers :3")
    else:
        print("For unit, you can choose :")
        print("km to ft : to convert kilometers to feet.")
        print("cm to ft : to convert centimetres to feet.")
        print("ft to km : to convert feet to kilometers.")
else:
    #List of inputs for the user to choose from.
    #Showing various conversion.
    print(script_seperator)
    print('You can either Choose : ')
    print('temp, for the Temp Converter,')
    print('math, for the Calculator,')
    print('unit, for the Unit of Measurment converter,')
    print(script_seperator)
    #Secret Inputs = "Secret:3, OwO"
    print('Please reload the program and try again with proper syntax!')
    #Yes I literally did just make a bunch of smaller scripts and then cram them
    #together to make this script
    print('Thank you for using Kenz Calc :3')
