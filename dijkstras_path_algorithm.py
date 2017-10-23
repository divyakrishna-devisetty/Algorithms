import copy
import os
from graph import Graph

import sys

__author__ = 'Divya_krishna_Devisetty'


def run_dijkstras(graph, src, dest):
    visited_nodes = set()
    distances = {}
    parent = dict()

    distances[src] = 0
    minimum_distance_node = src
    while len(visited_nodes) < len(graph.nodes):
        # print "current_src_node:", minimum_distance_node
        if minimum_distance_node == dest:
            # We build the shortest path and display it
            path = []
            prev = dest
            while prev != None:
                path.append(prev)
                prev = parent.get(prev, None)
            print('shortest path: ' + str(path[::-1]) + " cost=" + str(distances[dest]))
            return

        for neighbor in graph.edges[minimum_distance_node]:
            if neighbor not in visited_nodes:
                # print "neighbor:", neighbor
                new_distance = distances[minimum_distance_node] + graph.distances[minimum_distance_node][
                    neighbor]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    parent[neighbor] = minimum_distance_node
                    # print "parent[%s]:" % neighbor, parent[neighbor]

        visited_nodes.add(minimum_distance_node)
        reference_distances_dict = copy.deepcopy(distances)

        # print "reference_distances_dict:", reference_distances_dict
        # print "visited_nodes:", visited_nodes


        # Delete visited node entries from dictionary so that we calculate minimum distance for the valid ones.
        for node in visited_nodes:
            del reference_distances_dict[node]
        minimum_distance_node = min(reference_distances_dict, key=reference_distances_dict.get)


def main():
    # Read input from file.
    if not os.path.isfile('dijkstras_input'):
        print ("Please read input from file: dijkstras_input")
        sys.exit(1)
    input_file = open('dijkstras_input', "r")
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

    print("Enter a source node among:",graph.nodes)
    src = raw_input()
    print("Enter dest node among:",graph.nodes)
    dest = raw_input()
    if src not in graph.nodes:
        print("Enter a valid source")
    if dest not in graph.nodes:
        print("Enter a valid destination")

    run_dijkstras(graph, src, dest)


main()
