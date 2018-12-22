""" Python script to implement some simple sorting algorithms.
    I will handle the bubble, insertion and merge sort algorithms."""
import random


class Sorting(object):
    ''' constructor creates new data on every instance of the class.'''

    def __init__(self):
        self.numbers = []
        # List comprehension to generate integers 1 through 10.
        self.data = [x for x in range(1, 11)]
        random.shuffle(self.data)
        # Place those randomly ordered numbers in a list.
        self.numbers = self.data
        print(self.numbers)
   
    def bubble_sort(self):
        # Nested for loops to go through all elements.
        for i in range(0, len(self.numbers) - 1):
            for j in range(0, len(self.numbers) - 1 - i):
                if self.numbers[j] > self.numbers[j + 1]:
                    # Swap operation.
                    self.numbers[j], self.numbers[j + 1] = self.numbers[j + 1], self.numbers[j]
        return self.numbers


a = Sorting()
a.bubble_sort()
print(a.numbers)
