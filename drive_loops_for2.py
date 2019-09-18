# author: dlash
# Date: 9/18
# Demonstration of the for loop
ROWS = 9
COLS = 5
TICKETS = 5.50
CENTER = 7.00   #
for i in range(1,(ROWS+1)):
    print(f"R{i}: ", end=" ")
    for j in range(1,(COLS+1)):
        if j == 1 or j == 5:
            print(f"{TICKETS} ", end=" ")
        else:
            print(f"{CENTER} ", end=" ")
    print("")
