""" Python script to implement some classic sorting algorithms; bubble, insertion and merge sort algorithms."""
from random import shuffle


class Sorting(object):

    def __init__(self):
        self.swapped = False
        self.numbers_list = []
        self.insertion_position = 0
        self.value_to_insert = 0

    def get_user_input(self):
        """This function allows the user to specify how many and which integers they would like to be sorted. Returns
        a list of randomly arranged integers provided by the user."""
        n = int(input("How many numbers would you like sorted? "))
        for i in range(n):
            print("Enter number", i + 1)
            number = int(input())
            self.numbers_list.append(number)
        return self.numbers_list

    def shuffle_user_input(self):
        shuffle(self.numbers_list)
        return self.numbers_list

    def bubble_sort(self):
        """This sorting algorithm is a comparison-based algorithm in which each
        pair of adjacent elements is compared and the elements are swapped if they are not in order. Returns a sorted
        list."""
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
        """This is an in-place comparison-based sorting algorithm. Here, a sub-list is maintained which is always sorted.
        For example, the lower part of an array is maintained to be sorted. An element which is to be 'insert'ed in this
        sorted sub-list, has to find its appropriate place and then it has to be inserted there. Hence the name,
        insertion sort. Returns a sorted list."""
        for i in range(len(self.numbers_list) - 1):
            self.insertion_position = i
            self.value_to_insert = self.numbers_list[i]
            while self.insertion_position > 0 and self.numbers_list[self.insertion_position - 1] > self.value_to_insert:
                self.insertion_position -= 1
            self.numbers_list[self.insertion_position] = self.value_to_insert
        return self.numbers_list

    def merge_sort(self):
        pass


# TODO add merge sort algorithm
# TODO add boolean check to see if original input list is already sorted


# Objects for debugging purposes
a = Sorting()
print("Original list:", a.get_user_input())
print("Shuffled list:", a.shuffle_user_input())
a.bubble_sort()
# a.insertion_sort()
print("Sorted list:", a.numbers_list)
