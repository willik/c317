# -*- coding: utf-8 -*-

# Willis Kirkham
# 11084378
# wrk027
# C317 - a1

import gc as gc
import sys as sys

import a3q1 as P1
import a3q2 as P2
import a3q3 as P3
import a3q4 as P4
import A1Search as A1Search


if len(sys.argv) < 5:
    print('usage: python a3_run examplefile question solver timelimit [depthlimit]')
    sys.exit()

file = open(sys.argv[1], 'r').readlines()
solver = sys.argv[3]
question = sys.argv[2]
timelimit = int(sys.argv[4])

if solver not in ['DFS', 'BFS', 'DLS', 'IDS']:
    print('solver', solver, 'not known')
    sys.exit()

if solver == 'DLS' and len(sys.argv) != 6:
    print('missing depthlimit for DLS (last arg)')
    sys.exit()

print(sys.argv)

examples = []

# Process the input file, create a list of squares
#quantity = int(file[0])
skip = 0
for index, item in enumerate(file[1:]):

    # skip the lines corresponding to the rows of squares, and the blank after the square
    if skip != 0:
        skip -= 1
        continue

    # get the size of the current latin square
    order = int(item)

    # construct the square
    square = []
    for curr in file[index+2:index+2+order]:
        row = curr.rstrip().split()
        # convert underscores to zeros, and all values to integers
        row = [0 if x == '_' else int(x) for x in row]
        square.append(row)

    # add square to list of squares
    examples.append(square)

    # skip the rows of the recently processed square, plus the following blank line
    skip = order + 1

total_time = 0;
sum_err_sq = 0;

num_completed = 0
num_failed = 0

print('reached loop')

for ex in examples:

    gc.collect()  # clean up any allocated memory now, before we start timing stuff

    # ['DFS', 'BFS', 'DLS', 'IDS']:

    if question == 'a3q1':

        if solver == 'DFS':
            problem = P1.LatinSqProblem()
            state = P1.LatinSqState(ex)
            searcher = A1Search.Search(problem, timelimit=timelimit)
            answer = searcher.DepthFirstSearch(state)
        elif solver == 'BFS':
            problem = P1.LatinSqProblem()
            state = P1.LatinSqState(ex)
            searcher = A1Search.Search(problem, timelimit=timelimit)
            answer = searcher.BreadthFirstSearch(state)
        elif solver == 'DLS':
            problem = P1.LatinSqProblem()
            state = P1.LatinSqState(ex)
            searcher = A1Search.Search(problem, timelimit=timelimit)
            answer = searcher.DepthLimitedSearch(state, int(sys.argv[4]))
        elif solver == 'IDS':
            problem = P1.LatinSqProblem()
            state = P1.LatinSqState(ex)
            searcher = A1Search.Search(problem, timelimit=timelimit)
            answer = searcher.IDS(state)

        if answer.success == True:
            num_completed += 1
            output = 'S - '
        else:
            num_failed += 1
            output = 'F - '

        print(str(output) + 'S:' + str(num_completed) + ',F:' + str(num_failed) + ' ' + str(answer))

    elif question == 'a3q2':

        if solver == 'DFS':
            problem = P2.LatinSqProblem(ex)
            state = problem.create_initial_state()
            searcher = A1Search.Search(problem, timelimit=timelimit)
            answer = searcher.DepthFirstSearch(state)
        elif solver == 'BFS':
            problem = P2.LatinSqProblem()
            state = problem.create_initial_state()
            searcher = A1Search.Search(problem, timelimit=timelimit)
            answer = searcher.BreadthFirstSearch(state)
        elif solver == 'DLS':
            problem = P2.LatinSqProblem()
            state = problem.create_initial_state()
            searcher = A1Search.Search(problem, timelimit=timelimit)
            answer = searcher.DepthLimitedSearch(state, int(sys.argv[4]))
        elif solver == 'IDS':
            problem = P2.LatinSqProblem()
            state = problem.create_initial_state()
            searcher = A1Search.Search(problem, timelimit=timelimit)
            answer = searcher.IDS(state)

        if answer.success == True:
            num_completed += 1
            output = 'S - '
        else:
            num_failed += 1
            output = 'F - '

        print(str(output) + 'S:' + str(num_completed) + ',F:' + str(num_failed) + ' ' + str(answer))

    elif question == 'a3q3':

        if solver == 'DFS':
            problem = P3.LatinSqProblem(ex)
            state = problem.create_initial_state()
            searcher = A1Search.Search(problem, timelimit=timelimit)
            answer = searcher.DepthFirstSearch(state)
        elif solver == 'BFS':
            problem = P3.LatinSqProblem()
            state = problem.create_initial_state()
            searcher = A1Search.Search(problem, timelimit=timelimit)
            answer = searcher.BreadthFirstSearch(state)
        elif solver == 'DLS':
            problem = P3.LatinSqProblem()
            state = problem.create_initial_state()
            searcher = A1Search.Search(problem, timelimit=timelimit)
            answer = searcher.DepthLimitedSearch(state, int(sys.argv[4]))
        elif solver == 'IDS':
            problem = P3.LatinSqProblem()
            state = problem.create_initial_state()
            searcher = A1Search.Search(problem, timelimit=timelimit)
            answer = searcher.IDS(state)

        if answer.success == True:
            num_completed += 1
            output = 'S - '
        else:
            num_failed += 1
            output = 'F - '

        print(str(output) + 'S:' + str(num_completed) + ',F:' + str(num_failed) + ' ' + str(answer))

    elif question == 'a3q4':

        if solver == 'DFS':
            problem = P4.LatinSqProblem(ex)
            state = problem.create_initial_state()
            searcher = A1Search.Search(problem, timelimit=timelimit)
            answer = searcher.DepthFirstSearch(state)
        elif solver == 'BFS':
            problem = P4.LatinSqProblem()
            state = problem.create_initial_state()
            searcher = A1Search.Search(problem, timelimit=timelimit)
            answer = searcher.BreadthFirstSearch(state)
        elif solver == 'DLS':
            problem = P4.LatinSqProblem()
            state = problem.create_initial_state()
            searcher = A1Search.Search(problem, timelimit=timelimit)
            answer = searcher.DepthLimitedSearch(state, int(sys.argv[4]))
        elif solver == 'IDS':
            problem = P4.LatinSqProblem()
            state = problem.create_initial_state()
            searcher = A1Search.Search(problem, timelimit=timelimit)
            answer = searcher.IDS(state)

        if answer.success == True:
            num_completed += 1
            output = 'S - '
        else:
            num_failed += 1
            output = 'F - '

        print(str(output) + 'S:' + str(num_completed) + ',F:' + str(num_failed) + ' ' + str(answer))

    else:
        answer = None # and this will cause run time error below
