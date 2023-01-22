__author__ = 'Lampros BATALAS'

import sys
import argparse

import solution.handlers.OutputHandler as Out


def main():

    parser = argparse.ArgumentParser(description='Resolves the word ladder challenge')

    parser.add_argument('--start-word',
                        required=True,
                        dest='start',
                        help="""The initial word""")

    parser.add_argument('--end-word',
                        required=True,
                        dest='target',
                        help="""The target word""")

    parser.set_defaults(func=Out.run)
    args = parser.parse_args(sys.argv[1:len(sys.argv)])
    args.func(args)
