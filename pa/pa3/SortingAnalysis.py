# Hansol Lee
# PA 3: Sorting Analysis
# Version: 1.0
# Date: October 25, 2021
#
# This program is an implementation of doubly linked list through different sorting routines

from LinkedLists import DoublyLinkedList
import random
import time
import pandas as pd


def ascending_order(n):
    '''
    Creates a list of given size in ascending order
    :param n: size
    :return: list
    '''
    result = DoublyLinkedList()
    for i in range(0, n):
        result.append(i)
    return result


def descending_order(n):
    '''
    Creates a list of given size in descending order
    :param n: size
    :return: list
    '''
    result = DoublyLinkedList()
    for i in range(0, n):
        result.add(i)
    return result


def random_order(n):
    '''
    Creates a list of given size in random order
    :param n: size
    :return: list
    '''
    result = DoublyLinkedList()
    for i in range(0, n):
        result.append(random.randint(0, n))
    return result


class SortingAnalysis:
    def __init__(self, dll):
        '''
        Initializes global variables
        :param dll:
        '''
        self.algorithm = ""
        self.comp_count = 0
        self.swap_count = 0
        self.exec_time = 0
        self.dll = dll

    def selection_sort(self, dll):
        '''
        Performs selection sort
        :param dll: DLL to sort
        :return:
        '''
        start = time.time()
        # # duplicate dll without first element
        # temp_dll = DoublyLinkedList()
        # for node in dll:
        #     temp_dll.append(node)
        #
        # # iterator
        # for node in dll:
        #     temp = node
        #     for nextnode in temp_dll:
        #         if nextnode < node:
        #             temp = nextnode
        #             self.swap_count += 1
        #     original = node
        #     dll[dll.search(node)] = temp
        #     dll[dll.search(temp)] = original
        #     self.comp_count += 1

        for i in range(dll.size()):
            min_index = i
            for j in range(i + 1, dll.size()):
                if dll[j] < dll[min_index]:
                    min_index = j
                    self.swap_count += 1
            temp = dll[i]
            dll[i] = dll[min_index]
            dll[min_index] = temp
            self.comp_count += 1
        end = time.time()
        self.exec_time = end - start
        self.algorithm = 'selection_sort'

    def bubble_sort(self, dll):
        '''
        Performs bubble sort
        :param dll: DLL to sort
        :return:
        '''
        start = time.time()
        for i in range(dll.size() - 1):
            for j in range(dll.size() - 1):
                if dll[j + 1] < dll[j]:
                    temp = dll[j + 1]
                    dll[j + 1] = dll[j]
                    dll[j] = temp
                    self.swap_count += 1
            self.comp_count += 1
        end = time.time()
        self.exec_time = end - start
        self.algorithm = 'bubble_sort'

    def insertion_sort(self, dll):
        '''
        Performs insertion sort
        :param dll: DLL to sort
        :return:
        '''
        start = time.time()
        for i in range(1, dll.size()):
            current_value = dll[i]
            position = i
            while position > 0 and dll[position - 1] > current_value:
                dll[position] = dll[position - 1]
                position = position - 1
                self.swap_count += 1
            dll[position] = current_value
            self.comp_count += 1
        end = time.time()
        self.exec_time = end - start
        self.algorithm = 'insertion_sort'

    def shell_sort(self, dll):
        '''
        Performs shell sort
        :param dll: DLL to sort
        :return:
        '''
        start = time.time()
        temp = dll.size() // 2
        while temp > 0:
            for index in range(temp):
                self.gap_insertion(dll, index, temp)
            temp = temp // 2
            self.comp_count += 1
        end = time.time()
        self.exec_time = end - start
        self.algorithm = 'shell_sort'

    def gap_insertion(self, dll, index, temp):
        '''
        helper method for shell sort
        :param dll: DLL to sort
        :param index: index from for loop
        :param temp: gap
        :return:
        '''
        for i in range(index + temp, dll.size(), temp):
            current = dll[i]
            position = i
            while position >= temp and dll[position - temp] > current:
                dll[position] = dll[position - temp]
                position -= temp
                self.swap_count += 1
            dll[position] = current

    def merge_sort(self, dll):
        '''
        Performs merge sort
        :param dll: DLL to sort
        :return:
        '''
        start = time.time()
        if dll.size() <= 1:
            return
        mid = dll.size() // 2
        left = self.slice_helper(dll, 0, mid)
        right = self.slice_helper(dll, mid, dll.size())
        self.merge_sort(left)
        self.merge_sort(right)
        self.merge(dll, left, right)
        end = time.time()
        self.exec_time = end - start
        self.algorithm = 'merge_sort'

    def merge(self, dll, lefthalf, righthalf):
        '''
        helper method for merge sort
        :param dll: DLL to sort
        :param lefthalf: left half of the DLL
        :param righthalf: right half of the DLL
        :return:
        '''
        i = 0
        j = 0
        k = 0
        while i < lefthalf.size() and j < righthalf.size():
            if lefthalf[i] < righthalf[j]:
                dll[k] = lefthalf[i]
                self.swap_count += 1
                i += 1
            else:
                dll[k] = righthalf[j]
                self.swap_count += 1
                j += 1
            k += 1
            self.comp_count += 1
        while i < lefthalf.size():
            dll[k] = lefthalf[i]
            i += 1
            k += 1
            self.swap_count += 1
        while j < righthalf.size():
            dll[k] = righthalf[j]
            j += 1
            k += 1
            self.swap_count += 1

    def slice_helper(self, dll, index1, index2):
        '''
        helper method for merge sort
        :param dll: DLL to sort
        :param index1: first index
        :param index2: second index
        :return:
        '''
        half = DoublyLinkedList()
        i = 0
        while index1 < index2:
            half[i] = dll[index1]
            index1 += 1
            i += 1
        return half

    def quick_sort(self, dll):
        '''
        Performs quick sort
        :param dll: DLL to sort
        :return:
        '''
        start = time.time()
        if dll.size() <= 1:
            return
        self.quick_sort_helper(dll, 0, dll.size() - 1)
        end = time.time()
        self.exec_time = end - start
        self.algorithm = 'quick_sort'

    def quick_sort_helper(self, dll, start, end):
        '''
        helper method for quick sort
        :param dll: DLL to sort
        :param start: starting index
        :param end: ending index
        :return:
        '''
        if start < end:
            split_point = self.partition(dll, start, end)
            self.quick_sort_helper(dll, start, split_point - 1)
            self.quick_sort_helper(dll, split_point + 1, end)

    def partition(self, dll, start, end):
        '''
        helper method for quick sort
        :param dll: DLL to sort
        :param start: starting index
        :param end: ending index
        :return:
        '''
        pivot_value = dll[start]
        left_mark = start + 1
        right_mark = end
        while True:
            while left_mark <= right_mark and dll[left_mark] <= pivot_value:
                left_mark += 1
            while dll[right_mark] >= pivot_value and right_mark >= left_mark:
                right_mark -= 1
            if right_mark < left_mark:
                break
            else:
                temp = dll[left_mark]
                dll[left_mark] = dll[right_mark]
                dll[right_mark] = temp
                self.swap_count += 1
            self.comp_count += 1
        dll[start] = dll[right_mark]
        dll[right_mark] = pivot_value
        return right_mark

    def comp_size(self):
        '''
        Returns count of comparisons
        :return: count of comparisons
        '''
        return self.comp_count

    def swap_size(self):
        '''
        Returns count of swaps
        :return: count of swaps
        '''
        return self.swap_count

    def e_time(self):
        '''
        Returns execution time for the algorithm
        :return: execution time
        '''
        return self.exec_time

    def alg_type(self):
        '''
        Returns the algorithm type
        :return: String of algorithm type
        '''
        return self.algorithm


