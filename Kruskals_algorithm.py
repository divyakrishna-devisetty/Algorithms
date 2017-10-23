from collections import defaultdict

import os

import sys

import itertools

from graph import Graph


class MSTAlgo(object):
    def __init__(self, graph):
        self.nodes_list = graph.nodes
        self.MST = set()
        self.weights_dict = graph.distances
        self.edge_parent_dict = defaultdict(list)

    def mst(self, sorted_list_of_edges, k=0):
        n = len(self.nodes_list)
        count = 0

        for node in self.nodes_list:
            self.edge_parent_dict[node].append(node)
        for edge in sorted_list_of_edges:
            u = edge[0]
            v = edge[1]
            # print "node u:", u
            # print "parent of u:", find(u)
            # print "node v:", v
            # print "parent of v:", find(v)
            if self.find(v) != self.find(u):
                self.MST.add(edge)
                self.union(u, v)
            # else:
            #     print("("+u+ " , "+ v+ ")forms a cycle as they belong to same set")
            # Below logic is for k-spacing MST
            if k > 0:
                count += 1
                if count > n - k:
                    # print "count is n-k:", count
                    print("Node Set:", self.edge_parent_dict.values())
                    node_set = list(itertools.chain(*list(self.MST)))
                    print("nodes:", set(node_set))
                    print("Edge Set:", sorted(self.MST))
                    print("MST Total weight on MST edges:", self.total_weight(self.MST))
                    return self.MST
        print("Node Set:", self.edge_parent_dict.values())
        node_set = list(itertools.chain(*list(self.MST)))
        print("now:",set(node_set))
        print("Edge Set:", sorted(self.MST))
        print("MST Total weight on MST edges:", self.total_weight(self.MST))

    def total_weight(self, mst):
        return sum([self.weights_dict[edge] for edge in mst])

    def parent(self, node):
        for parent_node, child in self.edge_parent_dict.items():
            if node in child:
                return parent_node

    def find(self, node):
        return self.parent(node)

    def union(self, node_1, node_2):
        node1 = self.find(node_1)
        node2 = self.find(node_2)
        # print("in union node1:", node1)
        # print("in union node2:", node2)
        # print("edge dict b4:", self.edge_parent_dict)
        # print("edge dict node1 len:", len(self.edge_parent_dict.get(node1)))
        # print("edge dict node2 len:", len(self.edge_parent_dict.get(node2)))
        if len(self.edge_parent_dict.get(node1)) > len(self.edge_parent_dict.get(node2)):
            self.edge_parent_dict.get(node1).extend(self.edge_parent_dict[node2])
            del self.edge_parent_dict[node2]
        elif len(self.edge_parent_dict.get(node1)) < len(self.edge_parent_dict.get(node2)):
            self.edge_parent_dict.get(node2).extend(self.edge_parent_dict[node1])
            del self.edge_parent_dict[node1]
        else:
            # print("len(node1)", node1, "==", "len(node2):", node2)
            self.edge_parent_dict.get(node1).extend(self.edge_parent_dict[node2])
            del self.edge_parent_dict[node2]
            # print("edge dict after:", self.edge_parent_dict)


def main():
    if not os.path.isfile('kruskals_input'):
        print ("Please read input from file: kruskals_input")
        sys.exit(1)
    input_file = open('kruskals_input', "r")
    context = file.readlines(input_file)
    graph = Graph()
    if context:
        nodes_input_line = context.pop(0)
        for node in nodes_input_line.split(','):
            graph.add_node(node.strip())
        for lines in context:
            edge_detail_container = lines.split(',')
            start_node = edge_detail_container[0]
            end_node = edge_detail_container[1]
            distance = int(edge_detail_container[2])
            graph.add_edge(start_node, end_node, distance)
            graph.add_node(start_node)
    mst = MSTAlgo(graph)
    sorted_list_of_edges = sorted(mst.weights_dict, key=mst.weights_dict.get)
    print("Enter k-spacing between 0 to %d. Enter 0 for no spacing:"%len(graph.nodes))
    spacing = int(raw_input())
    mst.mst(sorted_list_of_edges, k=spacing)  # for mst k-spacing algorithm


main()
