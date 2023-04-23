import random

n=random.randrange(1,100)

guess = int(input("Guess a number between 1 and 100: "))
while n!= guess:
    if guess < n:
        print ("Too low")
        guess = int (input("Enter number again:"))
    elif guess > n:
        print ("Too High")
        guess = int (input("Enter number again:"))
    else:
        break
print ("You guessed it right")