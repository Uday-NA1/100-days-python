import random

print(random.randint(a=1, b=2)) # Random integer from a to b

print(random.random()) # Semi open, always has 0 but not always 1. A random number from 0 to 1

print(random.uniform(1,10)) # Random float from 1 and 10

num = random.randint(a=0, b=1)
if num == 0:
    print("Tails")
else:
    print("Heads")

fruits = ["Cherry", "Apple", "Pear"]

fruits[0] # -2 is Apple (from back its -1, -2, -3)

fruits[0] = "Cherishing Cherry" # Edit list

fruits.append("Mango") # Add to the end of the list as

fruits.extend(['Mango', 'Watermelon']) # Extend with an additional list

fruits.pop(0) # Prints "Cherry" and deletes it from the list

print(fruits.pop(0)) # Prints the position 0 and removes it from the list


friends = ['Alice', 'Bob', 'Charlie', 'David', 'Emanuel']


print(f"{random.choice(friends)} has to pay!") # Option1. Easy, docs


ran = random.randint(0, len(friends)-1) # Option2. Randint
print(friends[ran])

fruits = ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']
dirty_dozen = [fruits, vegetables] # Nested list - here [0][0] refers to first list first item. [1][1] is second list second item

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ascii = [rock, paper, scissors]

user = int(input("Type 0 for rock, 1 for paper, 2 for scissors:\n"))
computer = random.randint(0,2)

if user >= 0 and user <= 2:
    print("You chose:")
    print(ascii[user])

print("Computer chose:")
print(ascii[computer])

if user >= 3 or user < 0:
    print("You typed an invalid number. You lose!")
elif user == 0 and computer == 2:
    print("You win!")
elif computer == 0 and user == 2:
    print("You lose!")
elif user > computer:
    print("You win!")
elif computer > user:
    print("You lose!")
elif computer == user:
    print("It's a draw!")