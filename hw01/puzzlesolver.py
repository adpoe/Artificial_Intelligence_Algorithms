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

import waterjugs as WJ
import pathplanning as PATH
import pancakes as Pancakes
import waterjugs_tests as wj_tests
import bfs as bread_first_search
import dfs as depth_first_search
import iddfs as iterative_deepening_dfs
import unicost as UC
import greedy as greedy_search
import astar as astar_search
import idastar as iterative_deepening_astar
import tests as tests

############################
##### MAIN ENTRY POINT #####
############################

# For cost, need to enable the getPathCosts method.... do that in the puzzle classes, abstract it
def main():
    print "Hello world!"


    test_cases = tests.TestCases()
    print "\n\n\n"
    test_cases.water_jugs_test_cases()
    print "\n\n\n"
    test_cases.path_finding_test_cases()

    print "Finished WJ Test Cases"

    # MODEL PANCAKES
    pancake_puzzle = Pancakes.BurntPancakes()
    pancake_puzzle.parseInput("test_pancakes1.config")
    init_state = pancake_puzzle.initial_state
    successor_states = pancake_puzzle.getSuccessorStates(init_state)
    successor_state_costs = []
    for elem in successor_states:
        cost = pancake_puzzle.getPathCost(init_state, elem)
        successor_state_costs.append(cost)
    successor_state_heuristics = []
    for elem in successor_states:
        heuristic = pancake_puzzle.getHeuristic(init_state, elem)
        successor_state_heuristics.append(heuristic)

    #print "done"

    # MODEL WATERJUGS
    # parse the water jugs data
    jug_puzzle = WJ.WaterJugs()
    jug_puzzle.parseInput("jugs.config")
    #print jug_puzzle.getHeuristic((0,0),(4,2))
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
    print path_puzzle.getHeuristic(('Berkshire', 4), ('Chelmsford', 10))
    bfs_paths = bread_first_search.BFS(path_puzzle)
    bfs_paths.bfs()

    print "\n ---- PANCAKES BFS ----"
    #pancake_bfs = bread_first_search.BFS(pancake_puzzle)
    #pancake_bfs.bfs()
    print "Pancake BFS does not finish in reasonable time. We need an informed search for this one."

    print "\n\n\n ============ DEPTH FIRST SEARCH ============"
    print "\n ---- WATER JUG DFS ----"
    dfs_jugs = depth_first_search.DFS(jug_puzzle)
    dfs_jugs.dfs()
    print "\n --- PATH PLANNING DFS ---"
    dfs_paths = depth_first_search.DFS(path_puzzle)
    dfs_paths.dfs()
    print "\n --- BURNT PANCAKES DFS ---"
    #dfs_pancakes = depth_first_search.DFS(pancake_puzzle)
    #dfs_pancakes.dfs()
    print "Pancake DFS does not finish in reasonable time. We need an informed search for this one."

    print "\n\n\n ============ ITERATIVE-DEEPENING DEPTH FIRST SEARCH ============"
    print "\n ---- WATER JUG IDDFS ----"
    iddfs_jugs = iterative_deepening_dfs.IDDFS(jug_puzzle, max_depth=1, deepening_constant=1)
    iddfs_jugs.iddfs()
    print "\n --- PATH PLANNING IDDFS ---"
    iddfs_paths = iterative_deepening_dfs.IDDFS(path_puzzle, max_depth=1, deepening_constant=1)
    iddfs_paths.iddfs()
    print "\n --- BURNT PANCAKES IDDFS ---"
    #iddfs_pancakes = iterative_deepening_dfs.IDDFS(pancake_puzzle, max_depth=1, deepening_constant=1)
    #iddfs_pancakes.iddfs()
    print "Again, search space seems to big on this one for an uninformed search. I'm only seeing 4 expansions in a minute or so.\n" \
          "Beyond that, it looks like the space is growing too quickly, with each node having 11 branches."

    print "\n\n\n ============ UNICOST SEARCH ============"
    print "\n ---- WATER JUG UNICOST ----"
    unicost_jugs = UC.Unicost(jug_puzzle)
    unicost_jugs.unicost()
    print "\n --- PATH PLANNING UNICOST ---"
    unicost_paths = UC.Unicost(path_puzzle)
    unicost_paths.unicost()
    print "\n --- BURNT PANCAKES UNICOST ---"
    #unicost_pancakes = UC.Unicost(pancake_puzzle)
    #unicost_pancakes.unicost()
    print "Same here. The burnt pancake problem with our inputs is too large. "

    print "\n\n\n ============ GREEDY SEARCH ============"
    print "\n ---- WATER JUG GREEDY ----"
    greedy_jugs = greedy_search.Greedy(jug_puzzle)
    greedy_jugs.greedy()
    print "\n --- PATH PLANNING GREEDY ---"
    greedy_paths = greedy_search.Greedy(path_puzzle)
    greedy_paths.greedy()
    print "\n --- BURNT PANCAKES GREEDY ---"
    #greedy_pancakes = greedy_search.Greedy(pancake_puzzle)
    #greedy_pancakes.greedy()


    print "\n\n\n ============ A* SEARCH ============"
    print "\n ---- WATER JUG A* ----"
    astar_jugs = astar_search.AStar(jug_puzzle)
    astar_jugs.astar()
    print "\n --- PATH PLANNING A* ---"
    astar_paths = astar_search.AStar(path_puzzle)
    astar_paths.astar()
    print "\n --- BURNT PANCAKES A* ---"
    #astar_pancakes = astar_search.AStar(pancake_puzzle)
    #astar_pancakes.astar()


    print "\n\n\n ============ Iterative Deepening A* SEARCH ============"
    print "\n ---- WATER JUG Iterative Deepening A* ----"
    idastar_jugs = iterative_deepening_astar.IDAStar(jug_puzzle, max_depth=4, deepening_constant=4)
    idastar_jugs.idastar()
    print "\n --- PATH PLANNING Iterative Deepening A* ---"
    idastar_paths = iterative_deepening_astar.IDAStar(path_puzzle, max_depth=5, deepening_constant=5)
    idastar_paths.idastar()
    print "\n --- BURNT PANCAKES Iterative Deepening A* ---"
    #idastar_pancakes = iterative_deepening_astar.IDAStar(pancake_puzzle, max_depth=5, deepening_constant=5)
    #idastar_pancakes.idastar()

    return



if __name__ == "__main__":
    main()

