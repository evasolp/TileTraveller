# Step 1: Find valid moves for the first tile
# Step 2: Get a move from the user
# Step 3: If the move from the user is valid then move, othewise let him know that it is unvalid and get a new move from the user
# Step 4: Find valid moves for the next tile
# Step 5: Do step 2-4 until the user is in tile 3.1
# Step 6: Victory!

def print_valid_moves(position):
    '''Takes in the position and prints out the valid moves'''
    if position == 1.1 or position == 2.1:
        print('You can travel: (N)orth.')
    elif position == 1.2:
        print('You can travel: (N)orth or (E)ast or (S)outh.')
    elif position == 1.3:
        print('You can travel: (E)ast or (S)outh.')
    elif position == 2.2 or position == 3.3:
        print('You can travel: (S)outh or (W)est.')
    elif position == 2.3:
        print('You can travel: (E)ast or (W)est.')
    elif position == 3.2:
        print('You can travel: (N)orth or (S)outh.')


def direction_from_user():
    '''Gets a N, W, E or S from the user, (depending on where the user wants/can move) and returns it '''  
    direction = input('Direction: ')
    return direction

def is_move_valid(position, direction):
    '''Takes in the direction from user and the current position and checks if the direction is valid, and returns True or None''' 
    result = False
    if direction == 'n' or direction == 'N':
        if position == 1.1 or position == 2.1 or position == 1.2 or position == 3.2:
            result = True
    if direction == 's' or direction == 'S':
        if position == 1.2 or position == 1.3 or position == 2.2 or position == 3.3 or position == 3.2:
            result = True
    if direction == 'e' or direction == 'E':
        if position == 1.2 or position == 1.3 or position == 2.3:
            result = True
    if direction == 'w' or direction == 'W':
        if position == 2.2 or position == 3.3 or position == 2.3:
            result == True
    return result

def move():
    '''Takes the current tile and move direction in and returns the new tile''' 
    #Nota að hækka/lækka um heilan eða 0.1
    return


start_position_float = 1.1





position = start_position_float

while position != 3.1:
    print_valid_moves(position)
    direction = direction_from_user()

    if valid_moves(direction) == True:
        position = move()
        #látum position og direction í move fallið
        direction = direction_from_user()


    else:
        print("Not a valid direction!")
        direction = direction_from_user()

else:
    print("Victory!")
