from random import randrange

def add_pairs(a, b):
    """ Returns the component-wise sum of two pairs """
    return (a[0] + b[0], a[1] + b[1])

class Grid:
    """ Zero-indexed grid with col, row coordinates """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._arrays = []
        for i in range(height):
            self._arrays.append([0 for j in range(width)])

    def on_board(self, pos):
        col, row  = pos
        return col >= 0 and col < self.width and row >= 0 and row < self.height
    
    def get(self, pos):
        col, row = pos
        return self._arrays[col][row]
    
    def set(self, pos, value):
        col, row = pos
        self._arrays[col][row] = value

    def neighbours(self, pos):
        """Returns a list of pairs representing the coordinates of the
        neighbouring squares"""

        offsets = [
                (-1, -1), (0, -1), (1, -1),
                (-1,  0),          (1,  0),
                (-1,  1), (0,  1), (1,  1)]

        potential_neighbours = [add_pairs(offset, pos) for offset in offsets]
        neighbours = filter(self.on_board, potential_neighbours)

        return neighbours

class Mindsweaper:
    def __init__(self, width = 16, height = 16, bombs = 32):
        assert(bombs <= width * height)
        self.width = width
        self.height = height
        self._bombs = Grid(width, height)

        # Randomly place bombs
        set_bombs = 0
        while set_bombs < bombs:
            col, row = randrange(0, width), randrange(0, height)
            if self._bombs.get((col, row)) == False:
                self._bombs.set((col, row), True)
                set_bombs+=1

        self._explored = Grid(width, height)

    def _bomb_count(self, pos):
        """ Returns the number of adj. bombs to the position """
        return sum([self._bombs.get(neighbour) for neighbour in self._bombs.neighbours(pos)])

  
    def explore(self, pos):
        """ If adj. a bomb, uncover the number. If on a bomb, uncover the bomb
        and mark death.  Otherwise in-paint all squares not adj. a bomb """

        # mark as explored regardless of what's here
        self._explored.set(pos, True)
        if self._bombs.get(pos):
            return # we'll be dead soon
        if self._bomb_count(pos) > 0:
            return # stop exploring
        # explore all unexplored neighbours since we have no adj. bombs
        [self.explore(n) for n in self._explored.neighbours(pos) if not self._explored.get(n)]

    def won(self):
        """ Returns true if everything except for the bombs has been explored """
        for row in range(self.height):
            for col in range(self.width):
                pos = (col, row)
                if not self._bombs.get(pos) and not self._explored.get(pos):
                    return False
        return True

    def lost(self):
        """ Returns true if a bomb is uncovered """
        for row in range(self.height):
            for col in range(self.width):
                pos = (col, row)
                if self._bombs.get(pos) and self._explored.get(pos):
                    return True
        return False


    # UI
    def prompt_position(self):
        while True:
            print("Please enter a col and row separated by a comma, if you dare!")
            try:
                col_str, row_str = input().split(',')
                pos = (int(col_str), int(row_str)) 
                if not self._explored.on_board(pos):
                    print("Invalid position")
                elif self._explored.get(pos):
                    print("You've already explored there")
                else:
                    return pos

            except ValueError:
                print("Invalid format")

    def _symbol(self, pos):
        if self._explored.get(pos):
            if(self._bombs.get(pos)):
                return '*' # we're dead, but draw it anyways
            return self._bomb_count(pos) # uncovered next to bomb
        return '?' # not yet explored

    def draw(self):
        for row in range(self.height):
            for col in range(self.width):
                print(self._symbol((col, row)), end='')
            print('\n', end='')

    # Game loop
    def run(self):
        self.draw()
        while True:
            self.explore(self.prompt_position())
            self.draw()

            if self.lost():
                print("Game Over... you lost!")
                return

            if self.won():
                print("Game Over... you won!")
                return

            # else keep playing

        
game = Mindsweaper()
game.run()
