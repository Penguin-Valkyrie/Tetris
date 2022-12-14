import pygame

# Initiate
pygame.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Tetris")

# Global Variables
grid_size = 30
game_over = False
cols = screen.get_width() // grid_size
rows = screen.get_height() // grid_size
x_gap = (screen.get_width() - (cols * grid_size)) / 2
y_gap = (screen.get_height() - (rows * grid_size)) / 2
clock = pygame.time.Clock()
fps = 4

# 0 1 2 
# 3 4 5
# 6 7 8

blocks = [
    [[1, 4, 7], [3, 4, 5]], # straight
    [[1, 3, 4, 5, 7]], #cross
    [[0, 1, 4, 5], [1, 3, 4, 6]], #tank 1
    [[1, 2, 3, 4], [0, 3, 4, 7]], #tank 2
    [[0, 1, 3, 6], [0, 1, 2, 5], [2, 5, 7, 8], [3, 6, 7, 8]], # L1
    [[1, 2, 5, 8], [5, 6, 7, 8], [0, 3, 6, 7], [0, 1, 2, 3]], # L2
    [[4, 6, 7, 8], [0, 3, 4, 6], [0, 1, 2, 4], [2, 4, 5, 8]] # shooter
]

# Classes
class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = 3
        self.rotation = 1

    def shape(self):
        return blocks[self.type][self.rotation]

# Functions
def draw_grid(grid_size):

    for y in range(int(rows)):
        for x in range(int(cols)):
            pygame.draw.rect(screen, (100, 100, 100), 
            [x * grid_size + x_gap, y * grid_size + y_gap, grid_size, grid_size], 1)

def draw_block():
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                pygame.draw.rect(screen, (255, 255, 255), 
                                [(x + block.x) * grid_size + x_gap + 1, 
                                 (y + block.y) * grid_size + y_gap + 1,
                                 grid_size - 2, grid_size - 2])

def drop_block():
    can_drop = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if block.y + y >= rows - 1:
                    can_drop = False
    
    if can_drop:
        block.y += 1

def side_move(dx):
    can_move = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if x + block.x >= cols - 1 and dx == 1:
                    can_move = False
                elif x + block.x < 1 and dx == -1:
                    can_move = False
   
    if can_move:
        block.x += dx

# Object Declaration
block = Block(5, 6)

# Game Loop
while not game_over:    

    clock.tick(fps)

    # Check for input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            side_move(-1)
        if event.key == pygame.K_RIGHT:
            side_move(1)
        

    screen.fill((0, 0, 0))

    draw_grid(grid_size)
    
    if event.type != pygame.KEYDOWN:    
        drop_block()

    draw_block()

    pygame.display.update()

pygame.quit()
