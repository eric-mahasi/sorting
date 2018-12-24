""" Python script to implement some classic sorting algorithms; bubble, insertion and merge sort algorithms."""
import random


class Sorting(object):

    def __init__(self):
        """Constructor produces a new list of shuffled integers for every object."""
        self.swapped = False
        self.numbers_list = [x for x in range(1, 11)]  # List comprehension to generate integers 1 through 10.
        random.shuffle(self.numbers_list)
        print(self.numbers_list)

    def bubble_sort(self):
        for i in range(len(self.numbers_list) - 1):
            for j in range(len(self.numbers_list) - 1 - i):
                if self.numbers_list[j] > self.numbers_list[j + 1]:
                    self.numbers_list[j], self.numbers_list[j + 1] = self.numbers_list[j + 1], self.numbers_list[j]
                    # Swap operation.
                    self.swapped = True
            if not self.swapped:  # If no numbers swapped, that means that list is sorted.
                break
        return self.numbers_list

    def insertion_sort(self):
        for i in range(len(self.numbers_list) - 1):
            self.insertion_position = i
            self.value_to_insert = self.numbers_list[i]
            while self.insertion_position > 0 and self.numbers_list[self.insertion_position - 1] > self.value_to_insert:
                self.insertion_position -= 1
            self.numbers_list[self.insertion_position] = self.value_to_insert

    def merge_sort(self):
        pass

# TODO add merge sort algorithm
# TODO add functionality for numbers list to contain as many integers as necessary
# TODO allow user to choose which numbers they would like sorted
# TODO add some print statements to clarify output
# TODO add some documentation to explain how functions work


a = Sorting()
a.bubble_sort()
a.insertion_sort()
print(a.numbers_list)
print(a.numbers_list)
