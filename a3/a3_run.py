# -*- coding: utf-8 -*-

# Willis Kirkham
# 11084378
# wrk027
# C317 - a1

import gc as gc
import sys as sys

import a3.a3q1 as P
import a3.A1Search as A1Search


# if len(sys.argv) < 4:
#     print('usage: python a3_run examplefile solver timelimit [depthlimit]')
#     sys.exit()
# #
# file = open(sys.argv[1], 'r')
# solver = sys.argv[2]
# timelimit = int(sys.argv[3])

file = open('LatinSquares.txt', 'r').readlines()
solver = 'RRHCS'
timelimit = 20
restarts = 50

if solver not in ['DFS', 'BFS', 'DLS', 'IDS']:
    print('solver', solver, 'not known')
    sys.exit()

if solver == 'DLS' and len(sys.argv) != 5:
    print('missing depthlimit for DLS (last arg)')
    sys.exit()

print(sys.argv)

examples = []


# Process the input file, create a list of squares
quantity = int(file[0])
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

for ex in examples:

    gc.collect()  # clean up any allocated memory now, before we start timing stuff

    if solver == 'DFS':
        problem = P.LatinSqProblem()
        state = P.LatinSqState(ex)
        searcher = A1Search.Search(problem, timelimit=timelimit)
        answer = searcher.DepthFirstSearch(state)

#     elif solver == 'RSS':
#         problem = P.TargetedCodingProblem(ex[0], ex[1])
#         answer = Search.random_search(problem, timelimit)
#
#     elif solver == 'HCS':
#         problem = P.TargetedCodingProblem(ex[0], ex[1])
#         answer = Search.hill_climbing_search(problem, timelimit)
#
#     elif solver == 'RRHCS':
#         problem = P.TargetedCodingProblem(ex[0], ex[1])
#         answer = Search.random_restart_hill_climbing_search(problem, timelimit, int(sys.argv[4]))
#
#     elif solver == 'SHCS':
#         problem = P.TargetedCodingProblem(ex[0], ex[1])
#         answer = Search.stochastic_hill_climbing_search(problem, timelimit)
#
#     else:
#         answer = None # and this will cause run time error below
#
#     error = (problem.target - answer.result.register)/problem.target
#     sum_err_sq += error**2
#
#     total_time += answer.time
#
#     # Print the result of each example
#     # print(str(answer.result))
#     # print('target: ' + str(ex[0]) + '\noperands: ' + str(ex[1]) + '\n' + str(answer.time) + '\n')
#
# # Calc some stats and print them
# rmse = (sum_err_sq/len(examples))**(.5)
# avg_time = total_time/len(examples)
# print('Avg time: ' + str(avg_time))
# print('RMSE: ' + str(rmse))


def read_squares(square):
    """"
    Puts latin squares in a list
    """

    square = []

    for curr in square:
        row = curr.rstrip().split(' ')
        square.append(row)

    return square

