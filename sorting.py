""" Python script to implement some classic sorting algorithms; bubble, insertion and merge sort algorithms."""
import random


class Sorting(object):

    def __init__(self):
        """Constructor produces a new list of shuffled integers for every object."""
        self.numbers_list = [x for x in range(1, 11)]  # List comprehension to generate integers 1 through 10.
        random.shuffle(self.numbers_list)
        print(self.numbers_list)
   
    def bubble_sort(self):
        for i in range(0, len(self.numbers_list) - 1):
            for j in range(0, len(self.numbers_list) - 1 - i):
                if self.numbers_list[j] > self.numbers_list[j + 1]:
                    # Swap operation.
                    self.numbers_list[j], self.numbers_list[j + 1] = self.numbers_list[j + 1], self.numbers_list[j]
        return self.numbers_list
# TODO add insertion and merge sort algorithms
# TODO add functionality for numbers list to contain as many integers as necessary
# TODO allow user to choose which numbers they would like sorted


a = Sorting()
a.bubble_sort()
print(a.numbers_list)
