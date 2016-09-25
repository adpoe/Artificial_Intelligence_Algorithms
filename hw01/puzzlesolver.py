"""
# @author Anthony (Tony) Poerio
# @email adp59@pitt.edu
# University of Pittsburgh
# Fall 2016
# Computer Science 1571 - Artificial Intelligence
# Assignment 01
# Search Algorithm Implementations for Three Puzzle Types
#
# Notes: This is the main entry point for this program
#
"""

# There is some randomness in how the data is explored because using the set() data structure in a few places,
# principally at create of successor states.

# import problem types
import waterjugs as jugs
import pathplanning as paths
import pancakes as pancakes


# import tests to ensure problem types are working correctly
import waterjugs_tests as wj_tests
import pathplanning_tests as path_tests
import pancakes_tests as pancake_tests

# import search types
import bfs as breadth_first_search
import dfs as depth_first_search
import iddfs as iterative_deepending_dfs
import unicost as unicost_search
import greedy as greedy_search
import idastar as idastar_search
import astar as astar_search

# import tests
import tests as tests
import confirmation_tests as confirmations

# import the system library, so we can grab cmd line args
import sys

############################
##### MAIN ENTRY POINT #####
############################

def main():
    # get number of args passed in via command line
    num_args = len(sys.argv)

    # ensure we have valid input
    if num_args == 1:
        print "Usage: 'python puzzlesolver.py [config_filename] [search_algorithm_name] [optional: heuristic] "
        print "     to run test suite:  'python puzzlesolver.py -t'"
        return
    # check if we are running the test suite
    if sys.argv[1] == "-t":
        # run the test suite
        runTests()
        return

    # if we get this far, then we are running a specific algorithm
    if num_args < 3 or num_args > 4:
        print "Usage: 'python puzzlesolver.py [config_filename] [search_algorithm_name] [optional: heuristic] "
        print "     to run test suite:  'python puzzlesolver.py -t'"


    # otherwise, parse the args, and
    # take 2 input args... plus an optional one....
    # FIRST ARG --> a configuration file
    config_file = sys.argv[1]
    # SECOND ARG --> Keyword to specify which algorithm to use: bfs, dfs, iddfs, unicost, greedy, astar, diastar
    algorithm = sys.argv[2]
    # THIRD ARG --> Heuristic
    if num_args == 4:
        heuristic = sys.argv[3]

    """ parse the config file based on what's in the first line"""
    # do that here.... need to write a function just to get first line and then call the appropriate
    # parse based on what's sent in

    # grab all the data and store it as a single string
    with open(config_file, 'r') as f:
        data_as_string = f.read()

    # split the data we've just read on newline, so we can index into it
    data_array = data_as_string.split("\n")

    # ensure that we actually have pancake data
    puzzle_name = data_array[0]
    puzzle = None
    # check which puzzle we have and open the correct file for it
    if "jugs" in puzzle_name:
         # then it's the jug puzzle
        puzzle = jugs.WaterJugs()
        puzzle.parseInput(config_file)
    elif "pancake" in puzzle_name:
        # then it's burnt pancakes puzzle
        puzzle = pancakes.BurntPancakes()
        puzzle.parseInput(config_file)
    elif "path" in puzzle:
        # then it's path planning
        puzzle = paths.PathPlanning()
        puzzle.parseInput(config_file)
    else:
        # else it's nothing, and we have an invalid file
        print "Invalid data file. Please make sure your file has the correct format."
        return


    # determine which algorithm to initialize
    if algorithm == "bfs":
        print "---- START BFS ----"
        search = breadth_first_search.BFS(puzzle)
        search.bfs()
        print "---- END BFS ----"

    elif algorithm == "dfs":
        print "---- START DFS ----"
        search = depth_first_search.DFS(puzzle)
        search.dfs()
        print "---- END DFS ----"

    elif algorithm == "iddfs":
        print "---- START IDDFS ----"
        search = iterative_deepending_dfs.IDDFS(puzzle, 1, 1)
        search.iddfs()
        print "---- END IDDFS ----"

    elif algorithm == "unicost":
        print "----- START UNICOST ----"
        search = unicost_search.Unicost(puzzle)
        search.unicost()
        print "----- END UNICOST ----"

    elif algorithm == "greedy":
        print "----- START GREEDY -----"
        search = greedy_search.Greedy(puzzle)
        search.greedy()
        print "----- END GREEDY -----"

    elif algorithm == "astar":
        print "----- START ASTAR -----"
        search = astar_search.AStar(puzzle)
        search.astar()
        print "----- END ASTAR -----"

    elif algorithm == "idastar":
        print "----- START IDASTAR -----"
        search = idastar_search.IDAStar(puzzle, 5)
        search.idastar()
        print "----- END IDASTAR -----"
    else:
        print "Invalid algorithm name."


    return

def runTests():
    ## Maybe pass in -t to test...
    #### Below here needs to be a separate testing function.... need program to follow specifications outlined

    ####################################################
    ##### CONFIRM EVERYTHING WORKS ON SMALL INPUTS #####
    ####################################################
    """ Tests to confirm that **ALL 3-puzzles** run correctly in all search algorithms,
        using small inputs.
    """
    print "#####################################\n" \
          "##### BEGIN CONFIRMATION TESTS ######\n" \
          "#####################################\n"
    confirm_everything_works = confirmations.ConfirmationTests()
    confirm_everything_works.confirmAllPuzzlesRunOnAllSearches()
    print "\n####################################\n" \
          "####################################\n" \
          "###### END CONFIRMATION TESTS ######\n" \
          "####################################\n" \
          "####################################\n" \


    test_cases = tests.TestCases()
    print "\n\n\n"
    test_cases.water_jugs_test_cases()
    print "\n\n\n"
    test_cases.path_finding_test_cases()
    print "\n\n\n"
    test_cases.pancakes_test_cases_small()
    test_cases.pancakes_test_cases_big()

    return



if __name__ == "__main__":
    main()

