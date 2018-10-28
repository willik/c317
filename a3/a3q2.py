# Willis Kirkham
# 11084378
# wrk027
# C317 - a2q6

# Synopsis:


class Variable:
    """ A representation of a variable, which has a domain and a current value that is assigned or unassigned """

    def __init__(self, domain):
        """ Initialize the variable """

        self.current = None
        self.domain = domain

    def assign(self, value):
        """ Assign the variable a value, which also means the domain becomes empty """

        self.current = value
        self.domain = []


class LatinSqState:

    def __init__(self, square):
        """ Represent the problem as a collection of Variables """

        self.order = len(square)
        self.vars = {}
        self.blanks = []

        # convert the square into variables and assignments
        for row_num, row in enumerate(square):
            for col_num, entry in enumerate(row):

                # create the variable
                new_var = Variable(range(1, self.order + 1))
                new_var.assign(entry)

                # build list of identifiers of unassigned variables
                if entry == 0:
                    self.blanks.append((row_num, col_num))

                # put the variable in the dict
                self.vars.update({(row_num, col_num): new_var})


class LatinSqProblem:

    def __init__(self):
        self.test = 0

    def create_initial_state(self, square):

        # convert the square into variables and assignments
        for row_num, row in enumerate(square):
            for col_num, entry in enumerate(row):

                # create the variable
                new_var = Variable(range(1, self.order + 1))
                new_var.assign(entry)

                # build list of identifiers of unassigned variables
                if entry == 0:
                    self.blanks.append((row_num, col_num))

                # put the variable in the dict
                self.vars.update({(row_num, col_num): new_var})

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
        """Creates a new State object with the blank filled in, as described in
           action."""

        # make copy of
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
