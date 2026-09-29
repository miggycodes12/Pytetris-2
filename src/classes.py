
import pygame

class Helpers:
    pass

class Cell:
    def __init__(self, color: tuple[int, int, int], state_id):
        '''
        @param color: RGB tuple of the cell's color
        @state_id: The state of the cell. (0 = empty, 1 = filled, 2 = locked)
        '''

        self.color = color
        self.state_id = state_id

        if state_id == 0:
            self.color = (0, 0, 0)

class Tetromino:
    def __init__(self, shape: list, color: tuple[int, int, int]):
        '''
        @param shape: A 2D list representing the shape of the tetromino. Use 1 for filled cells and 0 for empty cells.
        @param color: RGB tuple of the tetromino's color
        '''

        self.shape = shape
        self.color = color

class Board:
    def __init__(self, width, height, scale):
        self.width = width
        self.height = height
        self.scale = scale

        self.grid = []

        for y in range(height):
            row = []
            for x in range(width):
                row.append({})

            self.grid.append(row)

    def draw_board(self, screen: pygame.Surface):
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (0, 0, self.width * self.scale, self.height * self.scale)
        )


    def add_cell(self, cell: Cell, x: int, y: int):
        '''
        @param cell: A cell class object containing the information of the cell to be added
        @param x: The x position of the cell to be added
        @param y: The y position of the cell to be added
        '''

        try:
            self.grid[y][x] = {
                "color": cell.color,
                "state_id": cell.state_id
            }
        except IndexError:
            print(f"Error: Cell position ({x}, {y}) is out of bounds.")
            print(f"Grid size: {self.width}x{self.height}")

    def spawn_tetromino(self, tetromino: Tetromino):
        pass

    def print_board(self):
        for row in self.grid:
            print(row)
