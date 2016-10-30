"""
# @author Anthony (Tony) Poerio
# @email adp59@pitt.edu
# University of Pittsburgh
# Fall 2016
# Computer Science 1571 - Artificial Intelligence
# Assignment 01
# Search Algorithm Implementations for Three Puzzle Types
#
# This File:  Depth First Search  (DFS)
#
"""
# make tree search instead of graph search, just look up 1 parent..
# then use this to create the CostLimitedDFS... with a STACK inside IDA*, instead of what's already there.
# IDA* isn't exactly an iterative deepening A*, it's a repeated cost-limited-dfs



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
        self.cost = total_cost



class DFS:
   def __init__(self, puzzle):
       #self.frontier = collections.deque()
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

   def dfs(self):
       # create a node for the initial state, this is our entry point on the graph
       start_node = Node(parent_node=None, state=self.puzzle.initial_state,
                         puzzle=self.puzzle, total_cost=0)
       self.graph.add(start_node)
       #self.frontier.extendleft(start_node.successor_states)
       for elem in start_node.successor_states_with_parent:
            self.frontier_with_parent.append(elem)

       # store start_node as parent_node, so we can create nodes as we proceed
       self.current_node = start_node

       # run the algorithm while the frontier still has valid states
       while not len(self.frontier_with_parent) == 0:

           # dequeue the first item that was entered in the frontier
           next_state_and_parent = self.frontier_with_parent.pop()

           # this new state is now in our graph, so turn it into a node, and add it...
           # Allow for adding costs by storing it as the 3rd value in our tuple, if needed
           # Not sure how to do this yet...
           node_cost = 0

           next_node = Node(parent_node=next_state_and_parent[1], state=next_state_and_parent[0],
                            puzzle=self.puzzle, total_cost=node_cost)
           self.graph.add(next_node)
           self.current_node = next_node

           # check if we have a match, if so -- we've found the end state
           if self.puzzle.goalTest(next_state_and_parent[0]):
               # Need to return the path that got us here
               print "DFS SOLUTION SEARCH PATH: "
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
               print "----- End DFS Search Path ----"
               print "DFS METRICS:"

               print "\tTIME:   Number of Nodes Created="+str(self.num_nodes+1)
               print "\tSPACE:  Frontier Maximum Size="+str(self.frontier_max_size+1)
               #print "\tSPACE:  Number of States Explored="+str(self.num_explored_states+1)

               return True

           # add the node to the explored list, if it's not a match
           self.explored.add(next_state_and_parent[0])

           # get all the frontier states, alone
           frontier_states = []
           for pair in self.frontier_with_parent:
               state = pair[0]
               frontier_states.append(state)

           # and expand our frontier, so that it contains everything on the list of our new node
           for elem in next_node.successor_states:
               # but don't add anything that's already in frontier or explored...
                if not elem in self.explored and \
                   not elem in frontier_states:
                    # self.frontier.appendleft(elem)
                    # with parent
                    cost = next_node.cost
                    state_and_parent = (elem, next_node, cost)
                    self.frontier_with_parent.append(state_and_parent)

           # book-keeping
           # update frontier size
           if len(frontier_states) > self.frontier_max_size:
               self.frontier_max_size = len(frontier_states)
           # update explored size
           if len(self.explored) > self.num_explored_states:
               self.num_explored_states = len(self.explored)
           # update graph size
           self.num_nodes = len(self.graph)

       # If we make it this far, there was no solution
       print "DFS:  No Solutions"
       return None

