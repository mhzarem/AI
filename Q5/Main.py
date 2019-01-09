from AI_Project.Q5.Problem import Problem
from AI_Project.Q5.Search import *
initial = [
            [3, 5, 2, 6, 2, 3, 2, 4, 4],
            [1, 1, 5, 5, 5, 2, 3, 1, 3],
            [3, 3, 5, 3, 3, 3, 4, 2, 5],
            [6, 5, 1, 1, 1, 6, 6, 5, 6],
            [5, 1, 2, 4, 4, 4, 2, 6, 1],
            [1, 2, 4, 2, 6, 4, 4, 6, 6]
        ]

problem = Problem(initial)
print(simulated_annealing(problem).state)
