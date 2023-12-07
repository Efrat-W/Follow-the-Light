import pygame
from random import randint
from algorithms import *

sides = {'top', 'bottom', 'right', 'left'}

class Grid:
    def __init__(self, rows, cell_w, margin) -> None:
        self.rows = rows
        self.cell_w = cell_w
        self.margin = margin
        self.W = self.rows * (self.cell_w) + self.margin * 2
        self.surf = pygame.Surface((self.W, self.W))

        self.grid = [Cell(i, j, self.cell_w) for j in range(self.rows) for i in range(self.rows)]

        #self.render_algo = dfs(self.grid, self.rows)
        self.maze_gen = MazeGen(self.grid, self.rows)
        



    def render_grid(self, surf):
        [cell.render(surf) for cell in self.grid]
        #self.render_algo()
        self.maze_gen.dfs()
        


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

    def index(self, grid, i, j, rows):
        if 0 <= i < rows and 0 <= j < rows:
            return grid[i + j * rows]
        return None
        

    def check_neighbours(self, grid, rows):
        neighbours = []

        top = self.index(grid, self.i, self.j-1, rows)
        bottom = self.index(grid, self.i, self.j+1, rows)
        right = self.index(grid, self.i+1, self.j, rows)
        left = self.index(grid, self.i-1, self.j, rows)


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

        


    def render(self, surf):
        if self.visited:
            pygame.draw.rect(surf, self.color, [self.x, self.y, self.w, self.w])
            self.color = [max(c - 5, 0) for c in self.color]
            for side, is_wall in self.walls.items():
                if is_wall:
                    pygame.draw.line(surf, self.wall_color, self.wall_pos[side][0], self.wall_pos[side][1])
                        
        #pygame.draw.rect(surf, self.color, [self.x, self.y, self.w, self.w])

