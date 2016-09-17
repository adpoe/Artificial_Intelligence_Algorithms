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
import dfs as depth_first_search
import iddfs as iterative_deepening_dfs


############################
##### MAIN ENTRY POINT #####
############################

# For cost, need to enable the getPathCosts method.... do that in the puzzle classes, abstract it
def main():
    print "Hello world!"

    # MODEL WATERJUGS
    # parse the water jugs data
    jug_puzzle = WJ.WaterJugs()
    jug_puzzle.parseInput("jugs.config")
    wj_tests.WaterJugsTests()

    print "\n\n\n ============ BREADTH FIRST SEARCH ============"
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

    print "\n\n\n ============ DEPTH FIRST SEARCH ============"
    print "\n ---- WATER JUG DFS ----"
    dfs_jugs = depth_first_search.DFS(jug_puzzle)
    dfs_jugs.dfs()
    print "\n --- PATH PLANNING DFS ---"
    dfs_paths = depth_first_search.DFS(path_puzzle)
    dfs_paths.dfs()

    print "\n\n\n ============ ITERATIVE-DEEPENING DEPTH FIRST SEARCH ============"
    print "\n ---- WATER JUG DFS ----"
    iddfs_jugs = iterative_deepening_dfs.IDDFS(jug_puzzle, max_depth=1, deepening_constant=1)
    iddfs_jugs.iddfs()
    print "\n --- PATH PLANNING DFS ---"
    iddfs_paths = iterative_deepening_dfs.IDDFS(path_puzzle, max_depth=1, deepening_constant=1)
    iddfs_paths.iddfs()

    return





if __name__ == "__main__":
    main()

