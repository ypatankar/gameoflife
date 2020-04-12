import time
import sys
import os
import ast


class Grid:
    """
    A two-dimensional grid has i * j cells, each of which is in one of the two following states:
        1 corresponds to Alive
        0 correspondents to Dead

    Every cell interacts with its eight neighbors that are horizontal, vertical or diagonally adjacent.
    """

    def __init__(self, grid, rows, columns):
        """
        Constructor to initiate the grid
        """
        self.grid = grid
        self.rows = rows
        self.columns = columns

    def play_game(self):
        """
        This method updates the grid for a generation
        Rules: At each step in time, following rules are applied simultaneously to every cell:
            1. Any live cell with two or three live neighbors lives on to the next generation
            2. Any dead cell with exactly three live neighbors become a live cell
            3. All other cells die

        :param
            grid (list[list[int]]): a cell universe with a seed
        :return:
            None
        """
        for i in range(self.rows):
            for j in range(self.columns):
                cell = self.grid[i][j]

                neighbor_count = self.get_neighbor_count(i, j)

                """
                Transitions and intermediate states of cells in the grid:
                    live --> dead denoted by -1
                    dead --> live denoted by 2
                    live --> live keep cell state as is
                """
                if cell == 1 and neighbor_count not in (2, 3):
                    # if cell is alive and does not have 2 or 3 neighbors, then it dies by under-population/overcrowding
                    self.grid[i][j] = -1
                elif cell == 0 and neighbor_count == 3:
                    # if cell is dead and has 3 neighbors, then it becomes a live cell as if by reproduction
                    self.grid[i][j] = 2

        # Generalize state of grid cells to alive(1) or dead(0) based on values of intermediate state
        for i in range(self.rows):
            for j in range(self.columns):
                # if the cell is greater than 0, then mark is as alive else dead
                if self.grid[i][j] > 0:
                    self.grid[i][j] = 1
                else:
                    self.grid[i][j] = 0

    def get_neighbor_count(self, i, j):
        """
        An utility method to get neighbor count of a cell
        :param
            grid (list[list[int]]): input cell universe
            i (int): row co-ordinate of the current cell
            j (int): column co-ordinate of the current cell
        :return
            n_count (int): neighbor count of a cell
        """
        n_count = 0

        # relative co-ordinates for the 8 neighbors of a cell
        relative_coordinates = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        # Using the relative coordinates, calculate real coordinates of a cell's neighbors in the grid
        for rel_i, rel_j in relative_coordinates:
            neigh_i = i + rel_i
            neigh_j = j + rel_j

            # Ensure that the neighbor is within grid
            if 0 <= neigh_i < self.rows and 0 <= neigh_j < self.columns:
                if abs(self.grid[neigh_i][neigh_j]) == 1:
                    # Since we are temporarily marking live --> dead transition as -1, need to perform abs() operation
                    # in order to count the neighbors that were previously alive in this generation
                    n_count += 1

        return n_count

    def create_generations(self, curr_n, n):
        """
        Create next generations of the grid based on the intermediary state of the grid and input count provided by user
        :param
            curr_n (int): generations to move forward based on user input
            n (int): total generations count
        :return:
            None
        """

        for i in range(1, curr_n+1):
            # call play_game() method for updating the grid for each generation
            self.play_game()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("{} generations(s): ".format(n + i - curr_n))
            print()
            formatted_grid = '\n'.join('  '.join('{}'.format(item) for item in row) for row in self.grid)
            sys.stdout.write("\r" + formatted_grid)
            time.sleep(0.4)
            sys.stdout.flush()


if __name__ == '__main__':

    """
    # Code for grid input at real time
    user_input_grid = input('Enter grid with seed :')
    input_grid = ast.literal_eval(user_input_grid)
    """
    # default input grid of 25*25 with seed at center
    input_grid = [[0 for c in range(25)] for r in range(25)]
    input_grid[11][12], input_grid[12][13] = 1, 1
    input_grid[13][11], input_grid[13][12], input_grid[13][13] = 1, 1, 1

    if not input_grid:
        exit()

    os.system('cls' if os.name == 'nt' else 'clear')
    print("This is the input grid:")
    print('\n'.join('  '.join('{}'.format(item) for item in row) for row in input_grid))

    # get the dimensions of the grid
    r = len(input_grid)
    c = len(input_grid[0])

    # instantiate Grid
    game_of_life = Grid(input_grid, r, c)

    # total count of generations
    gen_count = 0
    user_input = ''

    while user_input != 'q':
        print('\n')
        # get user input for the number of generations to be created
        user_input = input("Enter the number of generation(s) to create from this state onwards or 'q' to quit: ")

        if user_input == 'q':
            break
        else:
            try:
                # check if the input is valid
                input_count = int(user_input)
            except ValueError:
                print("Invalid input")
                continue
            else:
                # increment the total generations count
                gen_count += input_count
                # call the create_generations() method
                game_of_life.create_generations(input_count, gen_count)
