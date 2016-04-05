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
        self.board = board

    def __repr__(self):
        repr_string = "BoggleBoard(\n"
        for lines in self.board:
            repr_string += str(lines) + "\n"
        repr_string += ")"

        return repr_string

    def solve_boggle(self, check_dictionary):
        found_words = []
        return found_words


if __name__ == "__main__":
    test_dictionary = {'babe'}
    testBoard = BoggleBoard([['b', 'a'], ['e', 'b']])
    test_found_words = testBoard.solve_boggle(test_dictionary)
    print(testBoard)
