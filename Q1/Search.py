from collections import deque
from AI_Project.Q1.Node import Node
open('out.txt', 'w')


def breadth_first_tree_search(initial, problem):
    """Search the shallowest nodes in the search tree first.
        Search through the successors of a problem to find a goal.
        The argument frontier should be an empty queue.
        Repeats infinitely in case of loops. [Figure 3.7]"""
    f = open('out.txt', 'a')
    frontier = deque([Node(initial)])  # FIFO queue
    max_frontier = len(frontier)
    seen = []

    while frontier:
        node = frontier.popleft()
        seen.append(node)
        if problem.goal_test(node.state):
            len_seen = len(seen)
            print("**********************Breadth First Search*********************", file=f)
            print("the number of expanded nodes: {}".format(len_seen), file=f)
            print("the number of made nodes: {}".format(len_seen + len(frontier)), file=f)
            print("the maximum number of made nodes: {}".format(max_frontier), file=f)
            print("result: {}".format(node.individual), file=f)
            print("depth of result: {}".format(node.depth), file=f)
            return node
        frontier.extend(node.expand(problem))
        len_frontier = len(frontier)
        if max_frontier < len_frontier:
            max_frontier = len_frontier
    print('have no result')
    return None


def depth_first_tree_search(initial, problem):
    """Search the deepest nodes in the search tree first.
        Search through the successors of a problem to find a goal.
        The argument frontier should be an empty queue.
        Repeats infinitely in case of loops. [Figure 3.7]"""
    f = open('out.txt', 'a')
    frontier = [Node(initial)]  # Stack
    max_frontier = len(frontier)
    seen = []
    while frontier:
        node = frontier.pop()
        seen.append(node)
        if problem.goal_test(node.state):
            len_seen = len(seen)
            print("**********************Depth First Search*********************", file=f)
            print("the number of expanded nodes: {}".format(len_seen), file=f)
            print("the number of made nodes: {}".format(len_seen + len(frontier)), file=f)
            print("the maximum number of made nodes: {}".format(max_frontier), file=f)
            print("result: {}".format(node.individual), file=f)
            print("depth of result: {}".format(node.depth), file=f)
            return node

        expanded_node = node.expand(problem)
        step_front = []
        for item in expanded_node:
            if item.individual not in [x.individual for x in seen]:
                frontier.append(item)
                step_front.append(item)
        len_frontier = len(frontier)
        if max_frontier < len_frontier:
            max_frontier = len_frontier
    print('have no result')
    return None


def bidirectional_search(initial, end, problem):
    """Search the shallowest nodes in the search tree first.
            Search through the successors of a problem to find a goal.
            The argument frontier should be an empty queue.
            Repeats infinitely in case of loops. [Figure 3.7]"""
    frontier = deque([Node(initial)])  # FIFO queue
    interior = deque([Node(end)])
    seen_f = []
    seen_i = []
    max_len_f = len(frontier)
    max_len_i = len(interior)

    f = open('out.txt', 'a')
    while frontier:
        for item_f in frontier:
            for item_i in interior:
                if item_f.state == item_i.state:
                    len_made = len(frontier) + len(interior)
                    len_seen = len(seen_f) + len(seen_i)
                    print("**********************Bidirectional Search*********************", file=f)
                    print("the number of expanded nodes: {}".format(len_seen), file=f)
                    print("the number of made nodes: {}".format(len_seen + len_made), file=f)
                    print("the maximum number of made nodes: {}".format(max_len_f + max_len_i), file=f)
                    print("result: {}".format(item_f.individual + item_i.individual), file=f)
                    print("depth of result: {}".format(node_i.depth + node_f.depth), file=f)

                    return item_f.individual + item_i.individual

        node_f = frontier.popleft()
        node_i = interior.popleft()
        seen_f.append(node_f)
        seen_i.append(node_i)

        frontier.extend(node_f.expand(problem))
        interior.extend(node_i.un_expand(problem))

        max_len_f = max(max_len_f, len(frontier))
        max_len_i = max(max_len_i, len(interior))


    return None








