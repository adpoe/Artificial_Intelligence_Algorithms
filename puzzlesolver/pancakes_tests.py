""" Tests for the pathplanning puzzle endpoints
"""
import pancakes as pancakes

class PancakeTests:
    def __init__(self):
        self.pancakes = pancakes.BurntPancakes()

        print "===== TEST PANCAKES PUZZLE ======"
        # check that parse is okay
        self.pancakes.parseInput("test_pancakes1.config")

        print "\nTEST 01:"
        if self.checkParse() == True:
            print "\tcheckParse() --> PASS\n"
        else:
            print "\tcheckParse() --> FAIL\n"

        print "\nTEST 02:"
        if self.checkGoalTest() == True:
            print "\tcheckGoalTest() --> PASS\n"
        else:
            print "\tcheckGoalTest() --> FAIL\n"


        print "\nTEST 03:"
        if self.checkGetSuccessorStates() == True:
            print "\tcheckGetSuccessorStates() --> PASS\n"
        else:
            print "\tcheckGetSuccessorStates() --> FAIL\n"


        print "\nTEST 04:"
        if self.checkGetPathCosts() == True:
            print "\tcheckGetPathCosts() ) --> PASS\n"
        else:
            print "\tcheckGetPathCosts()  --> FAIL\n"

        print "\nTEST 05:"
        if self.checkGetHeuristic() == True:
            print "\tcheckGetHeuristic() ) --> PASS\n"
        else:
            print "\tcheckGetHeuristic()  --> FAIL\n"

        print "========== END PANCAKES TESTS ========="
        return


    def checkParse(self):
        if self.pancakes.goal_state == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) and \
           self.pancakes.initial_state == (-1, -11, -3, -6, -9, -4, -7, -10, -5, -8, -2) and \
           self.pancakes.num_pancakes == 11:
                return True
        else:
            return False

    def checkGoalTest(self):
        if self.pancakes.goalTest((1, 2, 3, 4, 5, 6, 7, -8, 9, 10, 11)) == False and \
           self.pancakes.goalTest((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) == True:
                return True
        else:
            return False

    # Use 'C11'..... that's where it's faltering
    def checkGetSuccessorStates(self):
        init_states = self.pancakes.getSuccessorStates((-1, -11, -3, -6, -9, -4, -7, -10, -5, -8, -2))
        expected_init_states = {
                                    (1, -11, -3, -6, -9, -4, -7, -10, -5, -8, -2),  # flip 1st
                                    (11, 1, -3, -6, -9, -4, -7, -10, -5, -8, -2),   # flip 2nd
                                    (3, 11, 1, -6, -9, -4, -7, -10, -5, -8, -2),    # flip 3rd
                                    (6, 3, 11, 1, -9, -4, -7, -10, -5, -8, -2),     # flip 4th
                                    (9, 6, 3, 11, 1, -4, -7, -10, -5, -8, -2),      # flip 5th
                                    (4, 9, 6, 3, 11, 1, -7, -10, -5, -8, -2),       # flip 6th
                                    (7, 4, 9, 6, 3, 11, 1, -10, -5, -8, -2),        # flip 7th
                                    (10, 7, 4, 9, 6, 3, 11, 1, -5, -8, -2),         # flip 8th
                                    (5, 10, 7, 4, 9, 6, 3, 11, 1, -8, -2),          # flip 9th
                                    (8, 5, 10, 7, 4, 9, 6, 3, 11, 1, -2),           # flip 10th
                                    (2, 8, 5, 10, 7, 4, 9, 6, 3, 11, 1)             # flip 11th
                                } # set literal
        set_difference = init_states - expected_init_states
        if len(set_difference) == 0:
            return True
        else:
            return False

    def checkGetPathCosts(self):
        current_state = (-1, -11, -3, -6, -9, -4, -7, -10, -5, -8, -2)
        successor_state = (2, 8, 5, 10, 7, 4, 9, 6, 3, 11, 1)
        path_cost = self.pancakes.getPathCost(current_state, successor_state)
        if path_cost == 1:
            return True
        else:
            return False

    def checkGetHeuristic(self):
        heuristic = self.pancakes.getHeuristic((-1, -11, -3, -6, -9, -4, -7, -10, -5, -8, -2), (2, 8, 5, 10, 7, 4, 9, 6, 3, 11, 1))
        # checking for a difference within one-tenth, because these are Real, floating point numbers,
        # so we'll get weird errors checking strictly for equality (calculations may be off at some small magnitude)

        if heuristic == 6:
            return True
        else:
            return False


