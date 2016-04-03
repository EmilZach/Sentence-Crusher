#!/usr/bin/env python
# coding: utf-8


class DataGuy:
    """ This class handles data for the server"""
    def __init__(self, new_data):

        self.new_data = new_data
        self.points = new_data[0]
        self.user = new_data[1]
        self.level = new_data[4]

        self.level_history = {}

        print("Dataguy initialized")

