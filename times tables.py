table = int(input("please enter a times table: "))
while (table <20):
    for x in range(0,12):
        print (x, "x", table, "=", x*table)
else:
    print("your number was greater than 20")
    table = int(input("please enter a times table: "))
