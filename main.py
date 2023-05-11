import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 60)

# icon
icon = pygame.image.load("ttt-icon.png")
pygame.display.set_icon(icon)
# title
pygame.display.set_caption("Tic Tac Toe")
running = True

# fill the screen with white
screen.fill("white")

turn = "X"

# initialize the board
board = [["" for _ in range(3)] for _ in range(3)]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row, col = get_square(mouse_x, mouse_y)
            if board[row][col] == "":
                if turn == "X":
                    draw_x(row, col)
                    board[row][col] = "X"
                    turn = "O"
                elif turn == "O":
                    draw_o(row, col)
                    board[row][col] = "O"
                    turn = "X"

    # RENDER YOUR GAME HERE
    # draw a tic tac toe board
    pygame.draw.line(screen, "black", (200, 0), (200, 600), 5)
    pygame.draw.line(screen, "black", (400, 0), (400, 600), 5)
    pygame.draw.line(screen, "black", (0, 200), (600, 200), 5)
    pygame.draw.line(screen, "black", (0, 400), (600, 400), 5)

    def get_square(mouse_x, mouse_y):
        if mouse_x < 200:
            col = 0
        elif mouse_x < 400:
            col = 1
        else:
            col = 2

        if mouse_y < 200:
            row = 0
        elif mouse_y < 400:
            row = 1
        else:
            row = 2

        return row, col

    def draw_x(row, col):
        pygame.draw.line(
            screen,
            "red",
            (col * 200, row * 200),
            (col * 200 + 200, row * 200 + 200),
            5,
        )
        pygame.draw.line(
            screen,
            "red",
            (col * 200, row * 200 + 200),
            (col * 200 + 200, row * 200),
            5,
        )

    def draw_o(row, col):
        pygame.draw.circle(screen, "blue", (col * 200 + 100, row * 200 + 100), 100, 5)

    def check_win():
        # Check rows

        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] and board[row][0] != "":
                return board[row][0]

        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
                return board[0][col]

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
            return board[0][0]

        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
            return board[0][2]

        return None

    winner = check_win()
    if winner:
        text = font.render(f"{winner} wins!", True, "black")
        screen.blit(text, (200, 300))

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
