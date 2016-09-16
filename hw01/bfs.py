"""
# @author Anthony (Tony) Poerio
# @email adp59@pitt.edu
# University of Pittsburgh
# Fall 2016
# Computer Science 1571 - Artificial Intelligence
# Assignment 01
# Search Algorithm Implementations for Three Puzzle Types
#
# This File:  Breadth First Search  (BFS)
#
"""

import collections
from copy import deepcopy

class Node:
    def __init__(self, parent_node, state, puzzle, total_cost=0):
        # initialize parent node, so we know where we came from,
        # and later we can find a path
        self.parentNode = parent_node
        # define base case for parent nodes
        if parent_node is not None:
            self.depth = parent_node.depth + 1
        else:
            self.depth = 0

        # store the current state
        self.current_state = state

        # store the successor states
        self.successor_states = puzzle.getSuccessorStates(state)

        # store the cost of making it this far,
        # we'll want to either have the max or min
        self.total_cost = total_cost

class BFS:
   def __init__(self, puzzle):
       self.frontier = collections.deque()
       self.explored = set()
       self.puzzle = puzzle
       self.graph = set()

       # careful here...
       self.current_node = None
       return

   def bfs(self):
       # create a node for the initial state, this is our entry point on the graph
       start_node = Node(parent_node=None, state=self.puzzle.initial_state,
                         puzzle=self.puzzle, total_cost=0)
       self.graph.add(start_node)
       self.frontier.extendleft(start_node.successor_states)

       # store start_node as parent_node, so we can create nodes as we proceed
       self.current_node = start_node

       # run the algorithm while the frontier still has valid states
       while not len(self.frontier) == 0:

           # dequeue the first item that was entered in the frontier
           next_state = self.frontier.pop()

           # this new state is now in our graph, so turn it into a node, and add it
           next_node = Node(parent_node=deepcopy(self.current_node), state=next_state,
                            puzzle=self.puzzle, total_cost=0)

           # check if we have a match, if so -- we've found the end state
           if self.puzzle.goalTest(next_state):
               # Need to return the path that got us here
               print str(next_state)
               return True

           # add the node to the explored list, if it's not a match
           self.explored.add(next_state)

           # and expand our frontier, so that it contains everything on the list of our new node
           for elem in next_node.successor_states:
                self.frontier.appendleft(elem)

           # test if we have the correct goal state

       return

