# Word ladder coding challenge solution

This project is intented to solve the word ladder challenge.
The solution given here is written in Python and offers a command line tool to the end user in order to pass the start word and the end word of his/her choice.


## Getting Started


### Deliverables

* **run.py** - Entrypoint of code execution
* **resources folder** - Contains configuration file(s) as well as the dictionary
* **resources/config.ini** - Configuration file that provides the path to the desired dictionary
* **resources/dictionary.txt** - The dictionary downloaded from [here](https://gist.github.com/paulcc/3799331)
* **solution folder** - The entrypoint folder of the solution package resides here
* **solution/__init__.py** - Contains the command line tool implementation 
* **solution/handlers folder** - The handlers (modules) used to solve the challenge
* **solution/handlers/__init__.py** - Empty file; required to make Python treat directories as a package
* **solution/OutputHandler.py** - Class to handle the input(s) from the user and the output of the program
* **solution/ConfigHandler.py**- Class to handle the config.ini files
* **solution/FileHandler.py** - Class to handle the dictionary; Returns a list with words of the dictionary.
* **solution/SolutionHandler.py** - The class that implements the solution algorithm of the word ladder challenge
* **tests folder** - The unit test(s) of the solution resides here
* **tests/__init__.py** - Empty file; required to make Python treat directories as a package
* **tests/test_SolutionHandler.py** - Contains 4 basic test cases for SolutionHandler class
* **README.md** - This file


### Deliverables (tree mode)

```
.
├── README.md
├── resources
│   ├── config.ini
│   └── dictionary.txt
├── run.py
├── solution
│   ├── handlers
│   │   ├── OutputHandler.py
│   │   ├── ConfigHandler.py
│   │   ├── FileHandler.py
│   │   ├── __init__.py
│   │   └── SolutionHandler.py
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_SolutionHandler.py

4 directories, 12 files
```

### Resources


The following links helped the author of this coding challenge to better understand the nature of the problem and to synthesize this deliverable.

* https://en.wikipedia.org/wiki/Word_ladder
* https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
* https://www.geeksforgeeks.org/applications-of-breadth-first-traversal/
* https://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/
* https://learnbyinsight.com/2020/10/18/how-to-solve-word-ladder-problem/
* https://afteracademy.com/blog/word-ladder-problem

### Prerequisites

A working computer with Python 3 installed, preferably with a Linux based Operating System

### Usage

Open a terminal within the root folder of this deliverable and type:

```
python run.py --start-word head --end-word tail
```

The aforementioned command will print the sortest path followed to reach from the start word until the end word

Example output:

```
python run.py --start-word tail --end-word head
tail
hail
heil
heal
head
```

Should you need more help please type the below command

```
python run.py --help
```

The aforementioned command will provide you with some more helpful messages in order to execute this command line tool

Example output:

```
python run.py --help
usage: run.py [-h] --start-word START --end-word TARGET

Resolves the word ladder coding challenge

optional arguments:
  -h, --help          show this help message and exit
  --start-word START  The initial word
  --end-word TARGET   The target word
```

### Test execution

Open a terminal within the root folder of this deliverable and type:

```
python -m unittest discover
```

The aforementioned command will search under the tests directory all the files starting with test* and will execute the unit tests within them.

Example output:

```
python -m unittest discover
...
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

## Author

* **Lampros Batalas** - [email](mailto:labrosbat@gmail.com)
