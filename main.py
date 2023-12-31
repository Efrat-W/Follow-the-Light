import pygame
from maze import *
from sys import exit

class Main:
    def __init__(self):
        pygame.init()
        self.cell_w = 22
        self.margin = 20
        self.rows = 20
        self.W = self.rows * (self.cell_w - 4) +6

        win_res = (self.W, self.W)
        self.win = pygame.display.set_mode([i * 1.4 for i in win_res])
        self.display = pygame.Surface((self.W, self.W))
        pygame.display.set_caption("Seek the Light")

        self.clock = pygame.time.Clock()

        self.grid = Grid(self.rows, self.cell_w, self.margin)

    def event(self):
        trail = self.grid.player.curr_cell.trail
        trail.append(Particle(self.grid.player.curr_cell.x + self.grid.player.curr_cell.w//2, self.grid.player.curr_cell.y + self.grid.player.curr_cell.w//1.5, self.grid.player.curr_cell.w, (255,220,100)))
        for particle in trail:
            particle.update()
            if particle.radius <= 0:
                trail.remove(particle)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.grid.player.move("UP")
                elif e.key == pygame.K_DOWN:
                    self.grid.player.move("DOWN")
                elif e.key == pygame.K_LEFT:
                    self.grid.player.move("LEFT")
                elif e.key == pygame.K_RIGHT:
                    self.grid.player.move("RIGHT")
                elif e.key == pygame.K_SPACE:
                        self.restart()

    def restart(self):
        self.grid = Grid(self.rows, self.cell_w, self.margin)
        self.start_ticks = pygame.time.get_ticks()

    def run(self):
        start_ticks = pygame.time.get_ticks()

        while True:
            self.display.fill((0,0,0))

            
            self.event()
                    
                
            self.grid.render_grid(self.display)


            if self.grid.player.win:
                time = (end_ticks - start_ticks) // 1000
                # Create a semi-transparent surface
                semi_transparent_surface = pygame.Surface(self.display.get_size(), pygame.SRCALPHA)
                semi_transparent_surface.fill((255, 200, 0, 150))  

                self.display.blit(semi_transparent_surface, (0, 0))

                #text = font.render("WIN", True, (255, 255, 255)) 
                text = pygame.font.Font(None, rows*2).render(f"Your time: {time} seconds", True, (255, 255, 255))
                restart_text = pygame.font.Font(None, int(rows*1.2)).render("Press <SPACE> to restart", True, (200, 200, 200))

                center_x = self.display.get_width() // 2
                center_y = self.display.get_height() // 2

                text_rect = text.get_rect(center=(center_x, center_y - rows*1.5))
                restart_rect = text.get_rect(center=(center_x, center_y + rows*1.5))


                self.display.blit(text, text_rect)
                self.display.blit(restart_text, restart_rect)
            else:
                end_ticks = pygame.time.get_ticks()

            self.win.blit(pygame.transform.scale(self.display, self.win.get_size()), (0,0))

            pygame.display.update()
            self.clock.tick(100)


if __name__ == '__main__':
    Main().run()