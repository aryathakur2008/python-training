import random
exitchoice = "nothing"
while exitchoice != "EXIT":
print("YOU ARE STUCK IN A PYRAMID,WITH A PUZZLE IN FRONT OF YOU.")
print("YOU NEED TO SOLVE IT TO GO TO THE TREASURE")
print("YOU HAVE TO GO THROUGH A DOOR ")
print("which will you pick?")
print("write answer in small letters")
playerchoice = input("DOOR 'ONE 'TWO' 'THREE 'FOUR?: ")
if playerchoice  == "one":
    print("YOU FIND A ROOM OF TREASURE!")
    print("YOU WIN! GAME OVER PLEASE RESTART")
elif playerchoice == "two" :
    print("A MUMMY COMES OUT OF A SARCOPHIGUS AND EATS YOU!")
    print("YOU DIE")
    print("GAME OVER,PLEASE RESTART")
elif playerchoice == "three" :
    print("YOU ENTER A ROOM AND FIND A SLEEPING DRAGON!")
    print("YOU CAN EITHER: ")
    print("1)TRY AND STEEL IT'S TRESURE")
    print("2)TRY TO SNEEK AROUND THE DRAGON AND EXIT")
    dragonchoice =input("type 1 or 2...")
    if dragonchoice == "1":
        print("THE DRAGON WAKES UP AND EATS YOU")
        print("YOU DIE, YOU LOOSE, PLEASE RESTART")
    elif dragonchoice=="2":
        print("YOU SNEAK AROUND THE DRAGON AND ESCAPE THE PYRAMID, BLINKING IN THE SUNSHINE")
        print("YOU WIN!PLEASE RESTART")
elif playerchoice == "four":
    print("you enter a room with a sphinx.")
    print("it asks you to guess what number it is thinking of, between 1 to 10.")
    number = int(input("what number do you choose?"))
    if number == random.randint(1,10):
        print("the sphinx hisses in disapointment.you guessed corectly.")
        print("she must let you go.")
        print ("you win!")
    else:
        print("the  sphinx tells you that you guessed incorrect.")
        print ("you are her prisoner forever")
        print("game over, you loose,please restart.")
else:
    print("you didn't pick door '1 '2 '3 ' 4.")
    exitchoice = input("press return to play again, or type EXIT to leave.")

