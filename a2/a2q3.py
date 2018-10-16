# Willis Kirkham
# 11084378
# wrk027
# C317 - a2q3

# Synopsis: implementing the Hill Climbing Search search strategy


def hill_climbing_search(problem, limit):
    """
    Starting from a random state
    Obtain the state’s best neighbour
    Move to it if it’s better than the current state
    Stop if no neighbour is better

    :param problem: the problem instance to run the search on
    :param limit: the number of guesses before returning
    :return: the best state obtained
    """

    best_guess = problem.random_state()
    count = 0
    while (count != limit):

        guess = problem.best_neighbour(best_guess)

        # calc the objective function and take the better state
        diff_guess = abs(problem.target - guess.register)
        diff_best = abs(problem.target - best_guess.register)
        if diff_guess < diff_best:
            best_guess = guess
        elif diff_guess > diff_best:
            return best_guess

        count += 1

    return best_guess
