# Willis Kirkham
# 11084378
# wrk027
# C317 - a2q6

# Synopsis:


class LatinSqState:

    def __init__(self, square):
        """Represent the problem naively, as a 2-dimensional list (or array) of integers"""

        self.square = square

        #self.blanks = build_blanks()

    # def build_blanks(self, square):
    #     """Create a list of blanks in a square. row and column as
    #        integer pairs (e.g., (2, 3)"""
    #
    #     for row, item in enumerate(square)
    #         for col, item in enumerate(square)





class LatinSqProblem:

    def __init__(self):


    def is_goal(self, state):
        """Checks if state is a true Latin Square."""

        # if we encounter a blank at any time, it's not a latin square

    def actions(self, state):
        """A blank can be filled in with any number 1, . . . , N."""

        # specify the blank or assume its the first one in list of blanks


    def result(self, state, action):
        """Creates a new State object with the blank filled in, as described in
           action."""

        # make copy of list array

        # change the copy

        # make the new state

        return