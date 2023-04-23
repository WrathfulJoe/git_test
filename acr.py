

while True:
    phrase = "fight the wild"
    acr = phrase[0] # add first letter

    for i in range (1,len(phrase)): # iterate over string, skip [0]
        if phrase[i-1] == ' ': # if letter - 1 equal to empty space

            acr += phrase[i] # add letter next to space
    acr = acr.upper() # uppercase oupt

    print(acr)

    play_again = input("Do you want to try again? (y/n): ")
    if play_again.lower() != "y":
        break