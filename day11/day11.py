import random

start = input("Do you want to play blackjack? (y/n): \n")
if start == 'y':
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    def calculate_score(cards):
        score = sum(cards)
        
        while score > 21 and 11 in cards:
            cards[cards.index(11)] = 1
            score = sum(cards)
        return score

    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"You have {user_cards} (score: {user_score})")
    print(f"The dealer's first card is: {computer_cards[0]}")

    deal_again = True

    while deal_again:
        hit = input("Do you want another card? ('y'/'n'):\n").lower()
        if hit == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"You have {user_cards} (score: {user_score})")

            if user_score > 21:
                print("BUST! You lose!")
                deal_again = False
        
        elif hit == "n":
            deal_again = False

    if user_score <= 21:
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = sum(computer_cards)

        print(f"You has {user_cards} (score: {user_score})")
        print(f"Dealer has {computer_cards} (score: {computer_score})")

        if computer_score > 21:
            print("Dealer busts! You win!")
        if computer_score > user_score:
            print("You lose!")
        elif user_score > computer_score:
            print("You win!")
        else:
            print("It's a draw!")

else:
    pass