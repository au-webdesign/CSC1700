# Author: dlash
# date: 9/14/2019

stuff = input("What is in your bottles???")
ct = int(input(f"How many {stuff} on the wall?"))
if ct < 0:
    print(f"Illegal count:{ct} ...", end=" ")
    print(f"Needs to be at least 1 {stuff} on the wall")
    quit()

keepGoing = 'y'
while ct > 0 and keepGoing.lower() == 'y':
    print( f"{ct} bottles of {stuff} on the wall", end=" ")
    print( f"{ct} bottles of {stuff}", end=" ")
    print( f"------ Take one down ... pass it around ...")
    keepGoing = input("You sure you want to keep going? (y or n)")
    ct = ct - 1

print (f"no more bottles of {stuff} on the wall")
