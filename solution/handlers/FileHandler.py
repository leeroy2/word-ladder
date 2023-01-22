#!/usr/bin/python


class FileHandler:

    @staticmethod
    def get_list_from_dictionary(path):
        pool = []
        with open(path) as dictionary:
            for word in dictionary:
                pool.append(word.rstrip('\n'))
        return pool
