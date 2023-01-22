#!/usr/bin/python
import configparser


class ConfigHandler:
    config = configparser.ConfigParser()

    def __init__(self):
        self.config.read('./resources/config.ini')

    def get_config_value(self, _section, _key):
        return self.config.get(_section, _key)
