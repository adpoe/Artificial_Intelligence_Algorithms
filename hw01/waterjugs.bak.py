"""
# @author Anthony (Tony) Poerio
# @email adp59@pitt.edu
# University of Pittsburgh
# Fall 2016
# Computer Science 1571 - Artificial Intelligence
# Assignment 01
# Search Algorithm Implementations for Three Puzzle Types
#
# This File:  Decomposition of the Water Jugs problem, so it can be solved by
#             any of our search algorithms
#
"""
from ast import literal_eval as make_tuple

#####################
#### PARSE INPUT ####
#####################
class WaterJugs:
    """ Class to model the water jugs problem
    """

    def __init__(self):
        # Constants
        self.num_jugs = 0
        self.jug_capacities = None
        self.initial_state = None
        self.goal_state = None
        self.transitions = set()

        # Variables
        self.current_state = None



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

        # ensure that we actually have jug data
        if not data_array[0] == "jugs":
            print "Invalid data file"
            # return a None if we fail
            return None

        # get num jugs
        jug_capacity_str = data_array[1]
        jug_capacities = make_tuple(jug_capacity_str)
        self.num_jugs = len(jug_capacities)

        # get jug capacities
        self.jug_capacities = jug_capacities

        # get initial state
        init_state_str = data_array[2]
        init_state_tuple = make_tuple(init_state_str)
        self.initial_state = init_state_tuple

        # get goal state
        goal_state_str = data_array[3]
        goal_state_tuple = make_tuple(goal_state_str)
        self.goal_state = make_tuple(goal_state_str)

        # set current state
        self.current_state = list(init_state_tuple)

        # set transitions
        self.getSuccessorStates()

        return


    #            #
    # Transition #
    #            #
    """ Generate all transitions from the actions we've stored...
        completely emptying and partially emptying
    """
    # Fill, Dump, Transfer
    # call this each time with the current state and fill actions

    def getSuccessorStates(self):
        # run each transition function
        self.createFillingActions()
        self.createDumpingActions()
        self.createTransferActions()
        self.createDumpAndTransfer()
        return

    #         #
    # Actions #
    #         #

    def createFillingActions(self):
        # iterate through jug capacities and find the values of each
        for index in xrange(0, len(self.jug_capacities)):

            # build an array for each action, just find the values
            action_array = [0] * len(self.jug_capacities)
            max_amount = self.jug_capacities[index]
            current_amount = self.current_state[index]
            fill_amount = min(max_amount, max_amount-current_amount)
            action_array[index] = fill_amount

            # transform our array to a tuple
            action_tuple = tuple(action_array)

            # ensure we're not adding a state that will take us nowhere
            if not all(v == 0 for v in action_tuple):
                # add the tuple to the the actions list
                self.transitions.add(action_tuple)

        return


    def createDumpingActions(self):
        # iterate through jug capacities and find the values of each
        for index in xrange(0, len(self.jug_capacities)):

            # build an array for each action, just find the negative values
            action_array = [0] * len(self.jug_capacities)
            max_amount = self.jug_capacities[index]
            current_amount = self.current_state[index]
            dump_amount = min(max_amount, current_amount)
            action_array[index] = -(dump_amount)

           # action_array[index] = -(self.jug_capacities[index])

            # transform our array to a tuple
            action_tuple = tuple(action_array)

            # ensure we're not adding a state that will take us nowhere
            if not all(v == 0 for v in action_tuple):
                # add the tuple to the the actions list
                self.transitions.add(action_tuple)

        return

    def createTransferActions(self):
        # iterate through and then for 0->(index-1) and index+1->end
        # fill with +3 in one and -3 in the other
        # and then do another one with a variable in it?
        # could be same logic... but up until the index value in self.jug_capacities
        # and minus the current value....

        for origin_index in xrange(0, len(self.jug_capacities)):

            # build an array for each action
            action_array = [0] * len(self.jug_capacities)

            for transfer_index in xrange(0, len(self.jug_capacities)):

                # compute the amount to transfer
                amount_at_origin = self.current_state[origin_index]
                amount_at_dest = self.current_state[transfer_index]
                max_at_origin = self.jug_capacities[origin_index]
                max_at_dest = self.jug_capacities[transfer_index]

                # where d=min(jug_capacities[index],
                transfer_amount = min(amount_at_origin, max_at_dest-amount_at_dest)

                # make the transfer
                if not origin_index == transfer_index:
                    action_array[origin_index] -= transfer_amount
                    action_array[transfer_index] += transfer_amount

                # transform our array to a tuple
                action_tuple = tuple(action_array)

                # add the tuple to the the actions list if not already contained
                if action_tuple not in self.transitions and \
                        not all(v == 0 for v in action_tuple):
                    self.transitions.add(action_tuple)

        return

    def createDumpAndTransfer(self):
        for origin_index in xrange(0, len(self.jug_capacities)):

            # build an array for each action
            action_array = [0] * len(self.jug_capacities)

            for transfer_index in xrange(0, len(self.jug_capacities)):

                # compute the amount to transfer
                amount_at_origin = self.current_state[origin_index]
                amount_at_dest = self.current_state[transfer_index]
                max_at_origin = self.jug_capacities[origin_index]
                max_at_dest = self.jug_capacities[transfer_index]

                # where d=min(jug_capacities[index],
                transfer_amount = amount_at_origin

                # make the transfer
                if not origin_index == transfer_index:
                    action_array[origin_index] -= transfer_amount
                    action_array[transfer_index] += transfer_amount

                # transform our array to a tuple
                action_tuple = tuple(action_array)

                # add the tuple to the the actions list if not already contained
                if action_tuple not in self.transitions and \
                        not all(v == 0 for v in action_tuple):

                    self.transitions.add(action_tuple)

        return


    #           #
    # Goal Test #
    #           #
    def goalTest(self):
        if self.current_state == self.goal_state:
            return None

        return


    #           #
    # Path Cost #
    #           #
    def getPathCost(self):
        return

