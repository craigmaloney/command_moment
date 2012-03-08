import random
import json

class CommandList:
    def __init__(self):
        self.commands = {}

    def load_commands(self):
        file = open('./commands.json', 'r')
        self.commands = json.load(file)

    def active_commands(self):
        all_true = [key for key, val in self.commands.iteritems() if val]
        return all_true

    def pick_command(self):
        active = self.active_commands()
        random.shuffle(active)
        return active.pop()
