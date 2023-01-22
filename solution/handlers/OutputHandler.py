#!/usr/bin/python

from solution.handlers.ConfigHandler import ConfigHandler
from solution.handlers.SolutionHandler import SolutionHandler
from solution.handlers.FileHandler import FileHandler


def run(args):
    configHandler = ConfigHandler()
    dictpath = configHandler.get_config_value('CONFIG', 'dictionary')
    pool = FileHandler.get_list_from_dictionary(dictpath)
    solution = SolutionHandler(args.start, args.target, pool)
    for word in solution.get_sortest_list():
        print(word)
