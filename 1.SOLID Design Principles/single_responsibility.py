"""
    SRP - SOC
    ==========
    Single Responsibility Principle - Seperation of Concerns
    A class should have its main responsibilities and nothing more.
"""
import os
import sys


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

    # Not recommended changes - example of bad practice
    """
        Secondary responsibility of persistence outside of scope of class.
        This approach entails having to change every method that may be repeated
        in another place.
    """
    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass

class PersistenceManager:
    """Enforce sep of concerns. Better implemantation than above"""
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()



j = Journal()
j.add_entry('I walked outside.')
j.add_entry('I love my cat.')

print(f'Journal Entries:\n{j}')

filepath = os.getcwd() 

PersistenceManager.save_to_file(j, filepath+'\myjournal.txt')

with open(filepath + '\myjournal.txt', 'r') as fh:
    print(fh.read())

"""
    Avoid GOD Objects, that contain every possible function. Antipattern. Seperate Concerns.
"""