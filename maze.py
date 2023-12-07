import pygame
from random import randint

sides = {'top', 'bottom', 'right', 'left'}

class Grid:
    def __init__(self, rows, cell_w, margin) -> None:
        self.rows = rows
        self.cell_w = cell_w
        self.margin = margin
        #self.grid = [Cell(x * self.cell_w + self.margin, y * self.cell_w + self.margin, self.cell_w) for y in range(self.rows) for x in range(self.rows)]
        self.grid = [Cell(i, j, self.cell_w) for j in range(self.rows) for i in range(self.rows)]
        
        self.curr_cell = self.grid[(len(self.grid)-1) // 2 + self.rows // 2]
        self.curr_cell.visited = True
        self.stack = []


    def dfs(self):
        next = self.curr_cell.check_neighbours(self.grid, self.rows)
        if next:
            next.visited = True

            self.stack.append(next)

            self.curr_cell.remove_wall(next)

            self.curr_cell = next
            
        elif len(self.stack) > 0:
            self.curr_cell = self.stack.pop()


    def render_grid(self, surf):
        [cell.render(surf) for cell in self.grid]
        pygame.draw.rect(surf, [100,0,10], [self.curr_cell.x, self.curr_cell.y, self.curr_cell.w, self.curr_cell.w])
        self.dfs()
        


class Cell:
    def __init__(self, i, j, width, wall_color = [150,150,150]) -> None:
        self.i, self.j = i, j
        self.x, self.y = i * width, j * width
        self.w = width
        self.color = [100,0,100]

        self.visited = False

        self.wall_color = wall_color
        self.walls = {side: True for side in sides}
        self.wall_pos = {
            'top': [(self.x, self.y), (self.x + self.w, self.y)],
            'bottom': [(self.x, self.y + self.w), (self.x + self.w, self.y + self.w)],
            'right': [(self.x + self.w, self.y), (self.x + self.w, self.y + self.w)],
            'left': [(self.x, self.y), (self.x, self.y + self.w)]
        }

    def index(self, i, j, rows):
        if 0 <= i < rows and 0 <= j < rows:
            return i + j * rows
        return -1
        
    def grid_cell_s(self, grid, i):
        if i > -1:
            return grid[i]
        return None

    def check_neighbours(self, grid, rows):
        neighbours = []

        top = self.grid_cell_s(grid, self.index(self.i, self.j-1, rows))
        bottom = self.grid_cell_s(grid, self.index(self.i, self.j+1, rows))
        right = self.grid_cell_s(grid, self.index(self.i+1, self.j, rows))
        left = self.grid_cell_s(grid, self.index(self.i-1, self.j, rows))


        if top and not top.visited:
            neighbours.append(top)
        if bottom and not bottom.visited:
            neighbours.append(bottom)
        if right and not right.visited:
            neighbours.append(right)
        if left and not left.visited:
            neighbours.append(left)

        if neighbours:
            return neighbours[randint(0,len(neighbours)-1)]

    def remove_wall(self, next):
        if self.i > next.i:
            self.walls['left'] = False
            next.walls['right'] = False
        elif self.i < next.i:
            self.walls['right'] = False
            next.walls['left'] = False
        elif self.j > next.j:
            self.walls['top'] = False
            next.walls['bottom'] = False
        elif self.j < next.j:
            self.walls['bottom'] = False
            next.walls['top'] = False

        


    def render(self, surf):
        if self.visited:
            pygame.draw.rect(surf, self.color, [self.x, self.y, self.w, self.w])
            self.color = [max(c - 5, 0) for c in self.color]
            for side, is_wall in self.walls.items():
                if is_wall:
                    pygame.draw.line(surf, self.wall_color, self.wall_pos[side][0], self.wall_pos[side][1])
                        
        #pygame.draw.rect(surf, self.color, [self.x, self.y, self.w, self.w])

