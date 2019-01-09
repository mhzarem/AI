import numpy as np
import copy
from collections import deque


class Problem(object):

    def __init__(self, initial):
        """The constructor specifies the initial state, and possibly a goal state."""
        self.state = initial
        self.cost = self.cost_calculate(initial)
        self.goal = [[
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4, 4, 4, 4, 4],
            [5, 5, 5, 5, 5, 5, 5, 5, 5],
            [6, 6, 6, 6, 6, 6, 6, 6, 6]
        ]]

    @staticmethod
    def rotate(mat2):
        mat = copy.deepcopy(mat2)

        if not len(mat):
            return

        """ 
            top : starting row index 
            bottom : ending row index 
            left : starting column index 
            right : ending column index 
        """

        top = 0
        bottom = len(mat) - 1

        left = 0
        right = len(mat[0]) - 1

        while left < right and top < bottom:

            # Store the first element of next row,
            # this element will replace first element of
            # current row
            prev = mat[top + 1][left]

            # Move elements of top row one step right
            for i in range(left, right + 1):
                curr = mat[top][i]
                mat[top][i] = prev
                prev = curr

            top += 1

            # Move elements of rightmost column one step downwards
            for i in range(top, bottom + 1):
                curr = mat[i][right]
                mat[i][right] = prev
                prev = curr

            right -= 1

            # Move elements of bottom row one step left
            for i in range(right, left - 1, -1):
                curr = mat[bottom][i]
                mat[bottom][i] = prev
                prev = curr

            bottom -= 1

            # Move elements of leftmost column one step upwards
            for i in range(bottom, top - 1, -1):
                curr = mat[i][left]
                mat[i][left] = prev
                prev = curr

            left += 1

        return mat

    @staticmethod
    def all_results(state):

        """Return the results that can be executed in the given
        state. The result would typically be a list."""
        result = []
        plate = {

            'up': np.reshape(state[0], (-1, 3)),
            'left': np.reshape(state[1], (-1, 3)),
            'center': np.reshape(state[2], (-1, 3)),
            'right': np.reshape(state[3], (-1, 3)),
            'down': np.reshape(state[4], (-1, 3)),
            'downiest': np.reshape(state[5], (-1, 3)),

        }

        vertical = ['up', 'center', 'down', 'downiest']
        horizontal = ['left', 'center', 'right', 'downiest']
        # print(plate)
        # vertical

        queue_v = []
        queue_h = []
        queue_v.append(deque(x[0] for j in vertical for x in plate[j]))
        queue_v[0].rotate(3)
        queue_v.append(deque(x[1] for j in vertical for x in plate[j]))
        queue_v[1].rotate(3)
        queue_v.append(deque(x[2] for j in vertical for x in plate[j]))
        queue_v[2].rotate(3)
        # horizontal
        queue_h.append(deque(x for j in horizontal for x in plate[j][0]))
        queue_h[0].rotate(3)
        queue_h.append(deque(x for j in horizontal for x in plate[j][1]))
        queue_h[1].rotate(3)
        queue_h.append(deque(x for j in horizontal for x in plate[j][2]))
        queue_h[2].rotate(3)

        # rotation of left and right

        left = Problem.rotate(Problem.rotate(plate['left'].T)).T
        right = Problem.rotate(Problem.rotate(plate['right'].T)).T
        up = Problem.rotate(Problem.rotate(plate['up'].T)).T
        down = Problem.rotate(Problem.rotate(plate['down'].T)).T

        # step one for vertical
        # print('-------------------------vertical--------------------')
        for step in range(0, 3):
            plate_new = copy.deepcopy(plate)
            # print(plate_new)
            s = 0
            while s < len(queue_v[step]):
                for i in vertical:
                    for j in plate_new[i]:
                        j[step] = queue_v[step][s]
                        s = s + 1
            if step == 0:
                plate_new['left'] = left
            if step == 2:
                plate_new['right'] = right

            # print(plate_new)
            w = []
            for temp in plate_new:
                plate_new[temp] = np.reshape(plate_new[temp], (1, -1))[0]
                w.append(list(plate_new[temp]))
            result.append(w)

        # step one horizontal
        # print('------------------------horizontal---------------------')
        for step in range(0, 3):
            plate_new = copy.deepcopy(plate)
            # print(plate)
            s = 0
            while s < len(queue_h[step]):
                for i in horizontal:
                    # for j in plate_new[i][step]:
                    for j in range(0, 3):
                        plate_new[i][step][j] = queue_h[step][s]
                        s = s + 1
            if step == 0:
                plate_new['up'] = up
            if step == 2:
                plate_new['down'] = down
            # print(plate_new)
            w = []
            for temp in plate_new:
                plate_new[temp] = np.reshape(plate_new[temp], (1, -1))[0]
                w.append(list(plate_new[temp]))
            result.append(w)

        return result

    @staticmethod
    def cost_calculate(state):
        cost = 0
        for i in range(0, 6):
            for j in range(0, 9):
                if state[i][j] != i + 1:
                    cost = cost + 1
        return cost

    def goal_test(self, state):
        """Return True if the state is a goal."""
        if state in self.goal:

            return True
        else:

            return False