def create_table(size_list, order_type, alg_type, result):
    '''
    Creates table for the csv output
    :param size_list: size list
    :param order_type: order of the list
    :param alg_type: type of algorithm
    :param result: list of results
    :return:
    '''
    for i in range(0, len(size_list)):
        if order_type == "ascending":
            list_order = ascending_order(size_list[i])
            config = "Ascending Sorted N = %s" % size_list[i]
        elif order_type == "descending":
            list_order = descending_order(size_list[i])
            config = "Descending Sorted N = %s" % size_list[i]
        elif order_type == "random":
            list_order = random_order(size_list[i])
            config = "Randomly Sorted N = %s" % size_list[i]
        else:
            print("Order type is not valid. Please enter from the following: ascending, descending, random")
        sorting = SortingAnalysis(list_order)
        choose_algorithm(sorting, list_order, alg_type)
        row_data = [config, sorting.e_time(), sorting.comp_size(), sorting.swap_size()]
        result.append(row_data)


def choose_algorithm(sorting, list_order, alg_type):
    '''
    Identifies the algorithm to perform
    :param sorting: sorting analysis object
    :param list_order: order of the list
    :param alg_type: type of algorithm
    :return:
    '''
    if alg_type == "selection":
        sorting.selection_sort(list_order)
    elif alg_type == "bubble":
        sorting.bubble_sort(list_order)
    elif alg_type == "insertion":
        sorting.insertion_sort(list_order)
    elif alg_type == "shell":
        sorting.shell_sort(list_order)
    elif alg_type == "merge":
        sorting.merge_sort(list_order)
    elif alg_type == "quick":
        sorting.quick_sort(list_order)
    else:
        print("Algorithm type is not valid. Please enter from the following: selection, bubble, insertion, shell, "
              "merge, quick")


def main():
    size_list = [10, 100]
    alg_list = ["selection", "bubble", "insertion", "shell", "merge", "quick"]
    column_names = ["List Configuration", "Time (in seconds)", "Data Comparisons (count)", "Data Swaps (count)"]
    for alg in alg_list:
        analysis_report = open("%s_sort_results.csv" % alg, mode='w+')
        result = []
        create_table(size_list, "ascending", alg, result)
        create_table(size_list, "descending", alg, result)
        create_table(size_list, "random", alg, result)
        df = pd.DataFrame(result, columns=column_names)
        df.to_csv(analysis_report)
        analysis_report.close()


main()