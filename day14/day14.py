import random
from day14_art import *
from day14_data import *
    

print(logo)

score = 0
over = False

a = random.choice(data)

while not over:
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")

    print(f"\n{vs_art}\n")

    b = random.choice(data)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

    winner_str = "".lower()
    winner_lst = []

    a_followers = a['follower_count']
    b_followers = b['follower_count']

    if a_followers > b_followers:
        winner_str = 'a'
        winner_list = a

    elif b_followers > a_followers:
        winner_str = 'b'
        winner_list = b

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    if choice == winner_str:
        score += 1
        print(f"You're right! Current score: {score}")
        a = winner_list

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        over = True
    