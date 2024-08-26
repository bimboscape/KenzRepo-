#imports os and shutil module
import os, shutil
perm_warning = ("You may require root privliges to perform this action")
inputpath = input("Which directory would you like to go? : ")
sep = ("*************************************************************************")
#Yes, I'm aware of the spaghetti
try:
    os.chdir(inputpath)
    input_option = input("Would you like to delete, or add a file?")
    if input_option == "add":
        #Add file
        try:
            print(sep)
            def print1():
                file_name = input("What would you like to call the file? : ")
                user_input = input("Please enter something to save to a file : ")
                # Open a file in write mode (creates the file if it doesn't exist)
                with open(file_name, 'w') as file:
                # Write the user input to the file
                    file.write(user_input + '\n')
                print("The input has been saved to 'output.txt'.")
                print(sep)
            print1()
        except:
            #error if it has any issues (usually permission issues)
            print("It appears the script can't write the file here :<")
            print(perm_warning)
    elif input_option == "delete_file":
        #File deletion
        try:
            print(sep)
            def print2():
                user_input2 = input("Please enter the name of the file you wish to delete : ")
                os.remove(user_input2)
                print("The file is now deleted!")
            print2()
            print(sep)
        except:
            #error if it has any issues (usually permission issues)
            print("It appears the scripts can't delete the file here :<")
            print(perm_warning)
    elif input_option == "delete_empty_directory":
        #Directory deletion
        try:
            print(sep)
            def print3():
                userinput4 = input("Please enter the directory you'd like to delete : ")
                os.rmdir(userinput4)
            print3()
            print("The directory has been removed!")
        except:
            #error if it has any issues (usually permission issues)
            print("It appears the script can't remove the directory :<")
            print(perm_warning)
    elif input_option == "delete_tree":
        #tree deletion
        try:
            print(sep)
            def print4():
                user_input5 = input("Please enter the tree youd like to delete : ")
                shutil.rmtree(user_input5)
            print4()
            print("The tree was removed!")
        except:
            #error if it has any issues (usually permission issues)
            print("It appears the script can't remove the tree :<")
            print(perm_warning)
            print(sep)
    elif input_option == "make_dir":
        #Directory maker
        try:
            print(sep)
            def print5():
                user_input6 = input("Please enter what you want to call the dir : ")
                os.mkdir(user_input6)
            print5()
            print("The Dir was created!")
        except:
            print("It appears the script couldn't create the Dir :<")
            print(perm_warning)
            print(sep)
    elif input_option == "make_nested_dir":
        #Nested directory maker
        try:
            print(sep)
            def print6():
                user_input7 = input("Please enter what you want to call the dir : ")
                os.makedirs(user_input7)
            print6()
            print("The nested directory was created!")
        except:
            print("It appears the script couldn't create the Dir : ")
            print(perm_warning)
            print(sep)
    else:
        #options (if you input a command it doesnt recognize)
        print(sep)
        print("Oops!")
        print("You're options are : ")
        print("'add' Adds a file.")
        print("'delete_file' Deletes a file.")
        print("'delete_empty_directory' Deletes empty directory.")
        print("'delete_tree' Deletes full tree (run with caution.)")
        print("'make_dir' Creates directories.")
        print("'make_nested_dir' Creates nested directories.")
        print(sep)
except:
    #If the script cant find the directory you inputed
    print(sep)
    print("Oops! it seems the script has run into an error. :<")
    print("The dir you pointed to may not exist, or you may not have permissions.")
    print(sep)
