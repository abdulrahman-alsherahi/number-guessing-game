

# Gussing Gama!


import random

print("🎮 Welcome to the Number Guessing Game!")

while True:

    secret_number = random.randint(1, 10)
    max_tries = 5
    attempts = 0

    print("\nI have chosen a number between 1 and 10.")
    print("You have 5 tries to guess it!")

    while attempts < max_tries:

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"✅ Correct! You guessed the number in {attempts} tries.")
            break

        elif guess > secret_number:
            print("⬆️ Too high! Try again.")

        else:
            print("⬇️ Too low! Try again.")

    else:
        print(f"❌ Game Over! The number was {secret_number}")

    play_again = input("\nDo you want to play again? (y/n): ").lower()

    if play_again != "y":
        print("Thanks for playing! 👋")
        break
