# Willis Kirkham
# 11084378
# wrk027
# C317 - a1

# Synopsis: a class for describing the problem state

class ProblemState:

    def __init__(self, value):
        self.result = value

    def display(self):
        print(self.result)

class Problem:

    def is_goal(state):
        """
        :param state: a Problem State instance
        :return: boolean
        """

    def actions(state):
        """
        :param state: a Problem State instance
        :return: returns a list of valid actions in the problem domain
        """

    def result(state, action):
        """
        :param state:
        :param action: an action as returned by actions(state)
        :return: new Problem State instance
        """

class SearchNode:

    def __init__(self, state, depth, action, parent, step_cost):
        """

        :param state: the Problem state
        :param depth: the depth of this node from the root
        :param action: the action that caused this state
        :param parent: the parent node
        :param step_cost: the path cost from root to this node
        """

