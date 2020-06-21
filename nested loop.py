for x in range(0,5):
    print("loop",x+1)
    for y in range(0,3):
        if y == 1:
            print("I am in under if ",y)
            break
        print("I am in inner for loop",y)
