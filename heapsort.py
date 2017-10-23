#!/usr/bin/python
import os

import sys

__author__ = 'Divya_krishna_Devisetty'


# Method to perform Heap sort. Takes list input.
def heap_sort(edge_weight_array):
    heapify(edge_weight_array)
    print("After heapify:", edge_weight_array)
    last_index = len(edge_weight_array) - 1
    while last_index >= 0:
        # Swap
        edge_weight_array[last_index], edge_weight_array[0] = edge_weight_array[0], edge_weight_array[last_index]
        last_index -= 1
        siftup(edge_weight_array, 0, last_index)  # Call sift_up method for descending operation


# Method to perform heapify operation. Takes list input.
def heapify(edge_weight_array):
    last_index = len(edge_weight_array) - 1
    last_parent_index = (last_index - 1) / 2  # Parent_index is (i-1)/2 for a left balanced binary tree.
    while last_parent_index >= 0:
        siftup(edge_weight_array, last_parent_index, last_index)
        last_parent_index -= 1


# Method to sift_down the array elements. Call for ascending order of array output.
def siftdown(edge_weight_array, parent_index, last_index):
    # Left child is present at (2*i)+1; This condition checks if left child exists.
    while (parent_index * 2) + 1 <= last_index:
        child_index = parent_index * 2 + 1
        # Right child is present at (2*i)+2;
        # This condition checks if right child exists and if its less than left child.
        if child_index + 1 <= last_index and edge_weight_array[child_index] < edge_weight_array[child_index + 1]:
            # child_node_to_swap = max(edge_weight_array[child_index], edge_weight_array[child_index+1])
            child_index = child_index + 1
        # Check if parent_node is less than child node
        if edge_weight_array[parent_index] < edge_weight_array[child_index]:
            # Swap
            edge_weight_array[parent_index], edge_weight_array[child_index] = edge_weight_array[child_index], \
                                                                              edge_weight_array[parent_index]
            parent_index = child_index
        else:
            return


# Method to sift_up the array elements. Call for descending order of array output.
def siftup(edge_weight_array, parent_index, last_index):
    # Left child is present at (2*i)+1; This condition checks if left child exists.
    while (parent_index * 2) + 1 <= last_index:
        child_index = parent_index * 2 + 1
        # Right child is present at (2*i)+2;
        # This condition checks if right child exists and if its greater than left child.
        if child_index + 1 <= last_index and edge_weight_array[child_index] > edge_weight_array[child_index + 1]:
            # child_node_to_swap = min(edge_weight_array[child_index], edge_weight_array[child_index+1])
            child_index = child_index + 1
        # Check if parent_node is greater than child node
        if edge_weight_array[parent_index] > edge_weight_array[child_index]:
            # Swap
            edge_weight_array[parent_index], edge_weight_array[child_index] = edge_weight_array[child_index], \
                                                                              edge_weight_array[parent_index]
            parent_index = child_index
        else:
            return


def main():
    # Read input from file.
    if not os.path.isfile('heap_input.txt'):
        print ("Please read input from file: heap_input.txt")
        sys.exit(1)
    input_file = open('heap_input.txt', "r")
    context = file.readline(input_file)
    edge_weights = [int(weights) for weights in context.split(',')]
    print("Unsorted input from file:", edge_weights)
    heap_sort(edge_weights)
    print("Sorted list:", edge_weights)


main()
