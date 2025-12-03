colors_of_fruit = {
    "apple" : "red",
    "pear" : "green",
    "banana" : "yellow",
    3 : "1 + 2"
}

colors_of_fruit["apple"] # Fetch from dictionary - Instead of index use the 'key'

colors_of_fruit["Watermelon"] =  "Green / Red" # Appending to dictionary

colors_of_fruit["pear"] = "pink" # Edit a dictionary

colors_of_fruit = {} # Wipe a dictionary

print(colors_of_fruit)

for item in colors_of_fruit: # 'item' refers only to the key
    print(item) # Prints the key only
    print(colors_of_fruit[item]) # Prints the value

nested_list = ['A', 'B', ['C', 'D']]

print(nested_list[2][1]) # Print 'D'

travel_log = {
    'France' : {
        'times_visited' : 8,
        'places_visited' : ['Paris', 'Lille', 'Dijon'],
    },

    'Germany' : {
        'times_visited' : 5,
        'places_visited' : ['Stuttgart', 'Berlin'],
    },
}

print(travel_log['Germany']['places_visited'][0])  # Print Stuttgart



def find_highest_bid(dict): # Can also use max(bids)
    highest = 0
    winner = ""
    for key in dict:
        current = dict[key]
        if highest == 0:
            highest = current
            winner = key
        if current > highest:
            highest = current
            winner = key
    print(f"The winner is: {winner}, with a bid of ${highest}")

bids = {}
over = False

while not over:
    name = input("What is your name?\n")
    amount = int(input("How much would you like to bid?\n"))
    bids[name] = amount
    check = input("Are there any other bidders? 'y' or 'n':\n").lower()

    if check == "n":
        over = True
        find_highest_bid(bids)
    elif check == "y":
        print("\n" * 20) # ALTERNATIVE: import os, system("cls")