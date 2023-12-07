def dfs(grid):
    next = grid.curr_cell.check_neighbours(grid.grid, grid.rows)
    if next:
        next.visited = True

        grid.stack.append(next)

        grid.curr_cell.remove_wall(next)

        grid.curr_cell = next
        
    elif len(grid.stack) > 0:
        grid.curr_cell = grid.stack.pop()
        
