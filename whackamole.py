import pygame
import random

GRID_WIDTH = 20
GRID_HEIGHT = 16
CELL_SIZE = 32
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE
LINE_COLOR = (0, 100, 0)
BACKGROUND_COLOR = "light green"

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        mole_image = pygame.transform.scale(mole_image, (CELL_SIZE, CELL_SIZE))
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Whack-A-Mole")
        clock = pygame.time.Clock()
        mole_position = (0, 0)

        def draw_grid():
            for x in range(0, SCREEN_WIDTH, CELL_SIZE):
                pygame.draw.line(screen, LINE_COLOR, (x, 0), (x, SCREEN_HEIGHT))
                
            for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
                pygame.draw.line(screen, LINE_COLOR, (0, y), (SCREEN_WIDTH, y))

        def get_random_position():
            grid_x = random.randrange(0, GRID_WIDTH) * CELL_SIZE
            grid_y = random.randrange(0, GRID_HEIGHT) * CELL_SIZE
            return grid_x, grid_y

        running = True
        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    mole_rect = pygame.Rect(mole_position, (CELL_SIZE, CELL_SIZE))

                    if mole_rect.collidepoint(mouse_pos):
                        mole_position = get_random_position()

            screen.fill(BACKGROUND_COLOR)
            draw_grid()
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_position))
            pygame.display.flip()

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
