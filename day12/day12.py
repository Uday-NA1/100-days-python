# When trying to call a global variable inside a function - you need to use 'global [variable]'
# as all variables inside the function is by default treated as a local variable or a new variable

enemies = 1

def increase_enemies(enemy):
    return enemy + 1

enemies = increase_enemies(enemies)


# Be careful with variables with global scope, but don't stop using them - it's useful for global constants
# If you want to differenciate constats --> Use full uppercased and underscores

PI = 3.14159
GOOGLE_URL = "https://www.google.com"


def circle_area(radius):
    global PI
    return PI * (radius**2)

import random

print("\nI'm thinking of a number between 1 to 100.")
difficulty = input("Enter a difficulty: ('easy' / 'hard'):\n")

answer = random.randint(1,100)
game_over = False
lives = 0

if difficulty == 'easy':
    lives = 10
if difficulty == 'hard':
    lives = 5

print(f"You start with: {lives} lives!\n")

while not game_over:
    guess = int(input("Guess a number: "))

    if guess > answer:
        lives -= 1
        print(f"Too high!")
        if lives == 0:
            print("You ran out of lives and lost the game. Better luck next time!")
            game_over = True
        else:
            print(f"You have {lives} lives remaining.")
        
    elif guess < answer:
        lives -= 1
        print(f"Too low!")
        if lives == 0:
            print("You ran out of lives and lost the game. Better luck next time!")
            game_over = True
        else:
            print(f"You have {lives} lives remaining.")

    else:
        print(f"You guessed correctly and won with {lives} lives remaining!")
        game_over = True