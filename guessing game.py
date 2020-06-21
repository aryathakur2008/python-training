import random
number = random.randint(1,20)
guess = float(input("i'm thinking of a number from 1 to 20, what is it?"))
while guess != number:
    if guess < number:
        print("your number is too low...")
    else:
        print("your number was too high")
    guess = float(input("please try again..."))
    print(guess)
print("congratulations! correct answer!")
