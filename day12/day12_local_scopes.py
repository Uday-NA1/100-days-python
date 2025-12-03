def drink_potion():
    potion_strength = 2 # Declared inside the function with a local scope
    print(potion_strength)


print(potion_strength) # NameError because 'power' has a local scope and cannot be run outside the function

# Creating a variable /function inside another function cannot be accessed outside the function because it has a 'local scope'
