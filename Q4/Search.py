from AI_Project.Q4.Problem import *
f = open('out.txt', 'a')

def simple_hill_climbing(problem):
    # if __name__ == "simple_hill_climbing":
    print("******Simple Hill Climbing*****",file=f)
    continue_alg = True
    while continue_alg:
        print(problem, file=f)
        continue_alg = False
        min_cost = float("infinity")
        global min_state
        min_state = problem.state
        all_next = Problem.all_results(problem.state)
        for item in all_next:
            cost = Problem.cost_calculate(item)
            if cost < min_cost:
                min_cost = cost
                min_state = item

        if min_cost < problem.cost:
            continue_alg = True
            problem.cost = min_cost
            problem.state = min_state
    return problem


def stochastic_hill_climbing(problem):
    continue_alg = True
    print("****Stochastic Hill Climbing***", file=f)
    while continue_alg:
        continue_alg = False
        all_next = Problem.all_results(problem.state)

        all_cost = [problem.cost - Problem.cost_calculate(x) if problem.cost - Problem.cost_calculate(x) > 0 else 0
                    for x in all_next]

        sum_cost = sum(all_cost)
        if sum_cost != 0:
            all_cost[:] = [x / sum_cost for x in all_cost]
            index = np.random.choice(len(all_next), 1, p=all_cost)[0]
            continue_alg = True
            problem = Problem(all_next[index])
        print(problem, file=f)
    return problem


def random_restart_hill_climbing(problem, num_reset):
    print("******Random Restart Hill Climbing*****", file=f)
    state = problem.state
    for _ in range(0, num_reset):
        new_state = copy.deepcopy(state)
        size = int(len(state) / 3)
        a = np.random.randint(0, size)
        b = np.random.randint(0, size)
        c = np.random.randint(0, 3)
        d = np.random.randint(0, 3)
        new_state[3 * a + c], new_state[3 * b + d] = state[3 * b + d], state[3 * a + c]
        p = Problem(new_state)
        r = simple_hill_climbing(p)
        if r:
            return r

    return None


def first_choice_hill_climbing(problem):
    print("*****First Choice Hill Climbing****", file=f)
    step = problem.state
    while step:
        if Problem.cost_calculate(step) < problem.cost:
            problem = Problem(step)

        step = problem.step_results()
    print(problem, file=f)
    return problem
