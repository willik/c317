# Willis Kirkham
# 11084378
# wrk027
# C317 - a1

# Synopsis: - a class for describing the problem state
#           - a class for describing the problem


import re   # For evaluating regular expressions


class InvArithState:
    """A data structure to describe a state in the problem space"""

    def __init__(self, expression=None):
        """
        Creates a new state
        :param expression: the arithmetic expression as a string
        """
        # Handle the root case
        if expression == None:
            self.expression = 0
        # Handle the non root case
        else:
            self.expression = expression

        self.result = eval(self.expression)

    def __str__(self):
        return 'expression' + str(self.expression) + ':' + str(self.result)

class InvArithProblem:
    """A data structure to describe the problem"""

    def __init__(self, target, bank):
        """
        Creates a new Problem instance
        :param target: the integer the search is trying to build an expression for
        :param bank: the list of integers that can be used to create an expression
        """
        self.goal = target
        self.bank = bank

    def is_goal(self, state):
        """
        Checks if a state is a goal state
        :param state: a Problem State instance
        :return: boolean
        """

        if state.result != self.goal:
            return False
        else:
            return True


    def actions(self, state):
        """
        Produces a list of valid actions from a state
        :param state: a Problem State instance
        :return: returns a list of valid actions in the problem domain
        """
        # Extract a list of used numbers from the expression
        numbers = re.findall(r'\d+', state.expression)

        # Remove numbers already in the expression from the problem's bank of numbers
        numbers = list(set(self.bank) - set(numbers))

        # Create the list of actions
        actions = []
        for num in numbers:
            actions.append("+" + num)
            actions.append('-' + num)
            actions.append('*' + num)
            actions.append('//' + num)

        return actions

    def result(self, state, action):
        """
        Produces the new state that results from taking an action on an existing state
        :param state: the state to perform the action on
        :param action: an action as returned by actions(state)
        :return: new Problem State instance
        """
        return InvArithState('(' + state.expression + action + ')')