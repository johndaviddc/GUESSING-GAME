import random

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess it in 7 tries or less?")

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Set the number of guesses to 0
guesses = 0

# Loop until the player guesses the correct number or runs out of guesses
while guesses < 7:
    guess = int(input("Guess a number between 1 and 100: "))

    # Increment the number of guesses
    guesses += 1

    # Check if the guess is correct
    if guess == number:
        print("Congratulations, you guessed the number in", guesses, "tries!")
        break
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")

# If the player runs out of guesses, reveal the answer
if guesses == 7:
    print("Sorry, you ran out of guesses. The number was", number)