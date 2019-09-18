# author: dlash
# Date: 9/18
# Demonstration of the for loop

# for loop is counting loop
last = int(input("how many loops?"))
sum = 0
for i in range(last):
    print(f"i:{i}")
    sum += i
print(f"The Value of Sum:{sum}")
print("--------------------------------------")
for i2 in range(1,10,2):
    print(f"i2:{i2}")

print("--------------------------------------")
for i3 in range(10,0,-1):
    print(f"{i3} bottles of stuff on the wall")
print("No more bottles on the wall")

print("--------------------------------------")
for i4 in range(5):
    print(f"{i4} bottles of stuff on the wall")
ct = 0
while ct < 5:
    print(f"{ct} bottles of stuff on the wall")
    ct = ct + 1
print("-----------------")
for idx in [1,9,100,4]:
    print(f"IND:{idx}")

for item in ["Box", "Bear", "Banana",1092]:
    print(f"Item:{item}")
