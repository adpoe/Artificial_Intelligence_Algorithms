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
import waterjugs as WJ
import pathplanning as PATH
import waterjugs_tests as wj_tests
import bfs as bread_first_search


############################
##### MAIN ENTRY POINT #####
############################
def main():
    print "Hello world!"

    # MODEL WATERJUGS
    # parse the water jugs data
    jug_puzzle = WJ.WaterJugs()
    jug_puzzle.parseInput("jugs.config")
    wj_tests.WaterJugsTests()

    print "\n ---- WATER JUG BFS ----"
    bfs = bread_first_search.BFS(jug_puzzle)
    bfs.bfs()

    # MODEL PATH-PLANNING
    path_puzzle = PATH.PathPlanning()
    path_puzzle.parseInput("cities.config")
    print "\n --- PATH PLANNING BFS ---"
    arlington_successors = path_puzzle.getSuccessorStates('Arlington')
    berkshire_successors = path_puzzle.getSuccessorStates('Berkshire')
    chelmsford_successors = path_puzzle.getSuccessorStates('Chelmsford')
    bfs_paths = bread_first_search.BFS(path_puzzle)
    bfs_paths.bfs()
    return





if __name__ == "__main__":
    main()

