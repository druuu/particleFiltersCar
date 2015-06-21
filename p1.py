grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0]]

walls = []

def gridWalls(grid):
    xGrid = len(grid[0])
    yGrid = len(grid)
    for i in xrange(yGrid):
        for j in xrange(xGrid):
            if grid[i][j] == 1:
                walls.append((xGrid * i) + j)

gridWalls(grid)

print walls
