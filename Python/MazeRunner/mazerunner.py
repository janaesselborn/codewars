import numpy as np

def maze_runner(maze, directions):
    start_pos = get_start_position(maze)
    return go_into_maze(start_pos, directions, maze)    

# Looking for the starting position
def get_start_position(maze):
    start_pos = np.argwhere(np.array(maze) == 2)
    return start_pos[0]

# Go through the given directions
def go_into_maze (start_pos, directions, maze):
    actual_pos = start_pos
    for direction in directions:
        actual_pos = go_step(actual_pos, direction)
        status = check_pos(actual_pos, maze)
        if (status != 0):
            return status
    return "Lost"

# Go the step into the right direction
def go_step (pos, direction):  
    if direction == "N":
        return [pos[0] - 1 , pos[1]]
    if direction == "E":
        return [pos[0] , pos[1] + 1]
    if direction == "S":
        return [pos[0] + 1 , pos[1]]
    if direction == "W":
        return [pos[0] , pos[1] - 1]

# Checking the actual position
def check_pos (pos, maze):
    # out of maze border
    if (pos[0] < 0 or pos[1] < 0 or pos[0] >= len(maze) or pos[1] >= len(maze)):
        return "Dead"
    # correct position to go
    elif (maze[pos[0]][pos[1]] == 0 or maze[pos[0]][pos[1]] == 2):
        return 0
    # run into a wall
    elif (maze[pos[0]][pos[1]] == 1):
        return "Dead"
    # get the finish point
    elif (maze[pos[0]][pos[1]] == 3):
        return "Finish"