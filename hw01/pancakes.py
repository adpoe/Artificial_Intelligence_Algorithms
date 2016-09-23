"""
# @author Anthony (Tony) Poerio
# @email adp59@pitt.edu
# University of Pittsburgh
# Fall 2016
# Computer Science 1571 - Artificial Intelligence
# Assignment 01
# Search Algorithm Implementations for Three Puzzle Types
#
# This File:  Burnt Pancake Problem Decomposition and API Creation
#
"""

# Goal: Sort stack so that they are in order from largest (at bottom) --> smallest (at top)
# Actions:  Stick spatula into stack and flip all pancakes above it
# I.e. [3 1 2 5 4] --> [2 1 3 5 4]  (flip between 2 and 5)
#
# BURNT pancake problem:  Distinguish between top and bottom of pancakes (bottoms burnt)
# ID bottom of pancakes with a negative number
# I.e  [3 -1 2 5 4] --> the -1 size pancake has burnt side up
# Flipping between 2 and 5 again, we get:  [3 -1 2 5 4] --> [-2 1 -3 5 4]
#    - Basically, change sign for everything the flipping range

# Read from .config
# Line 1 --> Keyword pancakes, tells us it's the pancake problem
# Line 2 --> Init state i.e. (3, -1, 2, 5, 4)
# Line 3 --> Goal state i.e. (1,2,3,4,5)

# So, transition state are:
# - for every elem in pancakes tuple, reverse the the sublist up until that point,
#   and flip sign of every element in it... takes a minute


from ast import literal_eval as make_tuple
import math


#####################
#### PARSE INPUT ####
#####################
class BurntPancakes:
    """ Class to model the burnt pancake problem
    """

    def __init__(self):
        # Constants
        self.num_pancakes = 0
        self.initial_state = None
        self.goal_state = None
        self.actions = set()
        self.graph = set()
        self.transitions = set()



    def parseInput(self, file_name_string):
        """
        Parse the input data and fill the class variables in init
        :param file_name_string:
        :return: void
        """

        # grab all the data and store it as a single string
        with open(file_name_string, 'r') as f:
            data_as_string = f.read()

        # split the data we've just read on newline, so we can index into it
        data_array = data_as_string.split("\n")

        # ensure that we actually have pancake data
        if not data_array[0] == "pancakes":
            print "Invalid data file"
            # return a None if we fail
            return None

        # get num pancakes
        pancake_starting_state_str = data_array[1]
        starting_pancakes = make_tuple(pancake_starting_state_str)
        self.num_pancakes = len(starting_pancakes)

        # get initial state
        init_state_str = data_array[1]
        init_state_tuple = make_tuple(init_state_str)
        self.initial_state = init_state_tuple

        # get goal state
        goal_state_str = data_array[2]
        goal_state_tuple = make_tuple(goal_state_str)
        self.goal_state = make_tuple(goal_state_str)

        return

    #            #
    # Transition #
    #            #
    def getSuccessorStates(self, current_state):
        # clear old transitions, if any
        self.transitions = set()
        successor_states = set()

        # reverse the sublist at every index from 0->(n-1)
        # and flip the sign
        for index in range(1, len(current_state)+1):
            # start by grabbing the tuple indices from 0->index
            sublist_front = list(current_state[:index])
            sublist_back = list(current_state[index:])

            # then reverse the front sublist we've just grabbed,
            # since we are flipping it, end-over-end
            sublist_front.reverse()

            sublist_flipped = []
            # now, change the sign of every element in sublist front
            for elem in sublist_front:
                elem = elem * -1
                sublist_flipped.append(elem)
            # concat our flipped front with old back
            successor_list = sublist_flipped + sublist_back
            # cast back to a tuple
            successor_tuple = tuple(successor_list)
            # add it to the successor states
            #print len(successor_tuple)
            assert len(successor_tuple) == self.num_pancakes
            successor_states.add(successor_tuple)
            # and keep on keepin on.

        return successor_states

    #           #
    # Goal Test #
    #           #
    def goalTest(self, current_state):
        if current_state == self.goal_state:
            return True
        else:
            return False



    #           #
    # Path Cost #
    #           #
    def getPathCost(self, current_state, successor_state):
        """
        # Define 'cost' as total number of pancakes flipped

        # to find the cost, we need to figure out how many pancakes have been flipped,
        # just by looking at difference between current state and successor state

        # to do this, first subtract the state tuples, element-wise to find their differences
        state_differences = tuple(x-y for x, y in zip(current_state, successor_state))

        # then, find the LAST index at which we have a nonzero value
        # that pancake must have been flipped
        last_nonzero_index = 0
        for index in range(0, len(state_differences)):
            # store the indices which are not == 0,
            # because they don't have same value as before
            if not state_differences[index] == 0:
                # we are iterating monotonically, so the last value we see that isn't == 0..
                # will be the last nonzero index, and hence the number of pancakes that were flipped
                last_nonzero_index = index

        cost = last_nonzero_index

        return cost
        """
        # the path cost here is constant. Every flip is 1 flip.
        return 1

    #           #
    # Heuristic #
    #           #
    # Heuristic idea from: https://www.aaai.org/ocs/index.php/SOCS/SOCS11/paper/viewFile/4013/4360
    def getHeuristic(self, current_state, successor_state):
        """
        # the heuristic is the value of pancake at the top of the stack - 1
        # because we know we need a flip of that size to move the pancake into position
        # Idea from:  https://inst.eecs.berkeley.edu/~cs188/fa11/section_handouts/section2soln.pdf
        """
        heuristic = successor_state[0] - 1
        # we want to favor positive-side up, so if we have negative value up front, add one and double it
        if heuristic <= 0:
            heuristic += 1
            heuristic *= 2

        # this gives a separate value for each and every successor state, which I like,
        # and that's why I've chosen it.
        return heuristic

        #return self.getLargesPancakeOutOfPosition(current_state,successor_state)

    def getLargesPancakeOutOfPosition(self, current_state, successor_state):
        largest = 0
        for index in range(0, len(successor_state)):
            if successor_state[index] == self.goal_state[index]:
                continue
            else:
                if abs(largest) < abs(successor_state[index]):
                    largest = abs(successor_state[index])

        if largest == 0:
            print "Largest == 0: " + str(successor_state)

        return largest
