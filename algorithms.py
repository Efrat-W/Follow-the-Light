
from random import randint, choice
from collections import deque


class MazeGen():
    def __init__(self, grid, rows) -> None:
        self.grid = grid
        self.rows = rows
        self.curr_cell = self.grid[0]
        self.curr_cell.visited = True
        self.stack = []

        self.count = 0

    def dfs(self):
        #next = self.curr_cell.check_neighbours(self.grid, self.rows)
        neighbours = self.curr_cell.get_neighbours(self.grid, self.rows)
        
        if neighbours:
            next = choice(list(neighbours.values()))
            next.visited = True

            self.stack.append(next)

            self.remove_wall(next)

            self.curr_cell = next
            
            self.count += 1

        elif len(self.stack) > 0:
            self.curr_cell = self.stack.pop()

        elif self.count >= self.rows * self.rows -1:
            return True


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
        

class PathFinder():
    def __init__(self, grid, rows) -> None:
        #self.grid = [setattr(cell, 'visited', False) or cell for cell in grid]
        self.grid = grid
        self.rows = rows
        self.end = [grid[-1].i, grid[-1].j]
        self.curr_cell = self.grid[0]
        self.curr_cell.visited = True
        self.stack = []


    def dfs(self):
        neighbours = self.curr_cell.get_neighbours(self.grid, self.rows)
        
        neighbours = {k: v for k, v in neighbours.items() if not self.curr_cell.walls[k]}
        self.curr_cell.color = [255,255,255]

        if neighbours:
            next = choice(list(neighbours.values()))

            if next.i == self.end[0] and next.j == self.end[1]:
                self.show_path()
                return True
            
            next.visited = True
            next.color = [255,255,255]

            self.stack.append(next)

            self.curr_cell = next
            
        elif len(self.stack) > 0:
            self.curr_cell = self.stack.pop()

    def show_path(self):
        for cell in self.stack:
            cell.color = [min(c - 5, 100) for c in cell.color]


