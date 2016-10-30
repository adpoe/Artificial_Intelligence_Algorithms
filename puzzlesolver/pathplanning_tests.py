""" Tests for the pathplanning puzzle endpoints
"""
import pathplanning as pplan

class PathPlanningTests:
    def __init__(self):
        self.paths = pplan.PathPlanning()

        print "===== TEST PathPlanning PUZZLE ======"
        # check that parse is okay
        self.paths.parseInput("test_cities.config")

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

        print "========== END PATHPLANNING TESTS ========="
        return


    def checkParse(self):
        if self.paths.goal_state == "C44" and \
           self.paths.initial_state == "C00" and \
           self.paths.num_cities == 25:
                return True
        else:
            return False

    def checkGoalTest(self):
        if self.paths.goalTest(("C10", 5)) == False and \
           self.paths.goalTest(("C44", 6)) == True:
                return True
        else:
            return False

    # Use 'C11'..... that's where it's faltering
    def checkGetSuccessorStates(self):
        init_states = self.paths.getSuccessorStates("C11")
        expected_init_states = set([('C01',7), ('C21',5), ('C10',5),('C12', 5),
                                    ('C00',4), ('C22', 8),('C02', 1), ('C20',1)])
        set_difference = init_states - expected_init_states
        if len(set_difference) == 0:
            return True
        else:
            return False

    def checkGetPathCosts(self):
        current_state = 'C01'
        successor_state = 'C11'
        path_cost = self.paths.getPathCost(current_state, successor_state)
        if path_cost == 1:
            return True
        else:
            return False

    def checkGetHeuristic(self):
        heuristic = self.paths.getHeuristic(('C00', 4), ('C11', 10))
        # checking for a difference within one-tenth, because these are Real, floating point numbers,
        # so we'll get weird errors checking strictly for equality (calculations may be off at some small magnitude)
        if heuristic - 4.24 < 0.1:
            return True
        else:
            return False


