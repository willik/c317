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

    def copy(self):
        """ Make a copy of the variable """
        var_cp = Variable(self.domain)
        if self.current != None:
            var_cp.assign(self.current)
        return var_cp

class LatinSqState:
    """ Class for Latin Square states"""

    def __init__(self, variables, blanks):
        """ Represent the problem as a collection of Variables """

        self.vars = variables
        self.blanks = blanks


class LatinSqProblem:
    """ Class for Latin Square problems"""

    def __init__(self, square):
        """ Initialize the problem """
        self.square = square
        self.order = len(square)

    def create_initial_state(self):
        """ Creates a state from the square defined the problem """

        order = len(self.square)
        variables = {}
        blanks = []

        # convert the square into variables and assignments
        for row_num, row in enumerate(self.square):
            for col_num, entry in enumerate(row):

                # create the variable
                new_var = Variable(range(1, order + 1))

                # build list of identifiers of unassigned variables
                if entry == 0:
                    blanks.append((row_num, col_num))
                else:
                    new_var.assign(entry)

                # put the variable in the dict
                variables.update({(row_num, col_num): new_var})

        return LatinSqState(variables, blanks)

    def is_goal(self, state):
        """Checks if state is a true Latin Square."""

        # if there are blanks, it's not a state
        if len(state.blanks) > 0:
            return False

        # TESTING
            # print_sq = self.var_to_square(state)
            # if self.equal_sq(print_sq):
            #    break1 = 1
            # self.print_sq(print_sq)

        new_sq = []

        # Check rows, and construct a square without blanks
        for row_num, row in enumerate(self.square):

            row_cp = row.copy()


            # get the keys of the blanks in the current row
            row_blank_keys = []
            for col_num, entry in enumerate(row_cp):
                if entry == 0:
                    row_blank_keys.append((row_num, col_num))

            # For every blank key, update the new row with the corresponding variable assignment
            for key in row_blank_keys:

                # get the variable in the state with that key
                curr_var = state.vars.get(key)

                # get the assignment in that variable
                val = curr_var.current

                # get the column of the variable
                col = key[1]

                # fill in the blank in the copy of the row with the assignment in the variable
                row_cp[col] = val

            # do the actual check for latin squareness on this row
            # set() removes duplicates, so if the length changes, there are duplicates, and its not a latin square
            if len(row_cp) != len(set(row_cp)):
                return False

            # add the filled in row to the new square
            new_sq.append(row_cp)

        # check columns (we already constructed the filled in square, so just perform the check)
        for i in range(0, self.order):
            col = [row[i] for row in new_sq]  # construct column by grabbing i-th entry of each row
            if len(col) != len(set(col)):
                return False

        return True

    def actions(self, state):
        """ Creates a list of actions for state.
            An unassigned variable can be filled in with any number in the domain of the variable"""

        if len(state.blanks) == 0:
            return []

        # assume the blank is the first one in the list, and get the key
        first_bl_key = state.blanks[0]

        # get the variable at that key
        first_bl_var = state.vars.get(first_bl_key)

        # build list of actions, where an action is a tuple of the entry position and the integer to put there
        actions = []
        for i in first_bl_var.domain:
            actions.append((first_bl_key, i))

        return actions

    def result(self, state, action):
        """Creates a new State object with the blank filled in, as described in action."""

        # make copy of variables
        new_vars = {}
        new_blanks = []

        # copy vars, perform the action, and make new blanks
        for key, var in state.vars.items():

            var_cp = var.copy()

            if var.current == None:
                if key == action[0]:
                    # found the unassigned variable we want to perform the action on
                    var_cp.assign(action[1])
                else:
                    # didn't find the unassigned variable we want, so add to list of unassigned variables
                    new_blanks.append(key)

            # add the new variable
            new_vars.update({key: var_cp})

        # make the new state
        new_state = LatinSqState(new_vars, new_blanks)

        return new_state



    ########    Functions for Testing!    ########

    def var_to_square(self, state):
        """ converts state with variables to a square """

        # have: variables with position and value

        new_sq = []
        new_sq.append([])

        curr_row = 0

        for key, var in state.vars.items():

            if key[0] > curr_row:
                new_sq.append([])
                curr_row += 1

            new_sq[curr_row].append(var.current)

        return new_sq

    def print_sq(self, square):
        """ print a square """

        with open('test_out.txt', 'a') as myfile:

            myfile.write(str(self.order) + '\n')
            for row in square:
                for entry in row:
                    myfile.write(str(entry) + ' ')
                myfile.write('\n')
            myfile.write('\n')

    def equal_sq(self, square):
        """ check if the square is equal to the hard coded square """

        test_sq = []
        test_sq.append([1, 4, 2, 3])
        test_sq.append([4, 1, 3, 2])
        test_sq.append([3, 2, 1, 4])
        test_sq.append([2, 3, 4, 1])

        result = True

        for index, row in enumerate(square):
            if row != test_sq[index]:
                result = False

        return result