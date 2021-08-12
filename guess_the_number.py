import random

# User will guess the Number
def user_guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess The number between 1 and {x} = "))
        if guess < random_number:
            print("Sorry, Try Again, Too Low")
        elif guess > random_number:
            print("Sorry, Try Again , Too High")
    print(f"Congratlation you Guessed the correct number....which is {guess}")

user_guess(10)


##############################################################################################

# Computer will guess the Number
def computer_guess(x):
    low = 1 
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess =random.randint(low,high)
        else:
            guess = low 
        feedback = input(f"Is {guess} too high (H), too low (L) or coorect (C) ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"The computer guessed the number,{guess} correctly! ") 

computer_guess(1000)