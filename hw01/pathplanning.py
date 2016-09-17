"""
# @author Anthony (Tony) Poerio
# @email adp59@pitt.edu
# University of Pittsburgh
# Fall 2016
# Computer Science 1571 - Artificial Intelligence
# Assignment 01
# Search Algorithm Implementations for Three Puzzle Types
#
# This File:  Decomposition of the Path Planning problem, so it can be solved by
#             any of our search algorithms
#
"""

from ast import literal_eval as make_tuple

"""
cities
[("Arlington",1,1), ("Berkshire",2,3), ("Chelmsford"1,5)]
"Berkshire"
"Arlington"
("Arlington", "Chelmsford", 4)
("Arlington", "Berkshire", 10)
("Berkshire", "Chelmsford", 5)
"""

#####################
#### PARSE INPUT ####
#####################
class PathPlanning:
    """ Class to model the water jugs problem
    """

    def __init__(self):
        # Constants
        self.num_cities = 0
        self.city_locations = None
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

        # ensure that we actually have jug data
        if not data_array[0] == "cities":
            print "Invalid data file"
            # return a None if we fail
            return None

        # get num jugs
        city_location_str = data_array[1]
        city_locations = make_tuple(city_location_str)
        self.num_cities = len(city_locations)

        # get jug capacities
        self.city_locations = city_locations

        # get initial state
        init_state_str = data_array[2]
        init_state_tuple = make_tuple(init_state_str)
        self.initial_state = init_state_tuple

        # get goal state
        goal_state_str = data_array[3]
        goal_state_tuple = make_tuple(goal_state_str)
        self.goal_state = make_tuple(goal_state_str)

        # set action states
        for elem in xrange(4, len(data_array)-1):
            action = data_array[elem]
            action = make_tuple(action)
            self.actions.add(action)


        return

    #            #
    # Transition #
    #            #
    def getSuccessorStates(self, current_state):
        # clear old transitions, if any
        self.transitions = set()
        successor_states = set()

        for elem in self.actions:
            if current_state in elem:
                if elem[0] == current_state:
                    # do one thing
                    new_state_and_cost = (elem[1], elem[2])
                    successor_states.add(new_state_and_cost)
                else:
                    # do another thing
                    new_state_and_cost = (elem[0], elem[2])
                    successor_states.add((new_state_and_cost))

        return successor_states

    #           #
    # Goal Test #
    #           #
    def goalTest(self, current_state):
        if current_state[0] in self.goal_state:
            return True
        else:
            return False



    #           #
    # Path Cost #
    #           #
    def getPathCost(self):
        return
