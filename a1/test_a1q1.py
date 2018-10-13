# Willis Kirkham
# 11084378
# wrk027
# C317 - a1

# Synopsis: a class for describing the problem state

from a1.a1q1 import *
from a1.a1q1 import InvArithProblem

def main():

    # Test the problem state class
    test_state = InvArithState("(4+1)")
    if test_state.result != 5:
        print('InvArithState does not set target properly')

    # Test the problem class
    numbers = ['1', '2', '3', '4', '5', '6']
    test_problem = InvArithProblem(5, numbers)

    # is_goal() with matching targets
    if test_problem.is_goal(test_state) != True:
        print('InvArithState does not set target properly')

    # is_goal() with non-matching targets
    test_state = InvArithState("(6+4)")
    if test_problem.is_goal(test_state) != False:
        print('InvArithState does not set target properly')

    # The following were verified with print statements
    actions = test_problem.actions(test_state)
    # print(actions)
    new_states = []
    for action in actions:
        new_states.append(test_problem.result(test_state, action))

    # for state in new_states:
    #     print(state)

    print('Tests complete')


if __name__ == "__main__":
    main()