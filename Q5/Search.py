from AI_Project.Q5.Problem import *


def probability_maker(start_temperature, iteration, basice_cost, neighor_cost):
    # first strategy
    temp = (start_temperature - iteration) if (start_temperature - iteration) == 0 else 1
    dif_cost = neighor_cost - basice_cost

    # p = 1 / temp * (100)
    # if 0 < p <= 1:
    #     print(p)
    #     return p
    #
    # else:
    #     return 0

    # second strategy
    p = np.exp(- 1 / (temp + 1))
    if 0 < p <= 1:
        print(p)
        return p

    else:
        return 0

    # third strategy
    # a = 2
    # b = 1
    # c = 1
    # new_temp = a * temp + b
    # new_cost = c * dif_cost + 1
    # p = np.exp(- new_cost / new_temp)
    # if 0 < p <= 1:
    #     print(p)
    #     return p
    #
    # else:
    #     return 0


def simulated_annealing(problem):
    start_temperature = 100
    n_iter = 1
    neighbor = Problem.all_results(problem.state)

    while neighbor:

        item = neighbor.pop()
        cost = Problem.cost_calculate(item)
        print(cost, problem.cost)
        if cost <= problem.cost:

                problem = Problem(item)
                neighbor = Problem.all_results(problem.state)
        else:

                probability = probability_maker(start_temperature, n_iter, problem.cost, cost)

                select = np.random.choice(2, 1, p=[1 - probability, probability])

                if select:

                    problem = Problem(item)
                    neighbor = Problem.all_results(problem.state)
        n_iter += 1
    return problem


