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
    #bfs = bread_first_search.BFS(jug_puzzle)

    return





if __name__ == "__main__":
    main()

