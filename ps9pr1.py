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
            if (row + 1) == self.height:
                break
            if self.slots[row+1][col] == "X" or self.slots[row+1][col] == "O":
                break
            row += 1
            
        self.slots[row][col] = checker   
      
    def reset(self):
        """should reset the Board object on which it is called
            by setting all slots to contain a space character.
        """
        for r in range(self.height):
            for c in range(self.width):
                self.slots[r][c] = " "
    
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'              
            
        
    def can_add_to(self, col):
        """returns True if it is valid to place a checker in the column col on the calling Board object.
            otherwise, it should return False."""

        if col > (self.width - 1) or col < 0:
            return False
        elif self.slots[0][col] == "X" or self.slots[0][col] == "O":
            return False
        else:
            return True
    
    def is_full(self):
        """returns True if the called Board object is completely full of checkers,
            and returns False otherwise.
        """
        for row in range(self.height):
            for col in range(self.width):
                check_full = self.can_add_to(col)
                if check_full== True:
                    return False
        return True 
        
    def remove_checker(self,col):
        """removes the top checker from column col of the called Board object.
            If the column is empty, then the method should do nothing."""

        for row in range(self.height):
            if self.slots[row][col] == "X" or self.slots[row][col] == "O":
                self.slots[row][col] = " "
                break

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker."""
        for row in range(self.height - 3):
            for col in range(self.height):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """ Check for diagonal (left to right downwards) win for the specified checker"""
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col +1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False
    
    def is_up_diagonal_win(self, checker):
        """ Check for diagonal (left to right upwards) win for the specified checker"""
        
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        return False
              

    def is_win_for(self, checker):
        """accepts a parameter checker that is either 'X' or 'O',
            and returns True if there are four consecutive slots containing checker on the board.
            Otherwise, it should return False.
        """
        assert(checker == 'X' or checker == 'O')

        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False
        
        
        
            
        
