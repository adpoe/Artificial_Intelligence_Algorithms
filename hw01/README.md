# Puzzlesolver
* @author Anthony (Tony) Poerio
* University of Pittsburgh
* CS1571 - Artificial Intelligence
* Prof. Rebecca Hwa
* Fall 2016
* Homework #01

## Overview
Puzzlesolver is an Artificial Intelligence project whose purpose to solve **any** abstract puzzle using one of SIX search algorithms.

The algorithms implemented are:

**Uninformed Search**
* BFS
* DFS
* IDDFS
* UNICOST

**Informed Search**
* Greedy
* A-Star
* IDA-Star

**The puzzle types currently supported are:**
* Water Jugs
* Path-finding
* Burnt Pancakes

## Architecture

Puzzlesolver can solve any puzzle type that implements the following functions, which serve as the endpoints that each search algorithm uses:
* getSuccessorStates() - Stores all successor states to the current state in a set()
* getPathCost() - Gets the path cost of the state passed into it
* getHeuristic() - Gets the cost of a user-defined heuristic

These are the only endpoints touched by search algorithms, so as long as the puzzle types implement them in an internally consistent way, the search algorithms can solve the puzzle.


## Getting Started

To get started, run the git clone command on this repository, and use the following commands to test each puzzle type/algorithm.
Abstractly:
```
    python puzzlesolver.py [config_filename] [search_algorithm_name] [optional: heuristic]
```

Specifically:

BFS
```
    python puzzlesolver.py test_jugs.config bfs
```

DFS
```
    python puzzlesolver.py test_jugs.config dfs
```

IDDFS
```
    python puzzlesolver.py test_jugs.config iddfs
```

UNICOST
```
    python puzzlesolver.py test_cities.config unicost
```

GREEDY
```
    python puzzlesolver.py test_cities.config greedy
```

ASTAR
```
    python puzzlesolver.py test_pancakes1.config astar
```

IDASTAR
```
    python puzzlesolver.py test_cities.config astar
```


### Notes
* This project supports use of an optional third argument to specify a heuristic. The program will run if a 3rd argument is passed in, but right now each puzzle type only supports a single heuristic, so the 3rd argument will have no effect.
* I've created my own config file to test that the Burnt Pancake problem works in principle for all search algorithms. The file is included in this repo, and it is named: 'small_pancakes.config'
    - The ONLY version of the Burnt Pancake problem that completes for the larger provided inputs is the A-Star algorithm for 'test_pancakes1.config'. The others take more than 30 minutes to complete, so I did not wait them out.


### Prerequisities

This project depends upon Python v. 2.7.8

You must also have the config files you intend to read from in the same directory as the source code

## Running the tests

This program is fully covered with automated tests. To run the suite, simply use this command.

```
python puzzlesolver.py -t
```
### What's being tested

Upon running the test suite, you will see the following outputs:
* Confirmation tests --> showing that every puzzle type works for every search type (small inputs).
* Tests for each puzzle type, showing that each API endpoint works as expected.
* Tests for the **jugs puzzle type**, run on the *test_jugs.config* file, for the 'dfs', 'bfs', and 'iddfs' search algorithms.
* Tests for the **path-finding puzzle type**, run on the *test_cities.config* file, for the 'unicost', 'greedy', and 'astar' search algorithms.
* Tests for the **pancakes puzzle** type, run on the *test_pancakes1.config* file and then the *test_pancakes2.config* file. For the 'iddfs', 'astar', and 'idastar' search algorithms.

## Transcripts
Transcripts can be found in the "transcipts" folder

## Report
The report for this project can be found in the file named: "REPORT_CS1571_HW01_ADP59.pdf"

## Data
I've stored all the data I collected and graphs I created in an excel file named "Algorithm_Data.xlsx"

## Built With

* Python v. 2.7.8
* PyCharm

## Acknowledgments

* Project done for Rebecca Hwa's Artificial Intelligence class at the University of Pittsburgh
* The heuristic used for the Burnt Pancakes problem was take from this paper, under the heading 'Gap Heuristic': https://www.aaai.org/ocs/index.php/SOCS/SOCS11/paper/viewFile/4013/4360 
    - I tried a few other heuristics for this problem, but this was the only one that had any success.
