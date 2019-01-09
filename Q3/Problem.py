import copy


class Problem(object):

    def __init__(self):
        """The constructor specifies the initial state, and possibly a goal state."""
        self.state = [[0, 0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, -1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, -1, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [2, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 2, 0, 0, 0]
                      ]
        self.goal = [
            [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, -1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, -1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 2, 0, 0, 0]
             ]
            ,
            [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, -1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, -1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [2, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0]
             ]
        ]

    @staticmethod
    def results(state):
        """Return the results that can be executed in the given
        state. The result would typically be a list."""
        result = []
        index = [s for j in state for s in j].index(1)

        i = int(index / 8)
        j = index % 8

        # down right
        next_i = i + 2
        next_j = j + 1
        if next_i < 8 and next_j < 8 and state[next_i][next_j] != -1:
            temp = copy.deepcopy(state)
            temp[i][j] = 0
            temp[next_i][next_j] = 1
            result.append(temp)

        # down left
        next_i = i + 2
        next_j = j - 1
        if next_i < 8 and -1 < next_j and state[next_i][next_j] != -1:
            temp = copy.deepcopy(state)
            temp[i][j] = 0
            temp[next_i][next_j] = 1
            result.append(temp)

        # up left
        next_i = i - 2
        next_j = j + 1
        if -1 < next_i and next_j < 8 and state[next_i][next_j] != -1:
            temp = copy.deepcopy(state)
            temp[i][j] = 0
            temp[next_i][next_j] = 1
            result.append(temp)

        # up right
        next_i = i - 2
        next_j = j - 1
        if -1 < next_i and -1 < next_j and state[next_i][next_j] != -1:
            temp = copy.deepcopy(state)
            temp[i][j] = 0
            temp[next_i][next_j] = 1
            result.append(temp)

        # right down
        next_i = i + 1
        next_j = j + 2
        if next_i < 8 and next_j < 8 and state[next_i][next_j] != -1:
            temp = copy.deepcopy(state)
            temp[i][j] = 0
            temp[next_i][next_j] = 1
            result.append(temp)

        # left down
        next_i = i + 1
        next_j = j - 2
        if next_i < 8 and -1 < next_j and state[next_i][next_j] != -1:
            temp = copy.deepcopy(state)
            temp[i][j] = 0
            temp[next_i][next_j] = 1
            result.append(temp)

        # right up
        next_i = i - 1
        next_j = j + 2
        if -1 < next_i and next_j < 8 and state[next_i][next_j] != -1:
            temp = copy.deepcopy(state)
            temp[i][j] = 0
            temp[next_i][next_j] = 1
            result.append(temp)

        # left up
        next_i = i - 1
        next_j = j - 2
        if -1 < next_i and -1 < next_j and state[next_i][next_j] != -1:
            temp = copy.deepcopy(state)
            temp[i][j] = 0
            temp[next_i][next_j] = 1
            result.append(temp)

        return result

    def goal_test(self, state):
        """Return True if the state is a goal."""
        if state in self.goal:
            return True
        else:
            return False
