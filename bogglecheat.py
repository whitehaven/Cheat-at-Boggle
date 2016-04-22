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
            self.empty_tracker = []
        else:
            self.board = board
            self.empty_tracker = [[False for i in range(len(self.board))] for j in range(len(self.board[0]))]

    def __repr__(self):
        repr_string = "BoggleBoard("
        repr_string += repr(self.board)
        repr_string += ")"

        return repr_string

    def solve_boggle(self, position ,lookup_dictionary, tracking_array):
        found_words = []

        # base case

        # checkup & continue

        """
        using tuples ( X , Y )
        Send execution to all possible directions
        (0,0) is center
        -1,1 | 0,1 | 1,1
        -1,0 | 0,0 | 1,0
        -1,-1| 0,-1| 1,-1
        """

        for possible_step in ():
        return found_words

if __name__ == "__main__":
    test_dictionary = {'babe'}
    testBoard_good = BoggleBoard([['b', 'a'], ['e', 'b']])
    testBoard_bad_dimensions = BoggleBoard([['b', 'a'], ['e', 'b','a']])

    test_found_words = testBoard_good.solve_boggle(test_dictionary)
    
    print("good test board:")
    print(testBoard_good)
    print('empty tracking array: ' + repr(testBoard_good.empty_tracker))
    
    print('\n' + "bad test board (non-rectangular dimensions):")
    print(testBoard_bad_dimensions)
