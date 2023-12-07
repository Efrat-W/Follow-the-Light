import pygame
from maze import *
from sys import exit
from random import random

class Main:
    def __init__(self):
        pygame.init()
        self.cell_w = 20
        self.margin = 2
        self.rows = 26
        self.W = self.rows * (self.cell_w) + self.margin * 2

        win_res = (self.W, self.W)
        self.display = pygame.display.set_mode(win_res)
        pygame.display.set_caption("Maze Generator")

        self.clock = pygame.time.Clock()

        self.grid = Grid(self.rows, self.cell_w, self.margin)



    def event(self):
        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()




    def run(self):
        while True:
            self.display.fill((220,150,220))

            self.event()
            #self.gen_grid()
            self.grid.render_grid(self.display)
            

            self.display.blit(pygame.transform.scale(self.display, self.display.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    Main().run()