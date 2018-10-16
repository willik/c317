# Willis Kirkham
# 11084378
# wrk027
# C317 - a2q1

# Synopsis: implementing the Random Guessing search strategy


def random_guessing (problem, limit):
    """ Keep generating random states, remember the best one
    :param problem: the problem instance to run the search on
    :param limit: the number of states to generate before returning
    :return: the best guess obtained
    """

    best_guess = problem.random_state()
    count = 0

    while (count != limit):

        guess = problem.random_state()

        # calc the objective function and take the better state
        diff_guess = abs(problem.target - guess.register)
        diff_best = abs(problem.target - best_guess.register)
        if diff_guess < diff_best:
            best_guess = guess

        count += 1

    return best_guess
