import pygame

rows = 26

class Player:
    def __init__(self, grid, cell_size):
        self.grid = grid
        self.cell_size = cell_size
        self.curr_cell = grid[0]
        
        self.curr_cell.traversed = True
        #self.rect = pygame.Rect(self.curr_cell.x, self.curr_cell.y, cell_size, cell_size)

    def move(self, direction):
        if direction == "UP":
            self.try_move(0, -1)
        elif direction == "DOWN":
            self.try_move(0, 1)
        elif direction == "LEFT":
            self.try_move(-1, 0)
        elif direction == "RIGHT":
            self.try_move(1, 0)

    def try_move(self, dx, dy):
        next = self.curr_cell.index(self.grid, self.curr_cell.i + dx, self.curr_cell.j + dy, rows)

        neighbours = self.curr_cell.get_visited_neighbours(self.grid, rows)
        neighs = {k: v for k, v in neighbours.items() if not self.curr_cell.walls[k]}

        if next in neighs.values():
            self.curr_cell.trail = []
            self.curr_cell = next
            self.curr_cell.traversed = True

    def render(self, surf):
        self.curr_cell.color = [255,255,100]
        self.curr_cell.render(surf)

