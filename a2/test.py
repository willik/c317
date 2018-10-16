# -*- coding: utf-8 -*-

# Willis Kirkham
# 11084378
# wrk027
# C317 - a1

import gc as gc
import sys as sys

import TargetedCoding as P
import a2q6 as Search

# if len(sys.argv) < 4:
#     print('usage: python runCD examplefile solver timelimit [restarts]')
#     sys.exit()
#
# file = open(sys.argv[1], 'r')
# solver = sys.argv[2]
# timelimit = int(sys.argv[3])

file = open('a2_data_simple.txt', 'r')
solver = 'RRHCS'
timelimit = 20
restarts = 50

if solver not in ['RGS', 'RSS', 'HCS', 'RRHCS', 'SHCS']:
    print('solver', solver, 'not known')
    sys.exit()

# if solver == 'RRHCS' and len(sys.argv) != 5:
#     print('missing depthlimit for RRHCS (last arg)')
#     sys.exit()

print(sys.argv)

examples = []
for line in file:
    line = line.rstrip().split(' ')
    line[0] = float(line[0])
    for index, item in enumerate(line[1:]):
        line[index+1] = int(item)
    examples.append((line[0], line[1:]))

total_time = 0;
sum_err_sq = 0;

for ex in examples:

    gc.collect()  # clean up any allocated memory now, before we start timing stuff

    if solver == 'RGS':
        problem = P.TargetedCodingProblem(ex[0], ex[1])
        answer = Search.random_guessing(problem, timelimit)

    elif solver == 'RSS':
        problem = P.TargetedCodingProblem(ex[0], ex[1])
        answer = Search.random_search(problem, timelimit)

    elif solver == 'HCS':
        problem = P.TargetedCodingProblem(ex[0], ex[1])
        answer = Search.hill_climbing_search(problem, timelimit)

    elif solver == 'RRHCS':
        problem = P.TargetedCodingProblem(ex[0], ex[1])
        answer = Search.random_restart_hill_climbing_search(problem, timelimit, restarts)

    elif solver == 'SHCS':
        problem = P.TargetedCodingProblem(ex[0], ex[1])
        answer = Search.stochastic_hill_climbing_search(problem, timelimit)

    else:
        answer = None # and this will cause run time error below

    error = (problem.target - answer.result.register)/problem.target
    sum_err_sq += error**2

    total_time += answer.time

    # Print the result of each example
    # print(str(answer.result))
    # print('target: ' + str(ex[0]) + '\noperands: ' + str(ex[1]) + '\n' + str(answer.time) + '\n')

# Calc some stats and print them
rmse = (sum_err_sq/len(examples))**(.5)
avg_time = total_time/len(examples)
print('Avg time: ' + str(avg_time))
print('RMSE: ' + str(rmse))
