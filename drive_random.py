# author: dlash
# Date: 9/18
# Demonstration of Random

import random
die1 = random.randint(1,6)
print(f"die1:{die1}")
die2 = random.randint(1,6)
print(f"die2:{die2}")
roll = die1 + die2
print(f"You rolled:{roll}")

print("We are done")
