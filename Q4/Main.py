from AI_Project.Q4.Problem import Problem
from AI_Project.Q4.Search import *
# initializing problem
initial = [2, 8, 6, 5, 2, 0]
problem = Problem(initial)
print(simple_hill_climbing(problem))
print(stochastic_hill_climbing(problem))
print(first_choice_hill_climbing(problem))
print(random_restart_hill_climbing(problem, 10))


