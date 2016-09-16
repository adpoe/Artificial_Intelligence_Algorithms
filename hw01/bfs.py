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
        # state the puzzle this is for
        self.puzzle = puzzle

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

        # ensure we are assigning parent nodes correctly
        #if parent_node is not None:
        #    if state not in parent_node.successor_states:
        #      suc_states = parent_node.successor_states
        #      assert state in parent_node.successor_states

        # store the successor states
        self.successor_states = puzzle.getSuccessorStates(state)

        self.successor_states_with_parent = set()
        for elem in self.successor_states:
            successor_and_parent = (elem, self)
            self.successor_states_with_parent.add(successor_and_parent)

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
       self.frontier_with_parent = []

       # time/space data
       self.solution_path = []
       self.num_nodes = 0
       self.frontier_max_size = 0
       self.num_explored_states = 0

       return

   def bfs(self):
       # create a node for the initial state, this is our entry point on the graph
       start_node = Node(parent_node=None, state=self.puzzle.initial_state,
                         puzzle=self.puzzle, total_cost=0)
       self.graph.add(start_node)
       self.frontier.extendleft(start_node.successor_states)
       for elem in start_node.successor_states_with_parent:
            self.frontier_with_parent.append(elem)

       # store start_node as parent_node, so we can create nodes as we proceed
       self.current_node = start_node

       # run the algorithm while the frontier still has valid states
       while not len(self.frontier) == 0:

           # dequeue the first item that was entered in the frontier
           next_state = self.frontier.pop()
           next_state_and_parent = self.frontier_with_parent.pop(0)

           # this new state is now in our graph, so turn it into a node, and add it
           #next_node = Node(parent_node=self.current_node, state=next_state,
           #                 puzzle=self.puzzle, total_cost=0)
           next_node = Node(parent_node=next_state_and_parent[1], state=next_state,
                            puzzle=self.puzzle, total_cost=0)
           self.graph.add(next_node)
           self.current_node = next_node

           # check if we have a match, if so -- we've found the end state
           if self.puzzle.goalTest(next_state):
               # Need to return the path that got us here
               print "BFS SOLUTION SEARCH PATH: "
               final_node = next_node
               path_list = [str(final_node.current_state)]

               while final_node.parentNode is not None:
                   path_list.append(str(final_node.parentNode.current_state))
                   final_node = final_node.parentNode

               path_list.reverse()
               count = 0
               for elem in path_list:
                   count += 1
                   print "Node "+str(count)+"\t->" + str(elem)
               print "----- End BFS Search Path ----"
               print "BFS METRICS:"

               print "\tTIME:   Number of Nodes Created="+str(self.num_nodes+1)
               print "\tSPACE:  Frontier Maximum Size="+str(self.frontier_max_size+1)
               print "\tSPACE:  Number of States Explored="+str(self.num_explored_states+1)

               return True

           # add the node to the explored list, if it's not a match
           self.explored.add(next_state)

           # and expand our frontier, so that it contains everything on the list of our new node
           for elem in next_node.successor_states:
               # but don't add anything that's already in frontier or explored...
                if not elem in self.explored and \
                   not elem in self.frontier:
                    self.frontier.appendleft(elem)
                    # with parent
                    state_and_parent = (elem, next_node)
                    self.frontier_with_parent.append(state_and_parent)

           # book-keeping
           # update frontier size
           if len(self.frontier) > self.frontier_max_size:
               self.frontier_max_size = len(self.frontier)
           # update explored size
           if len(self.explored) > self.num_explored_states:
               self.num_explored_states = len(self.explored)
           # update graph size
           self.num_nodes = len(self.graph)

       # If we make it this far, there was no solution
       print "BFS:  No Solutions"
       return None

