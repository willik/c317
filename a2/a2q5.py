# Willis Kirkham
# 11084378
# wrk027
# C317 - a2q5

# Synopsis: implementing the Stochastic Hill Climbing Search search strategy


def stochastic_hill_climbing_search(problem, limit):
    """
    Perform Hill-Climbing Search, expanding the search based on a random neighbour that is better
    than the current state
    :param problem: the problem instance to run the search on
    :param limit: the number of guesses in a hill climbing search before restarting or returning
    :return: the best state obtained
    """

    best_guess = problem.random_state()
    count = 0
    while (count != limit):

        guess = problem.random_better_neighbour(best_guess)

        # if there were no better
        if guess == None:
            return best_guess

        # if we got a new guess, it will always be better, so don't check that its better
        best_guess = guess

        count += 1

    return best_guess
