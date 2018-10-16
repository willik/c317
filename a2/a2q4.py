# Willis Kirkham
# 11084378
# wrk027
# C317 - a2q4

# Synopsis: implementing the Random Restart Hill Climbing Search search strategy

import a2.a2q3 as HCS


def random_restart_hill_climbing_search(problem, limit, restarts):
    """
    Repeatedly perform Hill Climbing Search

    :param problem: the problem instance to run the search on
    :param limit: the number of guesses in a hill climbing search before restarting or returning
    :param restarts: the number of times to restart the hill climbing search
    :return: the best state obtained
    """

    best_guess = problem.random_state()
    count = 0
    while (count != restarts):

        guess = HCS.hill_climbing_search(problem, limit)

        # calc the objective function and take the better state
        diff_guess = abs(problem.target - guess.register)
        diff_best = abs(problem.target - best_guess.register)
        if diff_guess < diff_best:
            best_guess = guess
        elif diff_guess > diff_best:
            return best_guess

        count += 1

    return best_guess
