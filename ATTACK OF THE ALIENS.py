aliens = 2
password = "ALIENS"
print("quickly! aliens are invading the planet.")
print("you need to activate the global defence platforms.")
print("hope you know the password, for earths sake...")
print()
print("-----------------------------------------------------------")
print("          WELCOME TO THE GLOBAL DEFFENCE NETWORK           ")
print("-----------------------------------------------------------")
print()
guess = input("please enter the password: ").upper()
while guess != password:
    print()
    print("INCORRECT PASSWORD.")
    print()
    aliens = aliens ** 2
    print("there are", aliens, "aliens now on earth. try again!")
    if aliens > 7400000000:
            break
    print()
    print("password hint: the things that are attacking you")
    print()
    guess = input("Quick! please enter the password: ").upper()
    if aliens > 7400000000d:
        print("nooooooo! the aliens have outnumbered us. All is lost.")
    else:
        print("hooray! we won the fight and the world is saved!")
    
