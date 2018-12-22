""" Python script to implement some classic sorting algorithms; bubble, insertion and merge sort algorithms."""
import random


class Sorting(object):
    """Constructor creates new data on every instance of the class."""

    def __init__(self):
        self.numbers_list = []
        # List comprehension to generate integers 1 through 10.
        self.data = [x for x in range(1, 11)]
        random.shuffle(self.data)
        self.numbers_list = self.data
        print(self.numbers_list)
   
    def bubble_sort(self):
        for i in range(0, len(self.numbers_list) - 1):
            for j in range(0, len(self.numbers_list) - 1 - i):
                if self.numbers_list[j] > self.numbers_list[j + 1]:
                    # Swap operation.
                    self.numbers_list[j], self.numbers_list[j + 1] = self.numbers_list[j + 1], self.numbers_list[j]
        return self.numbers_list
# TODO add insertion and merge sort algorithms
# TODO choose better variable name for data variable


a = Sorting()
a.bubble_sort()
print(a.numbers_list)
