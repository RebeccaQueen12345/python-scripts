
secretword = "babysitting"
guess = " "
guesscount = 0
guesslimit = 10
outofguesses = False
while guess != secretword and not (outofguesses):
    if guesscount < guesslimit:
        guess = input("enter guess: ")
        guesscount +=1
else:
            outofguesses = true
 
if outofguesses:
    print("Out of guesses, you lose!")
else:
    print("You Won!")
