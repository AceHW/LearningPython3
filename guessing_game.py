import random
number_of_guesses = 4
user_won = False

print("Welcome to the guessing game!")


# Computer guesses a random number between 1 and 10
correct_answer = random.randint(1, 10)

while number_of_guesses > 0:
# User guesses the number
    user_guess = input("Guess my number: ")
    user_guess = int(user_guess)
    if user_guess == correct_answer:
        print("Good guess")
        print("You're correct")
        user_won = True
        break

    # Computer tells user whether guess was too high or too low
    elif user_guess > correct_answer:
        print("Sorry, guessed too high")
    elif user_guess < correct_answer:
        print("Sorry, guessed too low")


    # User has 3 guesses before losing the game
    number_of_guesses -= 1


if user_won == True:
    print("You won!")
else:
    print("You lost")
