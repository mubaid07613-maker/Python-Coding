import random as rnd
choice = 0
guess = 0
guess_minimum = 0
guess_maximum = 100
guesses = []
win = False
print("This is a simple Number Guessing Game!")
while True:
    print("1--> PLAY\n2--> Exit")
    choice = int (input("Please enter your choice: "))
    match choice:
        case 1:
            while True:
                user_input = int( input("Enter a number between 1 and 100 : "))
                if user_input <= 100 and user_input >= 0:
                    turns = int (input ("How many turns will you allow me to guess your number? "))
                    while True:
                        guess= rnd.randint(0,100)
                        if guess in guesses[1:]:
                            continue
                        else:
                            guesses.append(guess)
                            break
                    i = 1
                    print("My Guess number", i," is :",guess)
                    for i in range(turns-1):
                        if guess == user_input:
                            print("Aha! i guessed your number I win!")
                            win = True
                        else:
                            while True:
                                print("So is your number above or below my guess? (A/B)")
                                answer = input(" ")

                                if answer.upper() == 'A' or answer.upper() == 'B':
                                    if answer.upper() == 'A':
                                        guess_minimum = guess+1
                                        guess = rnd.randint(guess_minimum,guess_maximum)
                                        break
                                    else:
                                        guess_maximum = guess-1
                                        guess = rnd.randint(guess_minimum,guess_maximum)
                                        break
                                else:
                                    print("Heyy thats not the right choice! Try again :)")
                                    continue
                            print("My Guess number", i+2," is :",guess)               
                else:
                    print("Come on! I need a number between 1 and 100!")
                    continue
                break
        case 2:
            print("See you next time! :3")
            break
        case _:
            print("You entered the wrong choice, try again")
    if choice == 1:
        if win == True:
            print("Well I won this time, but maybe the next time I won't be so lucky! Wanna play again?")
            continue
        else:
            print("Darn I lost? Think you'll let me have another shot?")
            continue




