# Willis Kirkham
# 11084378
# wrk027
# C317 - a2q6

# Synopsis:


class State:

    def __init__(self):
        """Represent the problem naively, as a 2-dimensional list (or array) of integers (the blank in thefile
           could be stored as a zero). You could add a list of blank locations by giving the row and column as
           integer pairs (e.g., (2, 3) ). This would help speed up some of the other functions"""

        #

        # list of blank locations


class Problem:

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