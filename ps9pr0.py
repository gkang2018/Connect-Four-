# Problem Set 9, Problem 1 ---- ps9pr1

# A Connect Four Board Class

# Gagandeep Kang----- gskang@bu.edu

class Board:
    """a class that stores a Connect
        Four board
    """
    def __init__(self, height, width):
        """constructs a new Board object
            by initializing the following three attributes
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """returns a string representing a Board object.
        """
        s = ''         

        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'  
        for row in range((self.width*2 + 1)):
            s += "-"
        s += '\n'
        s += " "
        for col in range(self.width):
                if col < 9:
                    s += str(col)
                else:
                    s += str((col % 10))
                s += " "
        return s

   def add_checker(self, checker, col):
        """accepts two inputs: checker, a one-character string that specifies the checker to add to the board (either 'X' or 'O').
            col, an integer that specifies the index of the column to which the checker should be added and
            that adds checker to the appropriate row in column col of the board.
    
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        row = 0
        while self.slots[row][col] == " ":
            row += 1
            if row == self.height:
                self.slots[row][col] == checker
            elif 
            
        
