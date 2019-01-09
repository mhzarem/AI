class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state.  Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node.  Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, individual=[], path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.individual = individual
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return self.child_node(problem)

    def child_node(self, problem):
        nodes = []
        all_next_state, all_next_individual = problem.results(self.state)
        for state in all_next_state:
            individual = [x for x in self.individual]
            individual.append(all_next_individual[all_next_state.index(state)])
            next_node = Node(state, self, individual, self.path_cost + 1)
            nodes.append(next_node)
        return nodes

    def un_expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return self.un_child_node(problem)

    def un_child_node(self, problem):
        nodes = []
        all_next_state, all_next_individual = problem.un_results(self.state)
        for state in all_next_state:
            individual = [x for x in self.individual]
            individual.append(all_next_individual[all_next_state.index(state)])
            next_node = Node(state, self, individual, self.path_cost + 1)
            nodes.append(next_node)
        return nodes

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node.state)
            node = node.parent
        return list(reversed(path_back))
