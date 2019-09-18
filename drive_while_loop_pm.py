keep_looping = True
while keep_looping:
    n = int(input("How many Times to loop? (from 1 to 5"))
    if n >= 1 and n <= 5:
        keep_looping = False
    else:
        print("Hey I said from 1 to 5")
ct = 0
while ct < n:
    ct = ct + 1
    print(f"Lopping ct:{ct}")
print("--- we are done")
