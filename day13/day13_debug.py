# # Describe your problem - ask questions - answer the questions - write comments - go through the code's flow and find the mistake

# # When bugs occur only under certain scenarios - like index out of range when using randint to get a random value from a list
# # In this scenario - try to find out what scenarios it happens and recreate this bug
# # Then proceed to fix the bug

# # Play Computer ---> Act like a computer and read through the lines of code to find errors - watch out for logic and syntax.
# # Make sure to read the code line-by-line

# # In consecutive if..elif...else watch out for >= and >= for gaps in the values

# # Watch out for red lines - but sometimes there are console errors that show up only *if* something happens. This needs to be
# # trial-based checked

# # You can use stackoverflow, documentation, and other cs communities to find other people with similar errors or ask questions.

# # You can use try blocks aswell

# try:
#     age = int(input("Enter your age: "))
# except ValueError:
#     print("You have typed an invalid response. Please try again.")
#     age = int(input("Enter your age: "))

# # Sometimes there are bugs that won't show as bugs in console or red lines or any other way. They pass but are logically
# # just different from what you want. These are the worst types of errors. Simple example:

# print("Your age is {age}")

# # Here no error is detected by your computer. You need to find it yourself. The error here is the f-string

# # Print statements help a lot when trying to solve bugs.

# words_per_page = 0
# pages = int(input("Number of pages: "))
# words_per_page == int(input("Number of words per page: "))
# total_words = words_per_page * pages

# print(f"pages = {pages}") # DEBUG
# print(f"words per page = {words_per_page}") # DEBUG

# print(total_words)

# # The result here for words_per_page is 0. Finding out is simple, by simply printing things out into the console for debugging purposes.

# # Here, in words_per_page == int(input) it uses 2 equal signs, which is a comparison and results in False or True (bool)

# # By fixing the equal to mark, the code will resume working perfectly fine and you can remove the 2 debug print statements
# # added in the middle

# Debugger:

import random, day13_maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item = day13_maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

# Use break points, red dots, on the left side (gutter) so that the debugger runs the code until that point and shows
# tracing of values which can help debugging. Can also use for line-by-line checking. Now we can see that it jumps back up
# instead of appending the list at the start. It does it only for the last value.

# The error is: The line has toe be indented (in line 62)

# You can also use 'step into' in lines with modules to see the function behind the module.