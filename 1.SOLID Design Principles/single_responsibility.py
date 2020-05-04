"""
    SRP - SOC
    ==========
    Single Responsibility Principle - Seperation of Concerns
    A class should have its main responsibilities and nothing more.
"""

class Journal:
    """ Journal class simply allows you to add, remove and read entries"""
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

j = Journal()
j.add_entry('I walked outside.')
j.add_entry('I love my cat.')

print(f'Journal Entries:\n{j}')