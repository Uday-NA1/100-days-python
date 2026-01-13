file = open("my_file.txt")
contents = file.read()
print(contents)

file.close() # Close the file so that it doesn't stay cached --> We don't want it to waste resources

# Instead use this which is more efficient:

with open("my_file.txt") as file:         # The default mode is read only. Look lower for append mode.
    contents = file.read()
    print(contents)

# No need to close as it gets closed when you exit the 'with' section

with open("my_file.txt", mode="a") as file:       # The 'a' mode is the append mode. It ADDS new things.
    file.write("\nNew Text.")   # REMEMBER: Remember it will be placed at the absolute end.

# Using the 'w' mode will replace all the contents with the new text. This does not append only replaces.

# Absolute file paths ---> Starts from the origin / root

# Relative file paths ---> Starts from working directory (the folder you are currently working from)

# /../ goes one folder up (relative)