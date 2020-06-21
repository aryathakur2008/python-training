print("YOU ARE STUCK IN A BULDING,WITH A BOMB NEXT TO YOU.")
print("YOU NEED TO CUT A WIRE TO DISARM THE BOMB")
print("YOU HAVE THREE CHOICES 'RED' 'BLUE' 'YELLOW' ")
print("which will you pick?")
playerchoice = input("write answer in small letters: ")
if playerchoice  == "red":
    print("YOU DISARMED THE BOMB!")
    print("YOU WIN! GAME OVER PLEASE RESTART")
elif playerchoice == "blue" :
    print("THE BOMB INSTANTLY BLOWS UP!")
    print("YOU DIE")
    print("GAME OVER,PLEASE RESTART")
elif playerchoice == "yellow" :
    print("THANOS SNAPPED YOU")
    print("YOU DISAPPEAR")
    print("GAME OVER,PLPEASE RESTART")
else:
    print("you ran out of time")
    print("game over, please restart")
