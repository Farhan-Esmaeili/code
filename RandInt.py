#input
range_start = int (input("Enter a number as the range start : "))
range_end = int (input("Enter a number as the range end : "))
#intializing and output
import random
rand = random.randint(range_start, range_end)
i=0
while i == 0 :
    num = int(input("Enter your number"))
    if num > rand:
        print("Go lower")
    elif num < rand :
        print("Go upper")
    elif num == rand :
        print("Thats correct! Well done.")
        ans=input("Do you wish to play again? yes/no : ")
        if ans == "no" :
            i+=1
        elif ans == "yes" :
            print("Here you go!")
            range_start = int (input("Enter a number as the range start : "))
            range_end = int (input("Enter a number as the range end : "))
            rand = random.randint(range_start, range_end)

# Farhan Esmaeili | newbie programmer


                        
