import random
from day7_words import word_list
from day7_art import logo, stages

print(logo)

word = random.choice(word_list)
print(word)

placeholder = ""
for pos in range(len(word)):
    placeholder += "_"
print(f"Word to guess: {placeholder}")

over = False
lives = 6
correct_guesses = []

while not over:
    print(f"********************{lives}/6 LIVES LEFT********************")
    guess = input("Choose a letter: ").lower()
    flag = False

    if guess in correct_guesses:
        print(f"You already guessed the letter '{guess}'")
        flag = True

    display = ""
    for ch in word:
        if guess == ch:
            display += f"{guess} "
            correct_guesses.append(ch)
            if not flag:
                print(f"You guessed correctly!")
        elif ch in correct_guesses:
            display += ch
        else:
            display += "_"

    print(display)
        
    if guess not in word:
        lives -= 1
        print(f"You guessed {guess} which is NOT in the word. You lose a life.")

        if lives == 0:
            over = True
            print(f"********************YOU LOSE********************")


    if "_" not in display:
        over = True
        print(f"********************YOU WIN********************")

    print(stages[lives])