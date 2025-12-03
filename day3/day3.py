height = int(input("Enter height (cm): "))
if height > 120:
    print("Greater than 120")
if height >= 120:
    print("Height is 120 or greater")
if height < 120:
    print("Height is less than")
if height <= 120:
    print("Height is 120 or less")
if height == 120:
    print("Height is 120")
if height != 120:
    print("Height isn't 120")


num = int(input("Enter a number to check: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

height = int(input("Enter height (cm): "))

if height > 120:
    age = int(input("Enter age: "))
    if age <= 12:
        print("Price of roller coaster ticket is $5")
    elif age < 18:
        print("Price of roller coaster ticket is $7")
    else:
        print("Price of roller coaster ticket is $12")
else:
    print("You cannot use a roller coaster!")

bmi = 84 / 1.65 ** 2

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi >= 25:
    print("Overweight")

height = int(input("Enter height (cm): "))
bill = 0

if height > 120:
    age = int(input("Enter age: "))
    if age <= 12:
        bill = 5
    elif age < 18:
        bill = 7
    else:
        bill = 12
    
    bonus = input("Do you want a photo? (y/n): ")
    if bonus == "y":
        bill += 3
    
    print(f"Your final bill is: {bill}")
else:
    print("You cannot use a roller coaster!")

size = input("What size do you want? S, M or L?: ")
pepperoni = input("Do you want pepperoni on your pizza? (y/n): ")
cheese = input("Do you want extra cheese on your pizza? (y/n): ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill +=20
elif size == "L":
    bill += 25
else:
    print("Invalid Option")

if pepperoni == "y":
    if size == "S":
        bill += 2
    if size == "M" or size == "L":
        bill += 3
else:
    print("Invalid Options")

if cheese == "y":
    bill += 1

print(f"Your final pizza bill is: {bill}")

e = 12
if not e == 12:
    print("e is not equal to 12") # THIS WONT

if not e > 12:
    print("e is less than 12") # THIS HAPPENS

height = int(input("Enter height (cm): "))
bill = 0

if height > 120:
    age = int(input("Enter age: "))
    if age <= 12:
        bill = 5
    elif age < 18:
        bill = 7
    else:
        bill = 12
    
    if age >= 45 and age <= 55:
        bill = 0
        print("Damn unc you ride for free due to unc sympathy (midlife crisis)!")

    bonus = input("Do you want a photo? (y/n): ")
    if bonus == "y":
        bill += 3
    
    print(f"Your final bill is: {bill}")
else:
    print("You cannot use a roller coaster!")

print("-------------------------------------\nWelcome to Treasure Island.\nYour mission is to find the treasure!\n")


a = input("Do you want to go left or right? (left/right): ")
if a == "left":
    b = input("Do you want to swim or wait? (swim/wait): ")
    if b == "wait":
        c = input("Which door red, yellow, or blue? (red/yellow/blue): ")
        if c == "red":
            print("Burned by fire.\nGAME OVER!!")
        elif c == "blue":
            print("Eaten by beasts.\nGAME OVER!!")
        elif c == "yellow":
            print("YOU WON!!")
        else:
            print("GAME OVER!!")
    else:
        print("Attacked by trout.\nGAME OVER!!")
else:
    print("You fell into a hole!\nGAME OVER!!")