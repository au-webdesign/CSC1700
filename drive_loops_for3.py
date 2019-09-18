# author: dlash
# Date: 9/18
# Ask the user for a number...
#  Keep rolling 2 die ...
#  if roll a 2 or 7 or 11 loose
#   if rool their number they win

import random
guess = int(input("What is your roll guess for 2 die->"))

keep_going = True
while keep_going:
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    both = d1 + d2
    print(f"Your rolled a {both}", end=" ")
    if both == guess:
        print(".... you are a winner ... !!!!!")
        keep_going = False
    elif both == 2 or both == 7 or both == 11:
        print(".... you are a LOSER!!!! ... !!!!!")
        keep_going = False
