import pygame
from algorithms import *
from player import *


sides = {'top', 'bottom', 'right', 'left'}

class Grid:
    def __init__(self, rows, cell_w, margin) -> None:
        self.rows = rows
        self.cell_w = cell_w
        self.margin = margin
        self.W = self.rows * (self.cell_w) + self.margin * 2
        self.surf = pygame.Surface((self.W, self.W))

        self.grid = [Cell(i, j, self.cell_w) for j in range(self.rows) for i in range(self.rows)]

        self.maze_gen = MazeGen(self.grid, self.rows)
        
        self.render_algo = self.maze_gen.dfs

        self.player = Player(self.grid, self.cell_w)

    def render_grid(self, surf):
        self.render_algo()
            #self.path = PathFinder(self.grid, self.rows)
            #self.render_algo = self.path.dfs
        [cell.render(surf) for cell in self.grid]
        self.player.render(surf)

    def event(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.player.move("UP")
                elif e.key == pygame.K_DOWN:
                    self.player.move("DOWN")
                elif e.key == pygame.K_LEFT:
                    self.player.move("LEFT")
                elif e.key == pygame.K_RIGHT:
                    self.player.move("RIGHT")


        


class Cell:
    def __init__(self, i, j, width, wall_color = [100,10,150]) -> None:
        self.i, self.j = i, j
        self.x, self.y = i * width, j * width
        self.w = width
        self.color = [100,0,100]

        self.visited = False 
        self.traversed = False

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
        

    def get_neighbours(self, grid, rows):
        neighbours = {}

        top = self.index(grid, self.i, self.j-1, rows)
        bottom = self.index(grid, self.i, self.j+1, rows)
        right = self.index(grid, self.i+1, self.j, rows)
        left = self.index(grid, self.i-1, self.j, rows)

        if top and not top.visited:
            neighbours['top'] = top
        if bottom and not bottom.visited:
            neighbours['bottom'] = bottom
        if right and not right.visited:
            neighbours['right'] = right
        if left and not left.visited:
            neighbours['left'] = left


        return neighbours
    

    def get_visited_neighbours(self, grid, rows):
        neighbours = {}

        top = self.index(grid, self.i, self.j-1, rows)
        bottom = self.index(grid, self.i, self.j+1, rows)
        right = self.index(grid, self.i+1, self.j, rows)
        left = self.index(grid, self.i-1, self.j, rows)

        if top and top.visited:
            neighbours['top'] = top
        if bottom and bottom.visited:
            neighbours['bottom'] = bottom
        if right and right.visited:
            neighbours['right'] = right
        if left and left.visited:
            neighbours['left'] = left


        return neighbours

        


    def render(self, surf):
        if self.visited:
            if self.traversed:
                self.color = [max(c - 0.1, 150) for c in self.color]
            else:
                self.color = [max(c - 10, 0) for c in self.color]
            
            pygame.draw.rect(surf, self.color, [self.x, self.y, self.w, self.w])

            for side, is_wall in self.walls.items():
                if is_wall:
                    pygame.draw.line(surf, self.wall_color, self.wall_pos[side][0], self.wall_pos[side][1])
                        

