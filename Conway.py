import pygame
import numpy as np

pygame.init()

# ----------Initial Setting----------
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
CELL_SIZE = 5

ROW_NUMBER = SCREEN_HEIGHT // CELL_SIZE
COLUMN_NUMBER = SCREEN_WIDTH // CELL_SIZE
cell = np.zeros((ROW_NUMBER, COLUMN_NUMBER))

FPS = 20
FONT = pygame.font.SysFont("Arial", 20)
BACK_GROUND = "#222222"  # Onyx Black
OFF_COLOR = "#111111"  # Onyx Black
COLOR = "#D1D1D1"  # Off White


# ----------Render Screen every run cycle----------
def render(pause,cell):
    screen.fill(BACK_GROUND)
    clone = cell
    for row in range(ROW_NUMBER):
        for col in range(COLUMN_NUMBER):
            if not pause:
                counter = np.sum(clone[row-1:row+2,col-1:col+2]) - clone[row,col]
                if clone[row,col] == 1:
                    if counter < 2 or counter > 3:
                        cell[row,col] = 0
                elif clone[row,col] == 0:
                    if counter == 3:
                        cell[row,col] = 1

            if cell[row,col] == 1:
                pygame.draw.rect(screen, COLOR, (row * CELL_SIZE, col * CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1))
            else:
                pygame.draw.rect(screen, OFF_COLOR, (row * CELL_SIZE, col * CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1))

# ----------Main Module----------
def main():
    # ----------Variable----------
    clock = pygame.time.Clock()

    # ----------Main loop----------
    run = True
    pause = True
    while run:
        # ----------Quit Event Handling----------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_SPACE:
                    pause = not pause
                    render(pause,cell)
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cell[pos[0] // CELL_SIZE,pos[1] // CELL_SIZE] = 1
                render(pause,cell)

        pygame.display.update()

        # ----------Render Object----------
        render(pause,cell)

        # ----------Define FPS----------
        clock.tick(FPS)


# ----------Main Program----------
pygame.display.set_caption("Conway's Game of Life")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

if __name__ == "__main__":
    main()
