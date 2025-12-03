player_health = 20 # Declared outside the function with a global scope.

def game():
    def drink_potion():
        potion_power = 2
        print(potion_power)
        print(player_health) # Can be called inside a function aswell as outside the function.

drink_potion() # Cannot call this function because it has a local scope inside the game() function.

# NAME SPACE --> Anything you give a name to is a 'namespace'
# EX: Variables, functions, lists, dicts, etc


