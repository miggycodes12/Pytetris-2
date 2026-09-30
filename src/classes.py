
import pygame
import math


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

    def draw_board(self, screen: pygame.Surface, offset_x=0, offset_y=0):

        self.offset_x = offset_x
        self.offset_y = offset_y

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (offset_x, offset_y, self.width * self.scale, self.height * self.scale),
            1
        )

    def render_cells(self, screen: pygame.Surface):
        if self.offset_x is None or self.offset_y is None:
            raise Exception("Board must be drawn with draw_board() before rendering cells.")
    
        for row in self.grid:
            for cell in row:

                if cell:
                    pygame.draw.rect(
                        screen,
                        cell["color"],
                        (
                            self.offset_x + row.index(cell) * self.scale,
                            self.offset_y + self.grid.index(row) * self.scale,
                            self.scale,
                            self.scale
                        )
                    )

    def search_active_cells(self):
        '''
        Searches through self.grid and provides a list containing tuple ordered pairs that are the active cells (1) positions on the grid.
        The order of the ordered pairs is guranteed and searches top to bottom.
        '''

        ordered_pairs = []
        full_empty_row = [0] * self.width

        for row in self.grid:

            if row == full_empty_row:
                continue

            for cell in row:
                if cell != 1:
                    pair = (
                        row.index(cell),
                        self.grid.index(row)
                    )

                    ordered_pairs.append(pair)

        return ordered_pairs

    def add_cell(self, cell: Cell, x: int, y: int, update=False):
        '''
        @param cell: A cell class object containing the information of the cell to be added
        @param x: The x position of the cell to be added
        @param y: The y position of the cell to be added
        @param update: A boolean that should updates an existing cell with the given cell object
        '''

        cell = self.grid[y][x]

        # will be used for game overs soon
        if cell != {} and not update:
            return "override"

        if update and cell == {}:
            print("Warning: updating an empty cell. defaults to adding to it.")

        try:
            self.grid[y][x] = {
                "color": cell.color,
                "state_id": cell.state_id
            }
        except IndexError:
            print(f"Error: Cell position ({x}, {y}) is out of bounds.")
            print(f"Grid size: {self.width}x{self.height}")


    def spawn_tetromino(self, tetromino: Tetromino):

        if self.current_tetromino != None:
            raise Exception("You cannot call spawn_tetromino() while there is an active tetromino.")

        self.current_tetromino = tetromino
        middle_x = math.floor(self.width / 2)

        # remember: the shape is a 2d list

        shape = tetromino.shape
        color = tetromino.color
        for row in shape:
            middle_offset = 0
            for cell_state in row:

                if cell_state != 0:
                    new_cell = Cell(color, 1)
                    self.add_cell(new_cell, middle_x + middle_offset, shape.index(row))

                middle_offset += 1

    def check_piece_locking(self):
        '''
        For the current tetromino, it checks every cell that has an empty cell below if there is a locked (2) cell or the bottom of the board beneath it.
        If any of these cells fulfill this condition upon this function call, the entire tetromino is locked.
        '''

        if self.current_tetromino == None:
            return

        active_cells = self.search_active_cells()

        def lock(active_cells):
            for pair in active_cells:
                x, y = pair[0], pair[1]
                old_cell = self.grid[y][x]
                color = old_cell["color"]

                new_cell = Cell(color, 2)
                self.add_cell(new_cell, x, y, True)

            self.current_tetromino = None
                

        for pair in active_cells:
            x = pair[0]
            y = pair[1]

            # checks if the cell is at the bottom of the board
            # subtracts self.width by 1 because y is in 0-indexing
            if y+1 > self.width - 1:
                lock(active_cells)
                return

            cell_below = self.grid[y+1][x]

            if cell_below != {}:
                continue

            if cell_below["state_id"] == 2:
                lock(active_cells)
                return

            
    #TODO: gravity


    def print_board(self):
        for row in self.grid:
            print(row)
