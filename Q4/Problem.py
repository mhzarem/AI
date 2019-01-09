import numpy as np
import copy


class Problem(object):
    def __init__(self, state):
        self.state = state
        self.iter = [0, 0]
        self.cost = self.cost_calculate(state)

    def __repr__(self):
        return "State: {} Cost:{}".format(self.state, self.cost)

    def step_results(self):
        """Return the results that can be executed in the given
        state. The result would typically be a list."""
        len_state = len(self.state)
        if self.iter[1] == len_state:
            return None
        else:
            for i in range(self.iter[0], len_state):
                for j in range(self.iter[1], len_state):
                    new_state = copy.deepcopy(self.state)
                    new_state[i], new_state[j] = self.state[j], self.state[i]
                    if self.iter[1] + 1 == len_state:
                        self.iter[0] += 1
                        self.iter[1] = 0
                    else:
                        self.iter[1] += 1
                    return new_state


    @staticmethod
    def all_results(state):
        len_state = len(state)
        results = []
        for i in range(0, len_state):
            for j in range(i + 1, len_state):
                new_state = copy.deepcopy(state)
                new_state[i], new_state[j] = state[j], state[i]
                results.append(new_state)
        return results

    @staticmethod
    def cost_calculate(state):
        size = int(len(state) / 3)
        max_cost = 0
        for i in range(0, size):
            max_cost = max(max_cost, state[3 * i] + state[3 * i + 1] + state[3 * i + 2])
        return max_cost


