import numpy as np

with open('day02.input') as f:
    data = [[x for x in line.strip()] for line in f]


def part1(start_at):
    code = ''
    # make keypad
    grid = np.array([(1,2,3),(4,5,6),(7,8,9)])
    height = grid.shape[1]-1
    width = grid.shape[0]-1

    # Calculate starting position on keypad
    row, col = np.where(grid==start_at)
    pos = [row[0], col[0]]

    for cmd in data:
        for step in cmd:
            if step == 'U':
                # can we move up?
                if pos[0]-1 >= 0:
                    pos[0] = pos[0]-1
            elif step == 'D':
                #can we go down?
                if pos[0]+1 <= height:
                    pos[0] = pos[0]+1
            elif step == 'L':
                # can we go left?
                if pos[1]-1 >= 0:
                    pos[1] = pos[1]-1
            elif step == 'R':
                # can we go right?
                if pos[1]+1 <= width:
                    pos[1] = pos[1]+1

        code += str(grid[pos[0],pos[1]])

    return code


def part2(start_at):
    code = ''
    # make keypad
    grid = np.array([(0,0,1,0,0),
                     (0,2,3,4,0),
                     (5,6,7,8,9),
                     (0,'A','B','C',0),
                     (0,0,'D',0,0)])
    height = grid.shape[1]-1
    width = grid.shape[0]-1

    # Calculate starting position on keypad
    row, col = np.where(grid==start_at)
    row = row[0]
    col = col[0]

    for cmd in data:
        for step in cmd:
            if step == 'U':
                # can we move up?
                if row-1 >= 0 and grid[row-1,col] != '0':
                    row = row-1
            elif step == 'D':
                #can we go down?
                if row+1 <= height and grid[row+1,col] != '0':
                    row = row+1
            elif step == 'L':
                # can we go left?
                if col-1 >= 0 and grid[row,col-1] != '0':
                    col = col-1
            elif step == 'R':
                # can we go right?
                if col+1 <= width and grid[row,col+1] != '0':
                    col = col+1

        code += str(grid[row,col])

    return code

print(part1(5))
print(part2('5'))
