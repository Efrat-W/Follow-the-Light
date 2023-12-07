
class MazeGen():
    def __init__(self, grid, rows) -> None:
        self.grid = grid
        self.rows = rows
        self.curr_cell = self.grid[0]
        self.curr_cell.visited = True
        self.stack = []

    def dfs(self):
        next = self.curr_cell.check_neighbours(self.grid, self.rows)
        if next:
            next.visited = True

            self.stack.append(next)

            self.remove_wall(next)

            self.curr_cell = next
            
        elif len(self.stack) > 0:
            self.curr_cell = self.stack.pop()

        
    def remove_wall(self, next):
        if self.curr_cell.i > next.i:
            self.curr_cell.walls['left'] = False
            next.walls['right'] = False
        elif self.curr_cell.i < next.i:
            self.curr_cell.walls['right'] = False
            next.walls['left'] = False
        elif self.curr_cell.j > next.j:
            self.curr_cell.walls['top'] = False
            next.walls['bottom'] = False
        elif self.curr_cell.j < next.j:
            self.curr_cell.walls['bottom'] = False
            next.walls['top'] = False
        


