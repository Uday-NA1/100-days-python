fruits = ['Apple', 'Peach', 'Pear']

for i in fruits:
    print(i)
    print(i + " pie")

scores = [150, 142, 185, 120, 170, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]
print(sum(scores)) # Totalling of a list

sum = 0
for score in scores: # Manual totalling
    sum += score

print(max(scores)) # Highest
print(min(scores)) # Lowest

low = 0
high = 0
for i in scores:
    if low == 0:
        low = i
    if high == 0:
        high = i
    if i < low:
        low = i
    if i > high:
        high = i

print(low, high)

for n in range(1,3): # Prints 1 and 2 (not 3)
    print(n)

for n in range(1, 11, 3):
    print(n)

sum = 0
for i in range(1,101):
    sum += i

print(sum)

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)

import random

print("Python Password Generator")
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '#', '$','%','&','(',')','*','+']

n_letters = int(input("How many letters would you like in your password?\n"))
n_numbers = int(input("How many numbers would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like in your password?\n"))

password = []
for i in range(0,n_letters):
    ch = random.choice(letters)
    password.append(ch)

for i in range(0,n_numbers):
    ch = random.choice(numbers)
    password.append(ch)

for i in range(0,n_symbols):
    ch = random.choice(symbols)
    password.append(ch)

random.shuffle(password)
pwd = ""
for i in password:
    pwd += i

print(f"Your password is: {pwd}")