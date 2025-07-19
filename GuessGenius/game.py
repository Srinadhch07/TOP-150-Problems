import random

def number_guessing_game():
    replay = True
    while replay:
        print("------------------------------------")
        print("Welcome to the Number Guessing Game!")
        print("------------------------------------")
        
        # Get the number of digits from the user
        while True:
            num_digits = input("Enter the number of digits of the number you want to guess: ")
            if num_digits.isdigit() and int(num_digits) > 0:
                num_digits = int(num_digits)
                break
            else:
                print("Please enter a valid number of digits (Number must be greater than 0).")
        
        # Get the maximum number of guesses from the user
        while True:
            max_guesses = input("In how many guesses you can guess the total number: ")
            if max_guesses.isdigit() and int(max_guesses) >= num_digits:
                max_guesses = int(max_guesses)
                break
            elif max_guesses.isdigit() and int(max_guesses) < num_digits:
                print("The maximum number of guesses must be greater than or equal to the number of digits!")
            else:
                print("Please enter a valid positive number for maximum guesses.")
        
        # Generate the number to guess
        number_to_guess = ''.join(random.choices('123456789', k=num_digits))
        print(f"\nI have selected a number with {num_digits} digits. Try to guess the secret number!")
        
        attempts = 0
        guessed_number = ['_'] * num_digits  # List to track the correct digits guessed so far
        
        # Game loop for guesses
        while ''.join(guessed_number) != number_to_guess and attempts < max_guesses:
            print(f"{attempts + 1} attempt")
            guess = input(f"Current guess: {''.join(guessed_number)}\nEnter your guess (one digit only): ")
            
            # Validate the guess
            if len(guess) != 1 or not guess.isdigit():
                print("Please enter a single digit between 1 and 9.")
                continue

            attempts += 1
            guess = str(guess)
            revealed = False  # Flag to indicate if a digit has been revealed
            
            # Check if the guessed digit matches and reveal it if correct
            for i in range(num_digits):
                if number_to_guess[i] == guess and guessed_number[i] == '_':
                    guessed_number[i] = guess
                    revealed = True
                    break  # Only reveal the first correct digit for this guess
                
            # End the game if the number is fully guessed
            if ''.join(guessed_number) == number_to_guess:
                break
        
        # Output the result of the game
        if ''.join(guessed_number) == number_to_guess:
            print("--------------------------------------------------------------")
            print(f"\nYou are Genius! You've guessed the number {number_to_guess} in {attempts} guesses.")
            print("--------------------------------------------------------------")
        else:
            print("--------------------------------------------------------------")
            print(f"Your guesses are completed. The correct number was {number_to_guess}.")
            print("--------------------------------------------------------------")
        
        # Ask the user if they want to play again
        replay = play_again()

def play_again():
    play_again = input("\nDo you want to play again? \n 1. YES\n 2. NO \n")
    while True:
        if play_again == '1':
            return True
        elif play_again == '2':
            print("Thanks for playing! Goodbye!")
            return False
        else:
            play_again = input("Invalid input. Please enter a valid option.\nDo you want to play again? \n 1. YES\n 2. NO \n")

# Start the game
number_guessing_game()