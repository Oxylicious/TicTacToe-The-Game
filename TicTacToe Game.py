import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 300, 400  # Increase height to add space for the text
line_width = 15
board_rows = 3
board_cols = 3
square_size = width // board_cols
circle_radius = square_size // 3
circle_width = 15
cross_width = 25
space = square_size // 4
bg_color = (255, 213, 166)
line_color = (255, 173, 82)
circle_color = (255, 48, 48)
cross_color = (84, 84, 84)
text_color = (80, 80, 80)

# Fonts
font = pygame.font.Font(None, 40)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(bg_color)

# Board setup
board = [[0] * board_cols for _ in range(board_rows)]

# Functions to draw the game elements
def draw_lines():
    for row in range(1, board_rows):
        pygame.draw.line(screen, line_color, (0, row * square_size), (width, row * square_size), line_width)
    for col in range(1, board_cols):
        pygame.draw.line(screen, line_color, (col * square_size, 0), (col * square_size, board_rows * square_size), line_width)

def draw_figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen, circle_color, (col * square_size + square_size // 2, row * square_size + square_size // 2), circle_radius, circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, cross_color, (col * square_size + space, row * square_size + square_size - space), (col * square_size + square_size - space, row * square_size + space), cross_width)
                pygame.draw.line(screen, cross_color, (col * square_size + space, row * square_size + space), (col * square_size + square_size - space, row * square_size + square_size - space), cross_width)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in board:
        for cell in row:
            if cell == 0:
                return False
    return True

def check_win(player):
    # Vertical check
    for col in range(board_cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    # Horizontal check
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True

    # Ascending diagonal check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True

    # Descending diagonal check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    return False

def restart():
    screen.fill(bg_color)
    draw_lines()
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0

def display_message(message):
    screen.fill(bg_color, (0, 300, width, 100))  # Clear the area where the text is displayed
    text = font.render(message, True, text_color)
    text_rect = text.get_rect(center=(width//2, 350))
    screen.blit(text, text_rect)

draw_lines()

player = 1
game_over = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            if mouseY < 300:  # Make sure clicks are within the board area
                clicked_row = mouseY // square_size
                clicked_col = mouseX // square_size

                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):
                        game_over = True
                        display_message(f"Player {player} wins!")
                    elif is_board_full():
                        game_over = True
                        display_message("It's a tie!")
                    else:
                        player = 3 - player  # Switch player
                        display_message(f"Player {player}'s turn")

                    draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False
                display_message(f"Player {player}'s turn")

    pygame.display.update()