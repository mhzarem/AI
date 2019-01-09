class Problem(object):

    def __init__(self):
        """The constructor specifies the initial state, and possibly a goal state."""
        self.goal = [(1, 2, 3, 4, 5, 6, 7, 8, 0)]

    def results(self, state):
        """Return the results that can be executed in the given
        state. The result would typically be a list."""
        result = []
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = state.index(0)

        if index_blank_square % 3 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 3:
            possible_actions.remove('UP')
        if index_blank_square % 3 == 2:
            possible_actions.remove('RIGHT')
        if index_blank_square > 5:
            possible_actions.remove('DOWN')

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}

        for action in possible_actions:
            new_state = list(state)
            neighbor = index_blank_square + delta[action]
            new_state[index_blank_square], new_state[neighbor] = new_state[neighbor], new_state[index_blank_square]
            result.append(tuple(new_state))

        return result

    def goal_test(self, state):
        """Return True if the state is a goal."""
        # print (state)
        # print (self.goal)
        if state in self.goal:
            return True
        else:
            return False

    def check_solvability(self, state):
        """ Checks if the given state is solvable """

        inversion = 0
        for i in range(len(state)):
            for j in range(i, len(state)):
                if state[i] > state[j] != 0:
                    inversion += 1

        return inversion % 2 == 0
