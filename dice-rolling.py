from random import randint

def roll():
    return randint(1,6)

loop = True
print("Rolling a dice...")
print(roll())

while loop == True:
    again = input("Do you want to roll a dice again?(y/n)")
    if again == "n":
        print("Stopping the program...")
        a = False
    elif again == "y" or again == "":
        print("Rolling a dice...")
        print(roll())
