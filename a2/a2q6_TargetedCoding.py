# Willis Kirkham
# 11084378
# wrk027
# C317 - a2

# Synopsis: - a class for describing the problem state
#           - a class for describing the problem

import random


class TargetedCodingState:
    """ A data structure to describe a state in the problem space """

    def __init__(self, problem, operators):
        """
        Creates a new state
        """
        self.operators = operators
        self.register = problem.machine_exec(operators)

    def __str__(self):

        return 'register: ' + str(self.register) + '\noperators: ' + str(self.operators)


class TargetedCodingProblem:
    """A data structure to describe the problem"""

    def __init__(self, target, operands):
        """
        Creates a new Problem instance
        """
        self.target = target
        self.operands = operands
        self.operators = [1, 2, 3, 4, 5]

    def random_state(self):
        """

        :return:
        """
        operators = []
        for x in self.operands:
            operators.append(random.randint(1, 5))
        return TargetedCodingState(self, operators)

    def random_neighbour(self, state):
        """

        :param state:
        :return:
        """

        operators = state.operators

        # get a random position to change
        pos = random.randint(0, len(operators) - 1)

        # put a random operator in that position
        operators[pos] = random.randint(1,5)

        return TargetedCodingState(self, operators)

    def best_neighbour(self, state):
        """
        Gets the best neighbour of state
        :param state: the state to get the best neighbour of
        :return: the bestneighbour if there is one, or the first neighbour if there isn't
        """

        neighbours = self.neighbours(state)

        # iterate the neighbours, always keeping the best neighbour
        best = neighbours[0]
        for guess in neighbours[1:]:
            # calc the objective function and take the better state
            diff_guess = abs(self.target - guess.register)
            diff_best = abs(self.target - best.register)
            if diff_guess < diff_best:
                best = guess

        return best

    def random_better_neighbour(self, state):
        """

        :param state:
        :return:
        """
        neighbours = self.neighbours(state)

        diff_state = abs(self.target - state.register)
        better = []

        # construct a list of all better neighbours
        for curr in neighbours:
            # calc the objective function and determine the better state
            diff_neighbour = abs(self.target - curr.register)
            if diff_neighbour < diff_state:
                better.append(curr)

        # when there are no better neighbours, return none
        if len(better) == 0:
            return None

        # return a randomly chosen better neighbour
        return random.choice(better)


    def neighbours(self, state):
        """
        Helper function to get all neighbours of a state
        :param state: the state to get the neighbours of
        :return: list of the neighbours
        """

        neighbours = []
        new_operators = []

        # iterate the list of current operators
        for index, operand in enumerate(state.operators):
            # get a new list of all operators except the current operator
            neighbour_operators = [item for item in self.operators if item != operand]

            # Make a neighbour for every unused operator, and add it to a list
            for curr in neighbour_operators:
                new_operators = state.operators.copy()
                new_operators[index] = curr
                neighbours.append(TargetedCodingState(self, new_operators))

        return neighbours

    def is_goal(self, candidate):
        """

        :return:
        """
        if self.target == candidate.register:
            return True
        else:
            return False

    def machine_exec(self, operators):
        """

        :param operators:
        :return:
        """

        # 1 = add
        # 2 = sub
        # 3 = mul
        # 4 = div
        # 5 = NOP

        register = 0

        for index, operator in enumerate(operators):

            if operator == 1:
                register += self.operands[index]
            elif operator == 2:
                register -= self.operands[index]
            elif operator == 3:
                register *= self.operands[index]
            elif operator == 4:
                register = register / self.operands[index]
            elif operator == 5:
                pass
            else:
                print('unknown operator', operator)

        return register

    class SearchResult(object):
        """A data structure to return information about how the search turned out."""

        def __init__(self, result, time=0):
            self.result = result  # the state returned by the search function
            self.time = time  # float: how much time was spent searching?

        def __str__(self):
            """Make a nice mess"""
            text = ''
            if self.success:
                text += 'Search successful'
            else:
                text += 'Search failed'
            text += ' (' + str(self.time) + ' sec, ' + str(self.nodes) + ' nodes, ' + str(self.space) + ' queue)'
            return text







