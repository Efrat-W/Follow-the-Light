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



    def run(self):
        while True:
            self.display.fill((10,10,10))

            self.grid.event()
            #self.gen_grid()
            self.grid.render_grid(self.display)

            self.display.blit(pygame.transform.scale(self.display, self.display.get_size()), (0,0))

            # Assuming self.display is your pygame Surface object
            if self.grid.player.win:
                # Create a semi-transparent surface
                semi_transparent_surface = pygame.Surface(self.display.get_size(), pygame.SRCALPHA)
                semi_transparent_surface.fill((255, 200, 0, 150))  # RGBA for semi-transparent orangish-yellow

                # Blit the semi-transparent surface onto the display
                self.display.blit(semi_transparent_surface, (0, 0))

                # Create a font object
                font = pygame.font.Font(None, 72)  # You can adjust the size

                # Render the text
                text = font.render("WIN", True, (255, 255, 255))  # White text

                # Get the center of the display
                center_x = self.display.get_width() // 2
                center_y = self.display.get_height() // 2

                # Get the center of the text
                text_rect = text.get_rect(center=(center_x, center_y))

                # Blit the text onto the display
                self.display.blit(text, text_rect)


            pygame.display.update()
            self.clock.tick(100)


if __name__ == '__main__':
    Main().run()