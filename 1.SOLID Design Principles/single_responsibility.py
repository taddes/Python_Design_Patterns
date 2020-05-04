"""
    SRP - SOC
    ==========
    Single Responsibility Principle - Seperation of Concerns
    A class should have its main responsibilities and nothing more.
"""

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

        def add_entry(self, text):
            self.count += 1
            self.entries.append(f'{self.count}: {text}')

        def remove_entry(self, pos):
            del self.entries[pos]