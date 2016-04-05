class BoggleBoard:
    """
 Boggle Board
+-------------------+
|+---+   |  |  |  | |
||0,0|   |  |  |  | |
|+---+   |  |  |  | |
|                 m |
|-----              |
|                   |
|-----              |
|                   |
|-----n             |
+-------------------+
  > Any Size, even irregular
  > char
    """
    def __init__(self, board):
        """If board has non-rectangular dimensions, the board comes through blank."""
        try:
            for row in board:
                if len(row) != len(board[0]):
                    raise Exception('Non-rectangular dimensions')
        except Exception:
            self.board = []
        else:
            self.board = board

    def __repr__(self):
        repr_string = "BoggleBoard("
        repr_string += repr(self.board)
        repr_string += ")"

        return repr_string

    def solve_boggle(self, check_dictionary):
        found_words = []
        return found_words


if __name__ == "__main__":
    test_dictionary = {'babe'}
    testBoard_good = BoggleBoard([['b', 'a'], ['e', 'b']])
    testBoard_bad_dimensions = BoggleBoard([['b', 'a'], ['e', 'b','a']])
    test_found_words = testBoard.solve_boggle(test_dictionary)
    
    print("good test board:")
    print(testBoard_good)
    
    print("bad test board (non-rectangular dimensions)")
    print(testBoard_bad_dimensions)
