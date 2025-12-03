game_level = 3
enemies = ['Skeleton', 'Zombies', 'Alien']

# if game_level < 5:
#     new_enemy = enemies[0] # Variables / namespaces inside a block [if/while/for/etc] will have the scope of the block.
#                         #    Example: this one has a global scope, since the 'if' statement has a global scope.
def create_army():
    if game_level < 5:
        new_enemy = enemies[0] # HERE: it has a local scope because the 'if' statement has a local scope

    print(new_enemy)

    # Here there may be a warning because 'new_enemy' might not exist if the if statement is false. You can bypass by adding an
    # empty variable earlier before the if statement


