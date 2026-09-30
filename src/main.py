
import pygame
import classes

def main():

    FPS = 60 # gravity is dependent on this value so keep it at 60
    TETROMINO_SHAPES = {
        "T_PIECE": {
            "rotation_1": [
                [1, 1, 1],
                [0, 1, 0]
            ],

            "rotation_2": [
                [0, 1],
                [1, 1],
                [0, 1]
            ],

            "rotation_3": [
                [0, 1, 0],
                [1, 1, 1]
            ],

            "rotation_4": [
                [1, 0],
                [1, 1],
                [1, 0]
            ]
        },

        "J_PIECE": {
            "rotation_1": [
                [0, 1],
                [0, 1],
                [1, 1]
            ],

            "rotation_2": [
                [1, 0, 0],
                [1, 1, 1]
            ],

            "rotation_3": [
                [1, 1],
                [1, 0],
                [1, 0]
            ],

            "rotation_4": [
                [1, 1, 1],
                [0, 0, 1]
            ]
        },

        "L_PIECE": {
            "rotation_1": [
                [1, 0],
                [1, 0],
                [1, 1]
            ],

            "rotation_2": [
                [1, 1, 1],
                [1, 0, 0]
            ],

            "rotation_3": [
                [1, 1],
                [0, 1],
                [0, 1]
            ],

            "rotation_4": [
                [0, 0, 1],
                [1, 1, 1]
            ]
        },

        "S_PIECE": {
            "rotation_1": [
                [0, 1, 1],
                [1, 1, 0]
            ],

            "rotation_2": [
                [1, 0],
                [1, 1],
                [0, 1]
            ]
        },

        "Z_PIECE": {
            "rotation_1": [
                [1, 1, 0],
                [0, 1, 1]
            ],

            "rotation_2": [
                [0, 1],
                [1, 1],
                [1, 0]
            ]
        },

        "I_PIECE": {
            "rotation_1": [
                [1, 1, 1, 1]
            ],

            "rotation_2": [
                [1],
                [1],
                [1],
                [1]
            ]
        },

        "O_PIECE": {
            "rotation_1": [
                [1, 1],
                [1, 1]
            ]
        }

    }

    new_board = classes.Board(10, 20, 45) # Standard NES Tetris uses 10x20 grid

    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Pytetris 2")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        new_board.draw_board(screen, offset_x=350)
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()