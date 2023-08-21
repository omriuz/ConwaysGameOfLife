import pygame
import numpy as np
from random import randint

# constants variables
WIDTH, HEIGHT, CELL_SIZE = 140, 90, 8
WHITE, BLACK, GREEN, BLUE = (255, 0, 255), (0, 0, 0), (0, 255, 0), (0, 0, 128)
RED, BACKGROUND, GRID = (255, 0, 0), (10, 10, 40), (30, 30, 60)


class button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win):
        # Call this method to draw the button on the screen
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        font = pygame.font.SysFont('comicsans', 60)
        text = font.render(self.text, 1, (0, 0, 0))
        win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        # Pos is the mouse position
        # this method determines if the mouse position is over the button
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False


def freeze_cells(cells, surface):
    # a function that draws the cells into the screen in a constant way
    for r, c in np.ndindex(cells.shape):
        col = WHITE if cells[r, c] == 1 else BACKGROUND
        pygame.draw.rect(surface, col, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))
    return cells


def update_cells(old_cells, surface):
    # a function that updates the cells according to game rules
    new_cells = np.zeros((WIDTH, HEIGHT))
    for r, c in np.ndindex(old_cells.shape):
        new_cells[r, c] = update_cell(old_cells, (r, c))
        col = WHITE if new_cells[r, c] == 1 else BACKGROUND
        pygame.draw.rect(surface, col, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))
    return new_cells


def update_cell(cells, position):
    x, y = position
    status = cells[position]
    neighbour_cells = [(x - 1, y - 1), (x - 1, y + 0), (x - 1, y + 1),
                       (x + 0, y - 1), (x + 0, y + 1),
                       (x + 1, y - 1), (x + 1, y + 0), (x + 1, y + 1)]
    count = 0
    for x, y in neighbour_cells:
        # summing up the neighbours
        if x >= 0 and y >= 0:
            try:
                count += cells[x][y]
            except:
                pass
    # updating the cell value according to the rules
    if status == 1 and (count < 2 or count > 3):
        return 0
    elif status == 0 and count == 3:
        return 1
    return status


def init():
    # initiates a new zero's matrix
    cells = np.zeros((WIDTH, HEIGHT))
    return cells


def gliders(cells=init()):
    patterns = [np.array(
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0]]), ]
    pos = (3, 3)
    cells[pos[0]:pos[0] + patterns[0].shape[0], pos[1]:pos[1] + patterns[0].shape[1]] = patterns[0]
    return cells


def make_random_grid(cells):
    for r, c in np.ndindex(cells.shape):
        cells[r, c] = (randint(0, 1))
    return cells


def game_faze(index, state, run, cells, pause):
    # determines the next game faze according to the user's decision
    if state == 0:
        if index == 0:
            cells = gliders(cells)
        elif index == 1:
            cells = make_random_grid(cells)
        elif index == 2:
            state = 1
            cells = init()
        elif index == 3:
            pause = not pause
        elif index == 4:
            cells = init()
        else:
            run = False

    else:
        state = 0
        if index == 0:
            cells = init()
    return state, run, cells, pause


def welcome_lines(font):
    line_1 = font.render("Welcome to", True, WHITE)
    line_2 = font.render("Conway's Game Of Life", True, WHITE)
    line_3 = font.render("please choose an option", True, WHITE)
    line_1_Rect = line_1.get_rect()
    line_1_Rect.center = (925, 30)
    line_2_Rect = line_2.get_rect()
    line_2_Rect.center = (925, 70)
    line_3_Rect = line_3.get_rect()
    line_3_Rect.center = (925, 120)
    return ((line_1, line_1_Rect), (line_2, line_2_Rect), (line_3, line_3_Rect))


def you_choose_lines(font):
    line_1 = font.render("please choose", True, WHITE)
    line_2 = font.render("the pixels you", True, WHITE)
    line_3 = font.render("want to turn alive", True, WHITE)
    line_1_rect = line_1.get_rect()
    line_1_rect.center = (925, 30)
    line_2_rect = line_2.get_rect()
    line_2_rect.center = (925, 70)
    line_3_rect = line_3.get_rect()
    line_3_rect.center = (925, 110)
    return ((line_1, line_1_rect), (line_2, line_2_rect), (line_3, line_3_rect))


def check_for_clicks_on_buttons(pos, buttons):
    for i, button in enumerate(buttons):
        if button.is_over(pos):
            return True, i
    return False, 0


def check_for_clicks_on_squares(cells, pos):
    dimx, dimy = cells.shape
    x, y = pos[1] // CELL_SIZE, pos[0] // CELL_SIZE
    if 0 <= x < dimx and 0 <= y < dimy:
        if cells[x, y] == 1:
            return 0
        else:
            return 1


def draw_lines(lines, surface):
    surface.blit(lines[0][0], lines[0][1])
    surface.blit(lines[1][0], lines[1][1])
    surface.blit(lines[2][0], lines[2][1])


def main():
    pygame.init()
    surface = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
    pygame.display.set_caption("Conway's Game Of Life")
    font = pygame.font.Font('freesansbold.ttf', 32)
    buttons_1 = [button(GREEN, 800, 150, 250, 50, "Gliders"), button(GREEN, 800, 250, 250, 50, "Random"),
                 button(GREEN, 750, 350, 350, 50, "make your own"),
                 button(GREEN, 800, 450, 250, 50, "pause game"),
                 button(GREEN, 800, 550, 250, 50, "clear"), button(RED, 800, 650, 250, 50, "exit"),
                 ]
    buttons_2 = [button(GREEN, 800, 200, 250, 50, "go back"), button(GREEN, 750, 300, 350, 50, "finish choosing")]
    run, state, cells, pause = True, 0, init(), False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            pos = pygame.mouse.get_pos()
            surface.fill(GRID)
            if state == 0:
                lines = welcome_lines(font)
                buttons = buttons_1
            else:
                lines = you_choose_lines(font)
                buttons = buttons_2
            draw_lines(lines, surface)
            [button.draw(surface) for button in buttons]
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked, index = check_for_clicks_on_buttons(pos, buttons)
                if clicked:
                    state, run, cells, pause = game_faze(index, state, run, cells, pause)
                else:
                    try:
                        cells[pos[1] // CELL_SIZE, pos[0] // CELL_SIZE] = check_for_clicks_on_squares(cells, pos)
                    except:
                        pass
        if state == 0 and pause is False:
            cells = update_cells(cells, surface)
        else:
            cells = freeze_cells(cells, surface)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
