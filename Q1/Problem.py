import copy


class Problem(object):

    def __init__(self):
        """The constructor specifies the initial state, and possibly a goal state."""
        self.state = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.goal = [[[1, 1], [1, 1], [1, 1], [1, 1]]]

    @staticmethod
    def results(state):
        """Return the results that can be done in the given
        state. The result would typically be a list."""
        result = []         # list of possible next state
        individual = []     # whom will be transported
        for i in range(0, 4):
            for j in range(0, 2):

                if state[i][j] == 0:

                    # for one person
                    temp = copy.deepcopy(state)
                    temp[i][j] = 1
                    result.append(temp)
                    individual.append([(i, j)])
                    # for two person
                    for a in range(0, 4):
                        if state[a][j] == 0 and a != i:
                            temp = copy.deepcopy(state)
                            temp[i][j] = 1
                            temp[a][j] = 1
                            if temp not in result:
                                individual.append([(i, j), (a, j)])
                                result.append(temp)
                    for b in range(0, 2):
                        if state[i][b] == 0 and b != j:
                            temp = copy.deepcopy(state)
                            temp[i][j] = 1
                            temp[i][b] = 1
                            if temp not in result:
                                individual.append([(i, j), (i, b)])
                                result.append(temp)

        return result, individual

    @staticmethod
    def un_results(state):
        """Return the results that can be done in the given
        state. The result would typically be a list."""
        result = []  # list of possible next state
        individual = []  # whom will be transported
        for i in range(0, 4):
            for j in range(0, 2):

                if state[i][j] == 1:

                    # for one person
                    temp = copy.deepcopy(state)
                    temp[i][j] = 0
                    result.append(temp)
                    individual.append([(i, j)])
                    # for two person
                    for a in range(0, 4):
                        if state[a][j] == 1 and a != i:
                            temp = copy.deepcopy(state)
                            temp[i][j] = 0
                            temp[a][j] = 0
                            if temp not in result:
                                individual.append([(i, j), (a, j)])
                                result.append(temp)
                    for b in range(0, 2):
                        if state[i][b] == 1 and b != j:
                            temp = copy.deepcopy(state)
                            temp[i][j] = 0
                            temp[i][b] = 0
                            if temp not in result:
                                individual.append([(i, j), (i, b)])
                                result.append(temp)

        return result, individual

    def goal_test(self, state):
        """Return True if the state is a goal."""
        # print (state)
        # print (self.goal)
        if state in self.goal:
            return True
        else:
            return False


# p = Problem()
# print(p.un_results(p.goal[0]))
