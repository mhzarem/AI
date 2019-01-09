from AI_Project.Q3.Problem import Problem
from AI_Project.Q3.Search import *
import numpy as np

f = open("result.txt", 'w')


# initializing problem

initial = [[0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0,-1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0,-1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [2, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 2, 0, 0, 0]]
problem = Problem()

result = breadth_first_tree_search(initial, problem).path()
print("***********************Breadth First Search********************", file=f)
for num, item in enumerate(result):
    print("step {} is:\n{}".format(num, np.matrix(item)), file=f)


result = depth_first_tree_search(initial, problem).path()
print("***********************Depth First Search********************", file=f)
for num, item in enumerate(result):
    print("step {} is:\n{}".format(num, np.matrix(item)), file=f)

result = iter_depth_first_tree_search(initial, problem, 10).path()
print("***********************Iterative Depth First Search********************", file=f)
for num, item in enumerate(result):
    print("step {} is:\n{}".format(num, np.matrix(item)), file=f)

result = uniform_cost(initial, problem).path()
print("***********************Uniform Cost Search********************", file=f)
for num, item in enumerate(result):
    print("step {} is:\n{}".format(num, np.matrix(item)), file=f)