import itertools


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

    def solve_boggle(self, position, lookup_dictionary, tracking_array):
        """
        :param position: (i,j) positions
        :type position: tuple
        :param lookup_dictionary:
        :type lookup_dictionary: set
        :param tracking_array:
        :returns: found_words: list of strings
        """
        found_words = []

        # base case

        # checkup & continue

        """
        using tuples ( I , J )
        Send execution to all possible directions
        (0,0) is center
        -1,1 | 0,1 | 1,1
        -1,0 | 0,0 | 1,0
        -1,-1| 0,-1| 1,-1
        """
        possible_steps = itertools.product([-1, 0, 1], [-1, 0, 1])
        for step in possible_steps:
            proposed_i = step[0] + position[0]
            proposed_j = step[1] + position[1]
            # if not going to go out (i-wise) or (j-wise)
            #   and not previously visited on this snake-iteration
            if ((proposed_i < 0 or proposed_i > len(self.board[0])) or (
                            proposed_j < 0 or proposed_j > len(self.board))) and tracking_array[proposed_i][
                proposed_j] == False:
                tracking_array[proposed_i][proposed_j] = True
                self.solve_boggle((proposed_i, proposed_j), lookup_dictionary, tracking_array)
        return found_words


if __name__ == "__main__":
    test_dictionary = {'babe'}
    testBoard_good = BoggleBoard([['b', 'a'], ['e', 'b']])
    testBoard_bad_dimensions = BoggleBoard([['b', 'a'], ['e', 'b', 'a']])

    test_found_words = testBoard_good.solve_boggle(test_dictionary)

    print("good test board:")
    print(testBoard_good)
    print('empty tracking array: ' + repr(testBoard_good.empty_tracker))

    print('\n' + "bad test board (non-rectangular dimensions):")
    print(testBoard_bad_dimensions)
