import random

def generate_secret_number():
    digits = list(range(1, 10))
    random.shuffle(digits)
    return "".join(map(str, digits[:4]))

def get_guess():
    while True:
        guess = input("Enter your 4-digit guess (digits 1-9, no duplicates): ")
        if len(guess) != 4:
            print("Invalid guess: Must be exactly 4 digits long.")
        elif not guess.isdigit():
            print("Invalid guess: Must contain only digits.")
        elif not all(c in '123456789' for c in guess):
            print("Invalid guess: Digits must be from 1 to 9.")
        elif len(set(guess)) != 4:
            print("Invalid guess: Digits must be unique.")
        else:
            return guess

def calculate_score(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if secret[i] == guess[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def play_game():
    secret_number = generate_secret_number()
    print("I have generated a 4-digit number. Try to guess it!")

    while True:
        guess = get_guess()
        if guess == secret_number:
            print(f"Congratulations! You guessed the number: {secret_number}")
            break
        else:
            bulls, cows = calculate_score(secret_number, guess)
            print(f"Score: {bulls} Bulls, {cows} Cows")

if __name__ == "__main__":
    play_game()