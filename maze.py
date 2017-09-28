def prettyprint(mat):
    for row in mat:
        print(row)

def answer(maze):
    height = len(maze)
    width = len(maze[0])
    shortest_path = [[[1000,1000] for col in row] for row in maze]
    stack=[]
    stack.append((0,0,1,0))
    while stack:
        item = stack.pop(0)
        row = item[0]
        col = item[1]
        steps = item[2]
        wall_removed = item[3]

        if steps < shortest_path[row][col][wall_removed]: 
            shortest_path[row][col][wall_removed] = steps
        else:
            continue

        moves = [(-1,0), (0,-1), (0,1), (1,0)]
        for i,j in moves:
            if row + i >= 0 and row + i < height and col + j >= 0 and col + j < width:
                if maze[row+i][col+j] == 0:
                    stack.append((row+i, col+j, steps+1, wall_removed))
                if wall_removed == 0 and maze[row+i][col+j] == 1:
                    stack.append((row+i, col+j, steps+1, 1))

    prettyprint(maze)
    prettyprint(shortest_path)
    return min(shortest_path[height-1][width-1])
                

maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
print(answer(maze))

maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(answer(maze))

maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(answer(maze))

maze = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
print(answer(maze))

maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0,0,1,0,0,0]]
print(answer(maze))
