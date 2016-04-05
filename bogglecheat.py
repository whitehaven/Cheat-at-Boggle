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
        try:
            for row in board:
                if len(row) != len(board[0]):
                    raise Exception('Non-rectangular dimensions')
        except Exception:
            print('Non-rectangular dimensions')
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
    testBoard = BoggleBoard([['b', 'a'], ['e', 'b','a']])
    test_found_words = testBoard.solve_boggle(test_dictionary)
    print(testBoard)
