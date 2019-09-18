# Suppose you want to output the cost per each
#   seat in a theature. Rules:
# YOu have 6 ROWS and Each Row has 5 seats
# Suppose the cheap seats cost 5.50
#     the expensive are 7.50   and they are the center seats

ROWS = 6
COLS = 5
CHEAP = 5.50
CENTER = 7.50
print("   ", end=" ")
for col in range(1,(COLS+1)):
    print(f"C{col} ", end=" ")
print("")
for row in range(1,(ROWS+1)):
    print(f"R{row} ", end=" ")
    for col in range(1, (COLS + 1)):
        if col == 1 or col == 5:
            print(f"{CHEAP}", end=" ")
        else:
            print(f"{CENTER}", end=" ")
        #print("R" + str(row) + "C" + str(col), end=" ")
    print("")
