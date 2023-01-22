#!/usr/bin/python

import sys


class SolutionHandler:

    def __init__(self, start, target, pool=[]):
        self.start = start
        self.target = target
        self.pool = pool
        self.bfsQueue = []

    def get_sortest_list(self):
        self.__word_validator(self.start, self.target, self.pool)
        if self.__differ_by_one(self.start, self.target):
            print([self.start, self.target])
        else:
            self.bfsQueue.append([self.start, [self.start]])
            while (len(self.bfsQueue) > 0):
                word, path = self.bfsQueue.pop(0)
                # Create list without the items already visited
                nextPossibleWords = [item for item in self.__find_possible_neighbours(word, self.pool) if item not in path]
                for nextPossibleWord in nextPossibleWords:
                    if nextPossibleWord == self.target:
                        path.append(self.target)
                        return path
                    else:
                        self.bfsQueue.append([nextPossibleWord, path + [nextPossibleWord]])

    def __word_validator(self, start, target, pool):
        # check if target exists in the pool
        if target in pool:
            pass
        else:
            sys.exit(0)

        # check if start and target word is the same
        if start == target:
            sys.exit(0)

    def __find_possible_neighbours(self, word, candidatesList):
        possiblenodes = []
        unique = []

        for candidate in candidatesList:
            if self.__differ_by_one(word, candidate):
                possiblenodes.append(candidate)

        uniqueNodes = set(possiblenodes)
        # Return unique list of next possible words
        for u in uniqueNodes:
            unique.append(u)
        return unique

    def __differ_by_one(self, start, target):
        # check if start and target words has (len(start) - 1) letters same
        counter = 0
        for i in range(len(start)):
            if start[i] == target[i]:
                counter += 1

        if counter == (len(start) - 1):
            return True
        return False
