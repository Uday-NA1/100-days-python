# Subscripting
print("Hello"[-1]) # -1  is the last character, 0 is the first character

# String - Concatenation
print ("123" + "456") # 123456

num = 123
 
print(123 + 456) # 579

print(123_456) # same as 123456


print(type(3.14)) # Any decimal numbers


flag1 = True
flag2 = False

print(type("123"))
print(type(123))
print(type(1.23))
flag = 1.23 == 1.23
print(type(flag)) # True
print(type(False))

print(float(123))
print(str(123))
print(int("123"))
print(bool(1)) # 1 = true, 0 = false

print(bool()) # empty, so false
print(bool("false")) # has a string, so true

print(1+2)
print(5-3)
print(3 * 2)
print(6/3) # division is ALWAYS a float
print(5 // 3) # removes decimal places, but gives integer value
print(2**2) # 2 ^ 2 exponents

weight = float(input("Enter your height in m: "))
height = float(input("Enter your weight in kgs: "))
bmi = weight / height**2

bmi = 84 / 1.65 ** 2
print(bmi)
print(round(bmi))
print(round(bmi, 2))

score = 0
score += 1 # score = score + 1
score -= 1 # score = score - 1
score *= 3 # score = score * 3
score /= 3 # score = score /3

print(f"Score is: {score}") # Skips data conversion


print("Welcome to my tip calculator")
bill = float(input("Enter your total bill: "))
tip = float(input("What percent tip would you like to give?"))
split = float(input("How many people are splitting the bill?"))
percent = 10 / 100
total = bill * percent
final = total / split
print(f"The final tip is: {round(final, 2)}")