# -*- coding: utf-8 -*-

# Willis Kirkham
# 11084378
# wrk027
# C317 - a2q6

# Synopsis:

import time as time

def random_guessing (problem, limit):
    """ Keep generating random states, remember the best one
    :param problem: the problem instance to run the search on
    :param limit: the number of states to generate before returning
    :return: the best guess obtained
    """
    start_time = time.time()
    now = start_time

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

    now = time.time()
    return problem.SearchResult(result=best_guess, time=now - start_time)


def random_search(problem, limit):
    """
    Randomly generate successors from the current state
    Move to it if it’s better than the current state
    :param problem: the problem instance to run the search on
    :param limit: the number of states to generate before returning
    :return: the best guess obtained
    """

    start_time = time.time()
    now = start_time

    best_guess = problem.random_state()
    count = 0

    while (count != limit):

        guess = problem.random_neighbour(best_guess)

        # calc the objective function and take the better state
        diff_guess = abs(problem.target - guess.register)
        diff_best = abs(problem.target - best_guess.register)
        if diff_guess < diff_best:
            best_guess = guess

        count += 1

    now = time.time()
    return problem.SearchResult(result=best_guess, time=now - start_time)


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

    start_time = time.time()
    now = start_time

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
            now = time.time()
            return problem.SearchResult(result=best_guess, time=now - start_time)

        count += 1

    now = time.time()
    return problem.SearchResult(result=best_guess, time=now - start_time)


def random_restart_hill_climbing_search(problem, limit, restarts):
    """
    Repeatedly perform Hill Climbing Search

    :param problem: the problem instance to run the search on
    :param limit: the number of guesses in a hill climbing search before restarting or returning
    :param restarts: the number of times to restart the hill climbing search
    :return: the best state obtained
    """

    start_time = time.time()
    now = start_time

    best_guess = problem.SearchResult(result=problem.random_state(), time=now)
    count = 0
    while (count != restarts):

        guess = hill_climbing_search(problem, limit)

        # calc the objective function and take the better state
        diff_guess = abs(problem.target - guess.result.register)
        diff_best = abs(problem.target - best_guess.result.register)
        if diff_guess < diff_best:
            best_guess = guess
        elif diff_guess > diff_best:
            now = time.time()
            return problem.SearchResult(result=best_guess.result, time=now - start_time)

        count += 1

    now = time.time()
    return problem.SearchResult(result=best_guess.result, time=now - start_time)


def stochastic_hill_climbing_search(problem, limit):
    """
    Perform Hill-Climbing Search, expanding the search based on a random neighbour that is better
    than the current state
    :param problem: the problem instance to run the search on
    :param limit: the number of guesses in a hill climbing search before restarting or returning
    :return: the best state obtained
    """

    start_time = time.time()
    now = start_time

    best_guess = problem.random_state()
    count = 0
    while (count != limit):

        guess = problem.random_better_neighbour(best_guess)

        # if there were no better
        if guess == None:
            now = time.time()
            return problem.SearchResult(result=best_guess, time=now - start_time)

        # if we got a new guess, it will always be better, so don't check that its better
        best_guess = guess

        count += 1

    now = time.time()
    return problem.SearchResult(result=best_guess, time=now - start_time)
