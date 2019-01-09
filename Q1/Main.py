from AI_Project.Q1.Problem import Problem
from AI_Project.Q1.Search import *


# initializing problem
initial = [[0, 0], [0, 0], [0, 0], [0, 0]]
end = [[1, 1], [1, 1], [1, 1], [1, 1]]
problem = Problem()


breadth_first_tree_search(initial, problem)
bidirectional_search(initial, end, problem)
depth_first_tree_search(initial, problem)



