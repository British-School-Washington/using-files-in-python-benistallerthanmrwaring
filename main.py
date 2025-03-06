import random
def generate_number():
    return random.randint(1, 100)
def give_hint(target_number, guess):
    if guess < target_number:
        return "Too low! Try a higher number."
    elif guess > target_number:
        return "Too high! Try a lower number."
    else:
        return "Correct! You've guessed the number."
def start_game()
    target_number = generate_number()  # Random number between 1 and 100
    attempts = 0  # To count the number of attempts
    guessed_numbers = []  # List to store guesses
    print("Welcome to the Guess the Number Game!")
    print("I have picked a number between 1 and 100. Try to guess it!")
    while True
        guess = input("Enter your guess: ")
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Please enter a valid number.")
            continue
        if guess in guessed_numbers:
            print("You've already guessed that number! Try a different one.")
            continue
        else:
            guessed_numbers.append(guess)
        attempts += 1  # Increment the attempt counter
        result = give_hint(target_number, guess)
        print(result)
        if guess == target_number:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break
        if attempts == 5:
            continue_game  input ("You've had 5 attempts. Do you want to keep trying? (yes/no): ").lower()
            if continue_game != 'yes':
                print(f"The number was {target_number}. Better luck next time!")
                break
if __name__ == "__main__":
    start_game() 
