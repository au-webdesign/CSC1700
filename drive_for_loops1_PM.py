# author: dlash
# Date: 9/18
# Demonstration of the for
n = int(input("How many should i Run?"))
for i in range(5):     # from 0 to 4
    print(f"i:{i}")
print("We are done!")
print("------------------------------------")
for i2 in range(1,5):     # from 1 to 4
    print(f"i2:{i2}")
print("We are done!")
print("------------------------------------")
for jacksparrow in range(1,10,2):    # from 1 to 9 but add 2 to i each iteration
    print(f"i3:{jacksparrow}")
print("We are done!")
print("------------------------------------")
for jacksparrow in range(10,0,-1):    #Start at 10 go until 1 and subtract 1
    print(f"{jacksparrow} bottle of beer on the wall")
    print( str(jacksparrow) + "Bottles of beer on the wall")
print("No more bottle of beer on the wall!")

print("------------------------------------")
sum = 0
for i in range(6):
    sum += i
print(f"sum:{sum}")

