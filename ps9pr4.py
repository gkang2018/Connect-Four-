#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """creates AI Player class that takes the approach outlined above
        (and in more detail below) to choose its next move.
    """
    def __init__(self, checker, tiebreak, lookahead):
        """constructs a new AIPlayer object."""

        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)

        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """returns a string representing an AIPlayer object"""
        s = "Player" + " " + self.checker
        s += " " + "(" + self.tiebreak + "," + " " + str(self.lookahead) + ")" 
        return s 

    def max_score_column(self, scores):
        """takes a list scores containing a score for each column of the board,
            and that returns the index of the column with the maximum score.
        """
        max_number = max(scores)
        index_list = []
        for num in range(len(scores)):
            if scores[num] == max_number:
                index_list += [num]
        if self.tiebreak == "LEFT":
            final_index = index_list[0]
        elif self.tiebreak == "RIGHT":
            final_index = index_list[-1]
        else:
            final_index = random.choice(index_list)
        return final_index

    def scores_for(self, board):
        """takes a Board object board and
            determines the called AIPlayer‘s scores for the columns in board.
        """
        scores = board.width * [50]
        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1
            elif board.is_win_for(self.checker) == True:
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                new_AI = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = new_AI.scores_for(board)
                opp_scores_max = max(opp_scores)

                if opp_scores_max == 100:
                    scores[col] = 0
                elif opp_scores_max == 0:
                    scores[col] = 100
                elif opp_scores_max == 50:
                    scores[col] = 50

                board.remove_checker(col)
        return scores
    
    def next_move(self, board):
        """ should return the called AIPlayer‘s judgment of its best possible move.
        """
        score_list = self.scores_for(board)
        AI_judgement = self.max_score_column(score_list)
        self.num_moves += 1
        return AI_judgement
        
            
    

