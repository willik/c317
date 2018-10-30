# Willis Kirkham
# 11084378
# wrk027
# C317 - a2q6

# Synopsis:


class LatinSqState:
    """ Class for Latin Square states"""

    def __init__(self, square):
        """Represent the problem naively, as a 2-dimensional list (or array) of integers"""

        self.square = square
        self.order = len(square)

        self.blanks = self.build_blanks()

    def build_blanks(self):
        """Create a list of blanks in a square.
           Row and column as integer pairs (e.g., (2, 3)"""

        blanks = []
        for row_num, row in enumerate(self.square):
            for col_num, entry in enumerate(row):
                if entry == 0:
                    blanks.append((row_num, col_num))

        return blanks


class LatinSqProblem:
    """ Class for Latin Square problems"""

    def is_goal(self, state):
        """Checks if state is a true Latin Square."""

        # if there are blanks, it's not a state
        if len(state.blanks) > 0:
            return False

        # check rows
        for row in state.square:
            # set() removes duplicates, so if the length changes, there are duplicates, and its not a latin square
            if len(row) != len(set(row)):
                return False

        # check columns
        for i in range(0, state.order):
            col = [row[i] for row in state.square]  # construct column by grabbing i-th entry of each row
            if len(col) != len(set(col)):
                return False

        return True

    def actions(self, state):
        """A blank can be filled in with any number 1, . . . , N."""

        if len(state.blanks) == 0:
            return []

        # specify the blank or assume its the first one in list of blanks
        first = state.blanks[0]

        # build list of actions, where an action is a tuple of the entry position and the integer to put there
        actions = []
        for i in range(1, state.order + 1):
            actions.append((first, i))

        return actions

    def result(self, state, action):
        """Creates a new State object with the blank filled in, as described in action."""

        # make copy of list array
        square_cp = []
        for row in state.square:
            square_cp.append(row.copy())

        # change the copy
        row = action[0][0]
        col = action[0][1]
        num = action[1]
        square_cp[row][col] = num

        # make the new state
        new_state = LatinSqState(square_cp)

        return new_state
