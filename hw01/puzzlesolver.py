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


import tests as tests
import confirmation_tests as confirmations
############################
##### MAIN ENTRY POINT #####
############################

# For cost, need to enable the getPathCosts method.... do that in the puzzle classes, abstract it
def main():

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

