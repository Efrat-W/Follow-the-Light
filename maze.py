import pygame
from algorithms import *
from player import *
from random import randint


sides = {'top', 'bottom', 'right', 'left'}

class Grid:
    def __init__(self, rows, cell_w, margin) -> None:
        self.rows = rows
        self.cell_w = cell_w -4
        self.margin = margin
        self.W = self.rows * (self.cell_w)
        self.surf = pygame.Surface((self.W, self.W))

        self.grid = [Cell(i, j, self.cell_w, is_goal= i == j == rows-1 ) for j in range(self.rows) for i in range(self.rows)]


        self.maze_gen = MazeGen(self.grid, self.rows)
        
        self.render_algo = self.maze_gen.dfs

        self.player = Player(self.grid, self.cell_w)

    def render_grid(self, surf):
        self.render_algo()
            #self.path = PathFinder(self.grid, self.rows)
            #self.render_algo = self.path.dfs
        [cell.render(surf) for cell in self.grid]
        self.player.render(surf)
        self.grid[-1].update_trail()
        #self.spotlight()

    def spotlight(self):
        spot_surf = pygame.Surface(self.surf.get_size(), pygame.SRCALPHA)
        radius = self.cell_w * 3
        center = [i//2 for i in self.surf.get_size()]

        while radius > self.cell_w:
            # add circles of radius value alpha,
            pygame.draw.circle(spot_surf, (255, 255, 255, radius), center, radius)
            radius -= 5
        self.surf.blit(spot_surf, (self.player.curr_cell.x, self.player.curr_cell.y))



class Cell:
    def __init__(self, i, j, width, wall_color = [50,10,100], is_goal = False) -> None:
        self.i, self.j = i, j
        self.x, self.y = i * width + 2, j * width + 2
        self.w = width
        
        self.trail = []
        self.goal = is_goal
        self.color = [100,0,100] if not self.goal else [240,200,100]

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
    
    def update_trail(self):
        self.trail.append(Particle(self.x+self.w//2, self.y, self.w, (255,220,100)))
        for particle in self.trail:
            particle.update()
            if particle.radius <= 0:
                self.trail.remove(particle)

    def render(self, surf):
        if self.visited:
            if self.traversed:
                self.color = [max(c - c * 0.005, 5) for c in self.color]
            elif self.goal:
                pass
            else:
                self.color = [max(c - c * 0.1, 0) for c in self.color]
            
            pygame.draw.rect(surf, self.color, [self.x, self.y, self.w, self.w])

            for side, is_wall in self.walls.items():
                if is_wall:
                    pygame.draw.line(surf, self.wall_color, self.wall_pos[side][0], self.wall_pos[side][1], 2)

        for particle in self.trail:
            particle.render(surf)
                        

class Particle:
    def __init__(self, x, y, size, color) -> None:
        offset_x = randint(-5, 5)
        offset_y = randint(-5, 5)
        self.pos = [x + offset_x, y + offset_y]
        self.radius = randint(size//5,size//2)
        #self.timer = self.radius
        self.color = color

    def update(self):
        #self.timer -= 1
        self.radius -= 0.3
        self.pos[1] -= 1

    def render(self, surface):
        radius = self.radius
        color = [max(50, c - 0.5) for c in self.color]
        part_surface = pygame.Surface((radius*2, radius*2))
        pygame.draw.circle(part_surface, color, (radius, radius), radius)
        part_surface.set_colorkey((0,0,0))
        part_surface.set_alpha(25 * self.radius)
        surface.blit(part_surface, (int(self.pos[0] - radius), int(self.pos[1] - radius)))