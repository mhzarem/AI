from AI_Project.Q2.Problem import Problem
from AI_Project.Q2.Search import *

initial = (1, 2, 3, 4, 5, 7, 8, 6, 0)
end = (1, 2, 3, 4, 5, 6, 7, 8, 0)
problem = Problem()

# check the solve ability of problem
solve_ability = problem.check_solvability(initial)
print(solve_ability)
# solve the problem
if solve_ability:
    limited_depth_first_tree_search(initial, problem, 30)
    breadth_first_tree_search(initial, problem)
    bidirectional_search(initial, end, problem)
    depth_first_tree_search(initial, problem).path()
    a_star(initial, problem).path()




