"""
#
# @author Anthony (Tony) Poerio
# @email adp59@pitt.edu
# University of Pittsburgh
# Fall 2016
# Computer Science 1571 - Artificial Intelligence
# Assignment 01
# Search Algorithm Implementations for Three Puzzle Types
#
# This File:  Iterative Deepening - Depth First Search  (IDDFS)
#
"""

# Idea:  Use DFS, and if node.depth >= specified depth.... stop the search, and run a new one from the beginning,
#        But with a higher value for depth

# TODO: Enable COSTS --> Some conditional, otherwise it's 1


import collections


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
   def __init__(self, puzzle, max_depth, num_nodes_created=0, frontier_max_size=0, num_states_explored=0):
       # data storage
       self.explored = set()
       self.puzzle = puzzle
       self.graph = set()
       self.max_depth = max_depth

       # careful here...
       self.current_node = None
       self.frontier_with_parent = []
       self.has_more_nodes = False

       # time/space data
       self.solution_path = []
       self.num_nodes = num_nodes_created
       self.frontier_max_size = frontier_max_size
       self.num_explored_states = num_states_explored

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



           """ DEPTH CHECK """
           if self.current_node.depth > self.max_depth:
               self.has_more_nodes = True
               continue
           """ END DEPTH CHECK """

           #######################################
           ####### KNOWN SAFE DEPTH CHECK ########
           #######################################
           # but potentially incorrect
           """ DEPTH CHECK """
           #if self.current_node.depth > self.max_depth:
           #    return False
           """ END DEPTH CHECK """



           # check if we have a match, if so -- we've found the end state
           if self.puzzle.goalTest(next_state_and_parent[0]):
               # Need to return the path that got us here
               print "IDDFS SOLUTION SEARCH PATH: "
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
               print "----- End IDDFS Search Path ----"
               print "IDDFS METRICS:"

               print "\tTIME:   Number of Nodes Created="+str(self.num_nodes+1)
               print "\tSPACE:  Frontier Maximum Size="+str(self.frontier_max_size+1)
               print "\tSPACE:  Number of States Explored="+str(self.num_explored_states+1)

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

       """ CHECK FOR ITERATIVE DEEPENING """
       # Nothin on frontier anymore, but are there any more deeper nodes?
       # If Yes, then we return False --> Which means need to do iterative deepening
       if self.has_more_nodes == True:
           return False
       """"   END CHECK FOR ITERATIVE DEEPENING """

       # If we make it this far, there was no solution
       print "IDDFS:  No Solutions"
       return None


class IDDFS:
    def __init__(self, puzzle, max_depth, deepening_constant):
        self.DFS = DFS(puzzle, max_depth) # dfs with our puzzle and max depth
        # get the current node in our dfs and check its depth.... make a whole new dfs if we go over
        # and increment the depth by 3 or something
        self.max_depth = max_depth
        self.deepening_constant = deepening_constant
        self.puzzle = puzzle
        self.times_expanded = 0

    def iddfs(self):
        # Note... may need to report on TOTAL SIZE and SPACE for this..
        # So need to grab that data from the DFS each time it fails, before restarting it.
        # get nodes made and pass it back in every time as optional arg with regular value of zero
        # same thing with max frontier size, and num states explored...
        # Note that these numbers are cumulative...
        while self.DFS.dfs() == False:
            print "Expanding IDDFS"
            self.times_expanded += 1

            # grow the max depth by our deepening constant
            self.max_depth += self.deepening_constant

            # get data collected so far on the search
            nodes_created = self.DFS.num_nodes
            frontier_max = self.DFS.frontier_max_size
            count_explored_states = self.DFS.num_explored_states

            # pass our new data back into the search
            self.DFS = DFS(self.puzzle, self.max_depth,
                           num_nodes_created=nodes_created,
                           frontier_max_size= frontier_max,
                           num_states_explored= count_explored_states)
        print "\t\tEXPANDED THE SEARCH SPACE: " + str(self.times_expanded) + " TIMES"
