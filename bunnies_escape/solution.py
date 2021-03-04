from operator import attrgetter
import unittest

##G_COST = DISTANCE FROM STARt
##H_COST = DISTANCE TO THE GOAL
##F_COST = SUM OF G+H

class Node:
    def __init__(self, pos, parent=None):
        #pos is a tuple
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.g_cost = 0
        self.h_cost = 0
        self.f_cost = 0
        # parent is a Node
        self.parent = parent

    def update_g(self, start):
        if self.parent:
            self.g_cost = self.parent.g_cost + 1
        else:
            self.g_cost = abs(self.pos[1] - start.pos[1])+\
                      abs(self.pos[0] - start.pos[0])

    def update_h(self, finish):
        self.h_cost = abs(self.pos[0] - finish.pos[0]) + \
                      abs(self.pos[1] - finish.pos[1])

    def update_f(self, start, finish):
        self.update_g(start)
        self.update_h(finish)
        self.f_cost = self.g_cost + self.h_cost

    def in_bounds(self, matrix):
        try:
            if self.x>=0 and self.y>=0 and \
                    matrix[self.x][self.y] == 0:
                return True
            else:
                return False
        except:
            return False

    def get_children(self, analyzed, m):
        children= []
        # No diagonal movement allowed
        nodes = [Node((self.x, self.y - 1), self),
                 Node((self.x, self.y + 1), self),
                 Node((self.x - 1, self.y), self),
                 Node((self.x + 1, self.y), self)]
        for node in nodes:
            flag = 0
            for an_node in analyzed:
                if node.pos == an_node.pos:
                    flag = 1
            if node.in_bounds(m) and flag == 0:
                children.append(node)
        return children


def get_smallest_f_cost(lst_of_nodes):
    nodes = sorted(lst_of_nodes, key=attrgetter('f_cost'))
    minimum = nodes[0]
    # If two or more nodes have the same f cost, we choose the one with the
    # smallest h cost
    for node in nodes[1:]:
        if node.f_cost == minimum.f_cost:
            if node.h_cost < minimum.h_cost:
                minimum = node
    return minimum

def shortest_path(m):
    start = Node((0,0))
    fin_coord_tuple = (len(m)-1, len(m[-1])-1)
    fin = Node(fin_coord_tuple)
    start.update_f(start, fin)
    potential_nodes = [start]
    analyzed_nodes = []
    while potential_nodes:

        # getting current node
        cur_node = get_smallest_f_cost(potential_nodes)
        analyzed_nodes.append(cur_node)
        potential_nodes.remove(cur_node)

        # if found
        if cur_node.pos == fin_coord_tuple:
            path = []
            current = cur_node
            while current is not None:
                path.append(current.pos)
                current = current.parent
            return path[::-1]  # Return reversed path

        # children
        children = cur_node.get_children(analyzed_nodes, m)
        for child in children:
            flag = 0
            child.update_f(start, fin)

            for pot_node in potential_nodes:
                if child.pos == pot_node.pos and \
                        child.g_cost > pot_node.g_cost:
                    flag = 1
            if flag == 0:
                potential_nodes.append(child)
    return "No path"





