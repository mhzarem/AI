import numpy as np
class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state.  Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node.  Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.path_cost = self.path_cost_calculate(state)

    def __repr__(self):
        return "<Node {} Cost {}>".format(np.matrix(self.state),self.path_cost)

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return self.child_node(problem)

    def child_node(self, problem):
        next_node = problem.results(self.state)
        if self.path_cost_calculate(next_node) <= self.path_cost:
            return Node(next_node, self)
        return self


    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node.state)
            node = node.parent
        return list(reversed(path_back))

    def path_cost_calculate(self, state):
        # print(state)
        size = int(len(state) / 3)
        maxe = 0
        for i in range(0, size):
           maxe = max(maxe, state[3*i] + state[3*i + 1] + state[3*i + 2])
        return maxe