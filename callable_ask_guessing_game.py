import random

#inputInt validates that user input is an int(whole number)
def inputInt(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer(whole number)! Try again.")
       continue
    else:
       return userInput 
       break 

def ask_guessing_game():
    
    number_of_guesses = 4
    user_won = False
    minrand = 1
    maxrand = 10

    print("Welcome to the (ask) guessing game!")
    
    print("This version asks what numbers you want the random number to be between and how many guesses you want to have.")
    
    minrand = inputInt("What number do you want the random pick to start at? Default and recommended value is 1 : ")
    
    maxrand = inputInt("What number do you want the random pick to max out at? Default value is 10 : ")
    
    number_of_guesses = inputInt("How many guesses do you want? : ")
    
    # Computer guesses a random number between 1 and 10
    correct_answer = random.randint(minrand, maxrand)
    
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
        

ask_guessing_game()
