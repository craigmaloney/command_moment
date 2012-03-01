import random

import json

class CommandList:
    def __init__(self):
        self.commands = []

    def load_commands(self):
        file = open('./commands.json', 'r')
        self.commands = json.load(file)
