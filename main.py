from read import *
from operations import *


"""Main file is to run the whole programs"""
loop = True
print("\n")
print(" \t **----------Manoj Gautam: 22067877----------**")
print("\n")
print(" \t **----------WELCOME to OLIZ FAMILY----------**")
print("\t ***-----WELCOME TO LAPTOPS SECTION----------***")
print("\n")
print("------ FOLLOW THE INSTRUCTION AND PUT INTEGER VALUE IN NEEDED FIELDS-----")
print("\n")
while loop == True:
    print("Enter 1 to sale laptop and reduce quatity of the existing stock")
    print("Enter 2 to buy laptop and add to the existing stock")
    print("Enter 3 to exit the portal")

    #only allow integer value only
    try:
        user_input_num=int(input("Enter the required number : "))
        for_portal(user_input_num)

        print(" Come again and Thank you for Choosing OLIZ STORE")#prints in the end of the program
        break
    except:
        print("Please! enter  value from 1-3")
    
