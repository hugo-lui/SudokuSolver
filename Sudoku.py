def valid(grid, r, c, value):
    row = value not in grid[r]
    column = value not in [grid[i][c] for i in range(9)]
    box = value not in [grid[i][j] for i in range(r // 3 * 3, r // 3 * 3 + 3) for j in range(c // 3 * 3, c // 3 * 3 + 3)]
    return row and column and box

def solve(grid, r = 0, c = 0):
    if r == 9:
        return True
    elif c == 9:
        return solve(grid, r + 1, 0)
    elif grid[r][c] != 0:
        return solve(grid, r, c + 1)
    else:
        for i in range(1, 10):
            if valid(grid, r, c, i):
                grid[r][c] = i
                if solve(grid, r, c + 1):
                    return True
                else:
                    grid[r][c] = 0
        return False