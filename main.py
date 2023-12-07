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
        self.win = pygame.display.set_mode(win_res)
        self.display = pygame.Surface((self.W, self.W))
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
            self.display.fill((0,255,255))

            self.event()
            #self.gen_grid()
            self.grid.render_grid(self.display)
            



            self.win.blit(pygame.transform.scale(self.display, self.win.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(10)


if __name__ == '__main__':
    Main().run()