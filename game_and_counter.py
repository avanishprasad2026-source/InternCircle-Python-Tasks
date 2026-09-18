import random

def number_guessing_game():
    print("--- Number Guessing Game ---")
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def word_counter():
    print("\n--- File Word Counter ---")
    filename = input("Enter the filename to read (e.g., sample.txt): ")
    
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            char_count = len(text)
            print(f"File '{filename}' contains {word_count} words and {char_count} characters.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the file path.")

if __name__ == "__main__":
    number_guessing_game()
    print("\n")
    word_counter()
