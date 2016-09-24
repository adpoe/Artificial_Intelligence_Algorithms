"""
# @author Anthony (Tony) Poerio
# @email adp59@pitt.edu
# University of Pittsburgh
# Fall 2016
# Computer Science 1571 - Artificial Intelligence
# Assignment 01
# Search Algorithm Implementations for Three Puzzle Types
#
# This File: Tests To Show That Each Search/Puzzle Type Is Functional
#
"""
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


class TestCases:

    def __init__(self):
        # initialize waterjugs tests
        self.waterjugs_puzzle = jugs.WaterJugs()
        self.waterjugs_puzzle.parseInput('test_jugs.config')
        wj_tests.WaterJugsTests()

        # initialize pathfinding tests
        self.cities_puzzle = paths.PathPlanning()
        self.cities_puzzle.parseInput('test_cities.config')
        path_tests.PathPlanningTests()

        # initialize pancakes tests
        self.pancakes_puzzle = pancakes.BurntPancakes()
        self.pancakes_puzzle.parseInput('test_pancakes1.config')
        pancake_tests.PancakeTests()

        self.big_pancakes_puzzle = pancakes.BurntPancakes()
        self.big_pancakes_puzzle.parseInput('test_pancakes2.config')



    def run_full_test_suite(self):
        # run the problem type setup tests
        # run the base case tests, make sure everything at least works on small inputs
        # run the prescribed waterjugs test
        # run the prescribed cities tests
        # run the presecribed pancakes tests
        return

    #                     #
    #    WATER JUG TESTS  #
    #                     #
    def water_jugs_test_cases(self):
        print "====== WATER JUGS TESTS ======="
        self.wj_bfs()
        self.wj_dfs()
        self.wj_iddfs()
        print "====== END JUGS TESTS ========="
        return

    def wj_bfs(self):
        bfs = breadth_first_search.BFS(self.waterjugs_puzzle)
        bfs.bfs()
        return

    def wj_dfs(self):
        dfs = depth_first_search.DFS(self.waterjugs_puzzle)
        dfs.dfs()
        return

    def wj_iddfs(self):
        iddfs = iterative_deepending_dfs.IDDFS(self.waterjugs_puzzle, 1, 1)
        iddfs.iddfs()
        return

    #                        #
    #    PATH FINDING TESTS  #
    #                        #
    def path_finding_test_cases(self):
        print "====== PATH FINDING TESTS ======="
        self.path_unicost()
        self.path_greedy()
        self.path_idastar()
        print "====== END PATH FINDING TESTS ========="
        return

    def path_unicost(self):
        uni = unicost_search.Unicost(self.cities_puzzle)
        uni.unicost()
        return

    def path_greedy(self):
        greedy = greedy_search.Greedy(self.cities_puzzle)
        greedy.greedy()
        return

    def path_idastar(self):
        idastar = idastar_search.IDAStar(self.cities_puzzle, 1, 5)
        idastar.idastar()
        return

    #                          #
    #    BURNT PANCAKES TESTS  #
    #                          #
    def pancakes_test_cases_small(self):
        print "====== BURNT PANCAKE TESTS - SMALL ======="
        puzzle = self.pancakes_puzzle
        self.pancake_astar(puzzle)
        #self.pancake_iddfs(puzzle)
        #self.pancake_idastar(puzzle)
        print "====== END >>> SMALL <<< PANCAKE TESTS ========="
        return

    def pancakes_test_cases_big(self):
        print "====== BURNT PANCAKE TESTS - BIG ======="
        puzzle = self.big_pancakes_puzzle
        self.pancake_astar(puzzle)
        #self.pancake_iddfs(puzzle)
        #self.pancake_idastar(puzzle)
        print "====== END >>> BIG <<< PANCAKE TESTS ========="
        return

    def pancake_iddfs(self, puzzle):
        iddfs = iterative_deepending_dfs.IDDFS(puzzle, 1, 5)
        iddfs.iddfs()
        return

    def pancake_astar(self, puzzle):
        astar = astar_search.AStar(puzzle)
        astar.astar()
        return

    def pancake_idastar(self, puzzle):
        idastar = idastar_search.IDAStar(puzzle, 1, 5)
        idastar.idastar()
        return