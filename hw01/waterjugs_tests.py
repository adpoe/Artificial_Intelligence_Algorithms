""" Tests for the waterjugs puzzle endpoints
"""
import waterjugs as jugs

class WaterJugsTests:
    def __init__(self):
        self.WJ = jugs.WaterJugs()

        print "===== TEST WATERJUGS PUZZLE ======"
        # check that parse is okay
        self.WJ.parseInput("jugs.config")

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


        print "\nTEST 01:"
        if self.checkGetSuccessorStates() == True:
            print "\tcheckGetSuccessorStates() --> PASS\n"
        else:
            print "\tcheckGetSuccessorStates() --> FAIL\n"

        print "========== END WATERJUG TESTS ========="
        return


    def checkParse(self):
        if self.WJ.goal_state == (0,2) and \
            self.WJ.initial_state == (0,0) and \
            self.WJ.jug_capacities == (3,4) and \
            self.WJ.num_jugs == 2:
                return True
        else:
            return False

    def checkGoalTest(self):
        if self.WJ.goalTest((2,0)) == False and \
            self.WJ.goalTest((0,2)) == True:
                return True
        else:
            return False

    def checkGetSuccessorStates(self):
        init_states = self.WJ.getSuccessorStates((0,0))
        expected_init_states = set([(3,0), (0,4)])
        one_three_states = self.WJ.getSuccessorStates((1,3))
        expected_one_three_states = set([(3,3), (3,1), (1,4), (0,4), (0,3), (1,0)])
        if init_states == expected_init_states and \
            one_three_states == expected_one_three_states:
            return True
        else:
            return False


