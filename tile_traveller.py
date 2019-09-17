# Step 1: Find valid moves for the first tile
# Step 2: Get a move from the user
# Step 3: If the move from the user is valid then move, othewise let him know that it is unvalid and get a new move from the user
# Step 4: Find valid moves for the next tile
# Step 5: Do step 2-4 until the user is in tile 3.1
# Step 6: Victory!



def direction_from_user():
    '''Gets a N, W, E or S from the user, (depending on where the user wants/can move) and returns it '''  


def valid_moves():
    '''Checks if input from user is valid, and returns True or None''' 


def move():
    '''Takes the current tile and move direction in and returns the new tile''' 
    return


start_position_float = 1.1


direction = direction_from_user()


position = start_position_float

while position != 3.1:
    if valid_moves(direction) == True:
        position = move()
        #látum position og direction í move fallið
        direction = direction_from_user()


    else:
        print("Not a valid direction!")
        direction = direction_from_user()

else:
    print("Victory!")
