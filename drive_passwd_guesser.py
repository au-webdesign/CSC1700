# Author: dlash
# date: 9/14/2019
PASS = "bananas"
print("Welcome to the super secret password cracker ...")
keepGoing = True
count = 1
while keepGoing:
    guess = input("Guess the password....")
    if guess == PASS:
        print(f"CORRECT! the pass is {guess}")
        keepGoing = False
    else:
        print(f"----Guess:{count} ... The passwd is NOT {guess}")
        count = count + 1
print(f"---- thanks for playing ... it took you {count} guesses") 
